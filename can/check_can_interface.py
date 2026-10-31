"""Check the DBC design on a PC; this is not ECU firmware or a bus test.

Install the version in can-design-requirements.txt, then run:
  python3 check_can_interface.py
The DBC and generated report are beside this script.
"""
from pathlib import Path
from itertools import product
from datetime import datetime, timezone
import hashlib
import json
import platform
import cantools
from cantools.database.errors import EncodeError

HERE = Path(__file__).resolve().parent
DBC = HERE / 'vehicle-lamp.dbc'

def check(condition, label):
    if not condition:
        raise AssertionError(label)

def independent_encode(signals):
    return (signals['IGN'] | signals['TURN'] << 1 | signals['HAZARD'] << 3
            | signals['TAIL'] << 4 | signals['BRAKE'] << 5
            | signals['REVERSE'] << 6)

def design_receive(message, data, *, frame_id=0x100, dlc=1,
                   extended=False, remote=False, fd=False, error=False):
    """Reference acceptance rule only; no timers, output control or state update."""
    if (frame_id != 0x100 or dlc != 1 or len(data) != 1
            or extended or remote or fd or error):
        return None
    decoded = message.decode(data, decode_choices=False,
                             allow_truncated=False, allow_excess=False)
    if decoded['TURN'] == 3 or decoded['RESERVED'] != 0:
        return None
    return decoded

def main():
    database = cantools.database.load_file(str(DBC), encoding='utf-8', strict=True)
    check(len(database.messages) == 1, 'Exactly one command message')
    msg = database.get_message_by_name('LAMP_COMMAND')
    check(msg.frame_id == 0x100 and not msg.is_extended_frame and not msg.is_fd,
          'Standard Classical CAN message')
    check(msg.length == 1 and msg.cycle_time == 50, 'DLC and cycle time')
    check(msg.senders == ['BCM_SIM'], 'Sender')
    check(database.dbc.attributes['NominalBitrate'].value == 500000, 'Bitrate metadata')
    layout = {'IGN': (0, 1, 0, 1), 'TURN': (1, 2, 0, 2),
              'HAZARD': (3, 1, 0, 1), 'TAIL': (4, 1, 0, 1),
              'BRAKE': (5, 1, 0, 1), 'REVERSE': (6, 1, 0, 1),
              'RESERVED': (7, 1, 0, 1)}
    check(set(s.name for s in msg.signals) == set(layout), 'Signal set')
    for s in msg.signals:
        check((s.start, s.length, s.minimum, s.maximum) == layout[s.name], s.name)
        check(s.byte_order == 'little_endian' and not s.is_signed, s.name + ' type')
        check(s.receivers == ['REAR_LAMP_ECU'], s.name + ' receiver')

    count = 0
    for ign, turn, hazard, tail, brake, reverse in product(range(2), range(3),
                                                         range(2), range(2), range(2), range(2)):
        signals = dict(IGN=ign, TURN=turn, HAZARD=hazard, TAIL=tail,
                       BRAKE=brake, REVERSE=reverse, RESERVED=0)
        payload = msg.encode(signals, strict=True)
        check(payload == bytes([independent_encode(signals)]), 'Independent bit layout')
        check(design_receive(msg, payload) == signals, 'Roundtrip')
        count += 1
    check(count == 96, 'All normal combinations covered')

    accepted, rejected = [], []
    for value in range(256):
        result = design_receive(msg, bytes([value]))
        expected = (value & 0x80) == 0 and ((value >> 1) & 3) != 3
        check((result is not None) == expected, f'Byte classification: {value:02X}')
        (accepted if expected else rejected).append(value)
    check(len(accepted) == 96 and len(rejected) == 160, 'All bytes classified')

    malformed = [
        ('wrong_id', b'\x00', {'frame_id': 0x101}),
        ('dlc_zero', b'\x00', {'dlc': 0}),
        ('dlc_two', b'\x00', {'dlc': 2}),
        ('empty_payload', b'', {}),
        ('excess_payload', b'\x00\x00', {}),
        ('extended_frame', b'\x00', {'extended': True}),
        ('remote_frame', b'\x00', {'remote': True}),
        ('fd_frame', b'\x00', {'fd': True}),
        ('error_frame', b'\x00', {'error': True}),
    ]
    for label, data, attrs in malformed:
        check(design_receive(msg, data, **attrs) is None, label)

    baseline = dict(IGN=0, TURN=0, HAZARD=0, TAIL=0, BRAKE=0, REVERSE=0, RESERVED=0)
    strict_rejections = []
    for key, value in [('TURN', 3), ('IGN', 2)]:
        try:
            msg.encode({**baseline, key: value}, strict=True)
        except EncodeError:
            strict_rejections.append(key)
        else:
            raise AssertionError('Strict encoding accepted ' + key)

    # The DBC parser can decode out-of-range raw values. Application checks remain necessary.
    check(msg.decode(b'\x06', decode_choices=False)['TURN'] == 3,
          'Decoder does not automatically enforce application validity')
    check(msg.encode({**baseline, 'RESERVED': 1}, strict=True) == b'\x80',
          'Reserved field raw range is not the application acceptance rule')
    check(design_receive(msg, b'\x80') is None, 'Application rejects reserved bit one')
    examples = []
    for label, value in [('ALL_OFF', 0x00), ('IGN_LEFT', 0x03),
                         ('IGN_RIGHT', 0x05), ('HAZARD_IGN_OFF', 0x08),
                         ('TAIL_ONLY', 0x10), ('BRAKE_ONLY', 0x20),
                         ('IGN_REVERSE', 0x41), ('ALL_REQUESTS_RIGHT', 0x7D)]:
        decoded = design_receive(msg, bytes([value]))
        check(decoded is not None, label)
        examples.append({'name': label, 'id': '0x100', 'dlc': 1,
                         'data_hex': f'{value:02X}', 'signals': decoded})

    report = {
        'scope': 'Offline DBC and reference acceptance-rule design checks only',
        'status': 'passed',
        'executed_at_utc': datetime.now(timezone.utc).isoformat(),
        'python': platform.python_version(), 'cantools': cantools.__version__,
        'dbc_sha256': hashlib.sha256(DBC.read_bytes()).hexdigest(),
        'normal_roundtrips': count, 'raw_payloads_classified': 256,
        'normal_payload_count': len(accepted), 'invalid_payload_count': len(rejected),
        'malformed_frame_checks': [x[0] for x in malformed],
        'strict_encoder_rejections': strict_rejections, 'examples': examples,
        'not_executed': ['ECU firmware tests', 'Physical CAN communication',
                         '50 ms transmission scheduling', '200 ms timeout behavior',
                         '10 ms / 50 ms response timing', 'LED output behavior'],
    }
    path = HERE / 'CAN-interface-check-results.json'
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: report[k] for k in ['status', 'cantools', 'normal_roundtrips',
                                            'raw_payloads_classified', 'invalid_payload_count']}, indent=2))
    print('Malformed frame checks:', len(malformed))
    print('Report:', path)

if __name__ == '__main__':
    main()

