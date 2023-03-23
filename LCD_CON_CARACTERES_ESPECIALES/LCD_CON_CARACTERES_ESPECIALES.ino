#include <LiquidCrystal.h>

LiquidCrystal lcd(7,6,5,4,3,2); //RS,EN,D4,D3,D2,D1
byte nombre[] = {
      0b00000,
    0b11011,
    0b11111,
    0b11111,
    0b01110,
    0b00100,
    0b00000,
    0b00000
};

byte imagen[] = {
    0b01110,
    0b10001,
    0b10001,
    0b01110,
    0b11111,
    0b00100,
    0b11111,
    0b11111
};
byte arroba[] = {
    0b01110,
    0b10001,
    0b10001,
    0b01101,
    0b10101,
    0b10101,
    0b11111,
    0b00000
};
int i;
void setup() {
lcd.begin(16,2);
lcd.createChar(1,nombre);
lcd.createChar(2,imagen);
lcd.createChar(3,arroba);
}
void loop() {
lcd.setCursor(0,0);
lcd.print("@ELECTRO_ARDUINO_PROGRAMACION");
lcd.setCursor(2,2);
lcd.write(1);
lcd.setCursor(10,2);
lcd.write(3);
lcd.setCursor(20,2);
lcd.write(2);
lcd.setCursor(0,1);
for ( i=0 ;i <16;i++){
  lcd.scrollDisplayLeft();
  delay(100);
}
for (i=0 ;i<16; i++){
  lcd.scrollDisplayRight();
  delay(100);
}

}
