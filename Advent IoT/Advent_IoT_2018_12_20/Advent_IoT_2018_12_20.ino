/*

*/
int incomingByte = 0;
int analogPin = A5;
int NTCpin = A7;
int analogValue;
int NTCvalue;
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
void setup() {
  pinMode(analogPin, INPUT);
  pinMode(NTCpin, INPUT);
  pinMode(ledPinGreen, OUTPUT);
  pinMode(ledPinYellow, OUTPUT);
  pinMode(ledPinBlue, OUTPUT);
  pinMode(button, INPUT);
  digitalWrite(ledPinGreen, LOW);
  digitalWrite(ledPinYellow, LOW);
  digitalWrite(ledPinBlue, LOW);
  Serial.begin(9600);
}

void loop() {
  analogValue = analogRead(analogPin);
  NTCvalue = analogRead(NTCpin);
  Vm=NTCvalue*k;
  NTCresistance = 1000*Vm/(5.0-Vm);
 //Serial.println(analogValue);
  buttonReading = digitalRead(button);
  Serial.println(analogValue);
  Serial.print("NTC value: ");
  Serial.println(NTCvalue);
  Serial.print("NTC: ");
  Serial.println(NTCresistance,10);
  delay(analogValue);
  digitalWrite(ledPinGreen, LOW);
  digitalWrite(ledPinBlue, HIGH );
  delay(analogValue);
  digitalWrite(ledPinBlue, LOW);
  digitalWrite(ledPinYellow, HIGH);

  delay(analogValue);
  digitalWrite(ledPinYellow, LOW);
  digitalWrite(ledPinGreen, HIGH);
  
}
