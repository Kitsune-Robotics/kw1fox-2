/**
 * @file main.cpp
 * @author Joe S (kenwood364@gmail.com)
 * @brief Entrypoint for the KW1FOX-2 Radio Station
 *
 * @copyright Copyright (c) 2022
 *
 */

#include <Arduino.h>
#include <FreeRTOS.h>

// Filesystems and SD
#include <SDFS.h>

void setup()
{
    Serial.begin();
    delay(2000);

    Serial.println("Initializing Devices.");
    delay(500);

    Serial.println("SDFS Bringup");
    // SDFS Settings
    SDFSConfig c2;
    c2.setCSPin(4);
    SDFS.setConfig(c2);

    // Begin SDFS
    if (!SDFS.begin())
    {
        Serial.println("Unable to bringup, formatting SPIFFS, see manual https://arduino-pico.readthedocs.io/en/latest/fs.html#begin");
    }

    Serial.println("initialization done.");

    // Do some filesystem testing
    if (!SDFS.exists("/Logs/"))
    { // If there is no logfolder
        SDFS.mkdir("/Logs/");
    }

    if (!SDFS.exists("/Logs/myLogFile.log"))
    {
        SDFS.open("/Logs/myLogFile.log", "a");
    }
    else
    {
        SDFS.open("/Logs/myLogFile.log", "a");
    }

    pinMode(16, OUTPUT);
}

void loop()
{
    Serial.println("Greatness awaits..");

    delay(1000);
    digitalWrite(16, HIGH);
    delay(1000);
    digitalWrite(16, LOW);
}
