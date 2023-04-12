import pyfirmata
import time


const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String message = Serial.readStringUntil('\n');
    message.trim();
    
    if (message == "BlinkLED") {
      for (int i = 0; i < 4; i++) {
        digitalWrite(ledPin, HIGH);
        delay(500);
        digitalWrite(ledPin, LOW);
        delay(500);
      }
    }
    else if (message == "TurnOffLED") {
      digitalWrite(ledPin, LOW);
    }
  }
}


board = pyfirmata.Arduino('/dev/ttyACM0')


led_pins = [2, 3, 4, 5]


for led in led_pins:

    board.digital[led].mode = pyfirmata.OUTPUT

   
    for i in range(4):
        board.digital[led].write(1)
        time.sleep(0.5)
        board.digital[led].write(0)
        time.sleep(0.5)


board.exit()
