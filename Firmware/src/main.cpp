/**
 * @file main.cpp
 * @author Joe S (kenwood364@gmail.com)
 * @brief Entrypoint for the KW1FOX-2 Radio Station
 *
 * @copyright Copyright (c) 2022
 *
 */

#include <Arduino.h>

#include <Arduino.h>

#include <Nokia_LCD.h>

Nokia_LCD lcd(7 /* CLK */, 6 /* DIN */, 5 /* DC */, 4 /* CE */, 3 /* RST */);

// Based on https://github.com/platisd/nokia-5110-lcd-library/tree/master/examples/Nokia_LCD_Demo

void setup()
{
    // Initialize the screen
    lcd.begin();
    // Set the contrast

    lcd.setContrast(60); // Good values are usualy between 40 and 60

    // Clear the screen by filling it with black pixels
    lcd.clear(true);

    delay(2000);

    // Set the cursor on the beginning of the 6th row (the last one)
    lcd.setCursor(0, 5);

    // Write something on the specific row with inverted color
    lcd.setInverted(true);
    lcd.print("Hello world!");
}

void loop()
{
    delay(200);
}