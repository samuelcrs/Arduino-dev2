#include <SPI.h>
#include <Ethernet.h>
 
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
byte ip[] = { 169, 254, 39, 10 };
    
EthernetServer server(80);
 
String readString;
int Pin = 6;
int Pin2 = 7;
 
void setup(){
 
  pinMode(Pin, OUTPUT);
  pinMode(Pin2, OUTPUT);
  Ethernet.begin(mac, ip);
  server.begin();
}
 
void loop(){
  EthernetClient client = server.available();
  if (client) {
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
 
        if (readString.length() < 100) {
          readString += c;              
        }

        if (c == '\n') {
         
          
          
          delay(1);
          client.stop();
          
          if(readString.indexOf("?ledon") > 0)
          {
            digitalWrite(Pin, HIGH);
          }
          else {
            if(readString.indexOf("?ledoff") > 0)
            {
              digitalWrite(Pin, LOW);
            }
          }
            if(readString.indexOf("?led2on") > 0)
          {
            digitalWrite(Pin2, HIGH);
          }
          else {
            if(readString.indexOf("?led2off") > 0)
            {
              digitalWrite(Pin2, LOW);
            }
          }
          readString="";     
        }
      }
    }
  }
}

