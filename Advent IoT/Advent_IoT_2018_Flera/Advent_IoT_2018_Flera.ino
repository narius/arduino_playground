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
char inByte;
String command;
bool clearCommand=false;
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
  Serial.flush(); //flush all previous received and transmitted data
  while(!Serial.available()) ;
  //while (!Serial.available()) {}
 //Serial.println(analogValue);
  //Serial.print("NTC value: ");
  //Serial.println(NTCvalue);
  //Serial.print("Light value: ");
  //Serial.println(LightValue);
  
   /*while (Serial.available()>0) {
    // get incoming byte:
    inByte = Serial.read();
    if(inByte!='\n'){
    command+=inByte;
    }
    else{
    clearCommand=true;
    }
   }*/
   if (Serial.available()){
      //command=Serial.readString();
      command=Serial.readStringUntil('\n');
    }
    if(command.equals("moisture")){
      MoistValue = analogRead(Moistpin);
      Serial.println(MoistValue); 
    }
    if(command.equals("temperature")){
      NTCvalue = analogRead(NTCpin);
      Serial.println(NTCvalue); 
    }
    if(command.equals("light")){
      LightValue = analogRead(Lightpin);
      Serial.println(LightValue); 
    }
    if(command.equals("blue_on")){//Turn on and off diods
      digitalWrite(ledPinBlue, HIGH);
    }
    if(command.equals("blue_off")){//Turn on and off diods
      digitalWrite(ledPinBlue, LOW);
    }
    else{
      Serial.print("fel: ");
      Serial.println(command);
    }
    if(clearCommand){
      command="";
      }
    
  
}
