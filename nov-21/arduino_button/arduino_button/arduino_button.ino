const int BUTTON_PIN  = 8;
const int LED_PIN     = 9;

int buttonState = LOW;
int prevButtonState;
int ledState = LOW;

// previous toggle time
unsigned long time = 0;
// buffer period to ignore circuit noise
unsigned long debounce = 200UL;

void setup() {
  Serial.begin(9600);

  pinMode(BUTTON_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);

  buttonState = digitalRead(BUTTON_PIN);
}

void loop() {
  // put your main code here, to run repeatedly:
  prevButtonState = buttonState;
  buttonState = digitalRead(BUTTON_PIN);
  // Serial.println(buttonState);

  // input going from LOW to HIGH
  // & enough time has passed to discount circuit noise
  // means button has been pressed
  if ((buttonState == HIGH) && (prevButtonState == LOW) && ((millis() - time) > debounce)) {
    Serial.println("Button pressed.");
    Serial.println(ledState);
    if (ledState == LOW)
      ledState = HIGH;
    else
      ledState = LOW;
  
    time = millis();
  }
  
  digitalWrite(LED_PIN, ledState);
}
