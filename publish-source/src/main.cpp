#include <Arduino.h>

const int inputPin = 12;

const int readingsPerSecond = 50;
const int interval = 1000 / readingsPerSecond;

unsigned long previousMillis = 0;

void setup()
{
  Serial.begin(115200);
  pinMode(inputPin, INPUT);
}

void loop()
{
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval)
  {
    int value = analogRead(inputPin);
    previousMillis = currentMillis;
    Serial.print(currentMillis);
    Serial.print(", ");
    Serial.println(value);
  }
}
