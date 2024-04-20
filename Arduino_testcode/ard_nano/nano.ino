
const int flexPin = A6;
const int buttonPin = 2; // Change to the pin connected to your button
const int sampleDuration = 10000; // 10 seconds in milliseconds
const int sampleInterval = 200; // Interval between samples
const int numSamples = sampleDuration / sampleInterval;
int samples[numSamples];
int currentIndex = 0;
bool recording = false;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT_PULLUP);
}

void loop() {
  if (Serial.available() > 0) {
    char signal = Serial.read();
    if (signal == '1') { 
      recordData();
    }
  }
}

void recordData() {
  // Serial.println("Recording data.. Move the finger...");// display as dialog box
  recording = true;
  unsigned long startTime = millis();
  
  while (millis() - startTime < sampleDuration) {
    int flexVal = analogRead(flexPin);
    float angle = map(flexVal, 129, 255, 90, 0);
    samples[currentIndex] = angle;
    currentIndex = (currentIndex + 1) % numSamples;
    delay(sampleInterval);
  }
  
  recording = false;
  evaluateSamples();
}

void evaluateSamples() {
  int sortedSamples[numSamples];
  memcpy(sortedSamples, samples, numSamples * sizeof(int));
  qsort(sortedSamples, numSamples, sizeof(int), compare);
  
  Serial.println("[\" " + String(sortedSamples[numSamples - 5]) + "\",\" " + String(sortedSamples[numSamples - 4]) + "\",\" " + String(sortedSamples[numSamples - 3]) + "\",\" " + String(sortedSamples[numSamples - 2]) + "\",\" " + String(sortedSamples[numSamples - 1]) + "\"]");
}

int compare(const void* a, const void* b) {
  return (*(int*)a - *(int*)b);
}