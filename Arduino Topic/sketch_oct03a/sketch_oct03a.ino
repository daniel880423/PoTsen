#include <Console.h>
void setup() {
  Bridge.begin();
  Console.begin();  
}
 
void loop() {
  int val = analogRead(A0);
  Console.println(val, DEC);
  delay(500);
}
