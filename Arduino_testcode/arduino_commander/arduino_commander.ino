void setup() {
  Serial.begin(9600); // Start serial communication at 9600 baud
}

void loop() {
  if (Serial.available() > 0) {
    char incomingByte = Serial.read();
    
    if (incomingByte == '1') {
      double x = 56.60; // Define the value of x
      Serial.println(x);
    }
  }
  delay(1000); // Wait for 1 second before checking again
}
