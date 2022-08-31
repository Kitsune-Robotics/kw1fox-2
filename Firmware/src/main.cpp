/**
 * @file main.cpp
 * @author Joe S (kenwood364@gmail.com)
 * @brief Entrypoint for the KW1FOX-2 Radio Station
 *
 * @copyright Copyright (c) 2022
 *
 */

#include <Arduino.h>

// #include <FreeRTOS.h>

void setup()
{
    Serial.begin();
    Serial.println("Hello world.");

    pinMode(16, OUTPUT);
}

void loop()
{
    Serial.println("Greatness awaits..");

    delay(100);
    digitalWrite(16, HIGH);
}
