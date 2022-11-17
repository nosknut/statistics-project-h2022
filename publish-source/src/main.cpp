#include <Arduino.h>

const int inputPin2 = 27;
const int inputPin = 12;
const int outputPin = 14;

const int readingsPerSecond = 250;
const int interval = 1000 / readingsPerSecond;

unsigned long previousMillis = 0;

void setup()
{
  Serial.begin(115200);
  pinMode(inputPin, INPUT);
  pinMode(inputPin2, INPUT);
  pinMode(outputPin, OUTPUT);
}

void printSource()
{
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval)
  {
    previousMillis = currentMillis;
    Serial.print(currentMillis);
    Serial.print(", ");
    Serial.print(analogRead(inputPin));
    Serial.print(", ");
    Serial.println(analogRead(inputPin2));
  }
}

void printOut()
{
  analogWrite(outputPin, map(3000, 0, 4095, 0, 255));
  while (true)
  {
    unsigned long currentMillis = millis();
    if (currentMillis - previousMillis >= interval)
    {
      previousMillis = currentMillis;
      Serial.print(currentMillis);
      Serial.print(", ");
      Serial.print(analogRead(inputPin));
      Serial.print(", ");
      Serial.println(analogRead(inputPin2));
    }
  }
}

void ramp()
{
  for (int i = 0; i < 250; i++)
  {
    analogWrite(outputPin, i);
    delay(10);
    Serial.print(map(i, 0, 255, 0, 4095));
    Serial.print(", ");
    Serial.print(analogRead(inputPin));
    Serial.print(", ");
    Serial.println(analogRead(inputPin2));
  }
  for (int i = 255; i > 0; i--)
  {
    analogWrite(outputPin, i);
    delay(10);
    Serial.print(map(i, 0, 255, 0, 4095));
    Serial.print(", ");
    Serial.print(analogRead(inputPin));
    Serial.print(", ");
    Serial.println(analogRead(inputPin2));
  }
}

void loop()
{
  printOut();
}