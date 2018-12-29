/*

*/
int incomingByte = 0;
int NTCpin = A7;
int Lightpin = A6;
int Moistpin = A5;
int analogValue;
int NTCvalue;
int LightValue;
int MoistValue;
int buttonReading;
const int ledPinGreen = 2;
const int ledPinYellow = 3;
const int ledPinBlue = 4;
const int button = 5;
int ledState = LOW;
int pin = ledPinGreen;
float k = 5.0/1023.0;/*k faktor*/
float Vm;
float NTCresistance;
String inByte;
void setup() {
  pinMode(Moistpin, INPUT);
  pinMode(NTCpin, INPUT);
  pinMode(Lightpin, INPUT);
  pinMode(ledPinGreen, OUTPUT);
  pinMode(ledPinYellow, OUTPUT);
  pinMode(ledPinBlue, OUTPUT);
  pinMode(button, INPUT);
  digitalWrite(ledPinGreen, LOW);
  digitalWrite(ledPinYellow, LOW);
  digitalWrite(ledPinBlue, LOW);
  Serial.begin(9600);
  Serial.println("Arduino ready");
}

void loop() {
  
 //Serial.println(analogValue);
  //Serial.print("NTC value: ");
  //Serial.println(NTCvalue);
  //Serial.print("Light value: ");
  //Serial.println(LightValue);
  
   if (Serial.available() > 0) {
    // get incoming byte:
    inByte = Serial.readString();
    if(inByte.equals("moist\r\n")){
      MoistValue = analogRead(Moistpin);
      Serial.print("Moistvalue: ");
      Serial.println(MoistValue); 
    }
    if(inByte.equals("ntc")){
      NTCvalue = analogRead(NTCpin);
      Serial.print("NTCvalue: ");
      Serial.println(NTCvalue); 
    }
    if(inByte.equals("light")){
      LightValue = analogRead(Lightpin);
      Serial.print("Light: ");
      Serial.println(LightValue); 
    }
    Serial.println(inByte);
  }
  
}
