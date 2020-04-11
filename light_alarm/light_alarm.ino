int sensorValue = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // pinMode(8,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  sensorValue = analogRead(A0);
  Serial.println(sensorValue);

  if(sensorValue >= 3) {
    tone(8,sensorValue*50);
  }
  else {
    noTone(8);
  }
}
