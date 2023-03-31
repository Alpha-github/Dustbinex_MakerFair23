#include <Servo.h>
Servo myservo;
int close=180;
int open=155;
void setup() {
  Serial.begin(9600);
  Serial.println("Serial Monitor Started");

  pinMode(13,OUTPUT);
  pinMode(10,INPUT);
  myservo.attach(7);
  myservo.write(180);
}

void loop() {
  
  if(Serial.available())
  {
    char a  = Serial.read();
    Serial.println(a);
    int capac = digitalRead(10);
    if(capac==LOW){
      if(a=='1')
      {
        for(int i=close; i>=open; i=i-2)
        {
          myservo.write(i);
          delay(15);
        }
        delay(5000);
        for(int i=open; i<=close; i=i+2)
        {
          myservo.write(i);
          delay(15);
        }
      }
      else{
        myservo.write(180);
      }
    }
    else
    {
      myservo.write(180);
      Serial.println("Dustbin Full");
      digitalWrite(13,HIGH);
    }
  }
}
