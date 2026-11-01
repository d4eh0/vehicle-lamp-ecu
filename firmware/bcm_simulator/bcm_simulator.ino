#include <CAN.h>

// bit0 IGN, bit1~2 TURN, bit3 HAZARD, bit4 TAIL,
// bit5 BRAKE, bit6 REVERSE, bit7 RESERVED=0
const uint8_t commands[] = {0x03, 0x05, 0x0B, 0x10, 0x30, 0x41, 0x03};
const char *const names[] = {
    "LEFT", "RIGHT", "HAZARD", "TAIL", "BRAKE", "REVERSE", "LEFT", "TX PAUSE"
};
bool canReady = false;
uint32_t sequenceStart = 0;
uint32_t lastSend = 0;
uint32_t lastPrint = 0;
uint8_t previousStep = 255;
int lastTxResult = 0;

void setup()
{
    Serial.begin(115200);
    uint32_t waitStart = millis();
    while (!Serial && (uint32_t)(millis() - waitStart) < 3000UL)
        delay(10);

    canReady = CAN.begin(CanBitRate::BR_500k);
    Serial.println(canReady ? "CAN init OK" : "CAN init FAILED");
    sequenceStart = millis();
}

void loop()
{
    uint32_t now = millis();
    if (!canReady)
    {
        if ((uint32_t)(now - lastPrint) >= 1000UL)
        {
            lastPrint = now;
            Serial.println("CAN init FAILED");
        }
        delay(10);
        return;
    }

    uint8_t step = ((uint32_t)(now - sequenceStart) / 3000UL) % 8UL;
    bool changed = (step != previousStep);
    previousStep = step;
    if (step != 7U)
    {
        if (changed || (uint32_t)(now - lastSend) >= 50UL)
        {
            lastSend = now;
            uint8_t data[1] = {commands[step]};
            CanMsg message(CanStandardId(0x100), sizeof(data), data);
            Serial.println("TX start");
            lastTxResult = CAN.write(message);
            Serial.print("TX return=");
            Serial.println(lastTxResult);
        }
    }

    if ((uint32_t)(now - lastPrint) >= 1000UL)
    {
        lastPrint = now;
        Serial.print("mode=");
        Serial.print(names[step]);
        if (step == 7U)
            Serial.println(" / transmission paused");
        else
        {
            Serial.print(" / TX result=");
            Serial.print(lastTxResult);
            Serial.print(" / ID=0x100 / data=0x");
            Serial.println(commands[step], HEX);
        }
    }
    delay(1);
}
