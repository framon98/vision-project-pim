#include <SoftwareSerial.h>
#include <TinyGPS.h>

SoftwareSerial gps(4,3);
TinyGPS decodegps;


char data=' ';

void setup()
{
 Serial.begin(9600);            
 gps.begin(9600); 
}


void loop()
{
  if(gps.available())
  {
    data=gps.read();
    Serial.print(data);

    bool temp = decodegps.encode(data);
    

//    if(decodegps.encode(data))  
//    {
//      float latitude, longitude;
//      decodegps.f_get_position(&latitude, &longitude);
//      Serial.print("Latitud/Longitud: "); 
//      Serial.print(latitude); 
//      Serial.print(", "); 
//      Serial.println(longitude);
//
//    }
  }
}
