#include <Arduino.h>

const int inputPin = 12;
const int outputPin = 14;

const int readingsPerSecond = 85;
const int interval = 1000 / readingsPerSecond;

unsigned long previousMillis = 0;

void setup()
{
  Serial.begin(115200);
  pinMode(inputPin, INPUT);
  pinMode(outputPin, OUTPUT);
}

void printSource()
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

void printOut()
{
  int i = 1;
  // analogWrite(outputPin, map(1877, 0, 4095, 0, 255));
  while (true)
  {
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= interval)
    {
      analogWrite(outputPin, i);
      i += 1;
      Serial.println(i);
      // int value = analogRead(inputPin);
      previousMillis = currentMillis;
      // Serial.print(currentMillis);
      // Serial.print(", ");
      // Serial.println(value);
    }
  }
}

void ramp()
{
  for (int i = 0; i < 255; i++)
  {
    analogWrite(outputPin, i);
    delay(10);
    Serial.print(map(i, 0, 255, 0, 4095));
    Serial.print(", ");
    Serial.println(analogRead(inputPin));
  }
  for (int i = 255; i > 0; i--)
  {
    analogWrite(outputPin, i);
    delay(10);
    Serial.print(map(i, 0, 255, 0, 4095));
    Serial.print(", ");
    Serial.println(analogRead(inputPin));
  }
}

void loop()
{
  ramp();
}