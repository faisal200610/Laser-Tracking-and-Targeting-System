#include <Servo.h>

Servo clickServo;   // Pin 11
Servo pan;          // Pin 9
Servo tilt;         // Pin 10

int laserPin = 7;

void setup() {

  Serial.begin(115200);

  clickServo.attach(11);
  pan.attach(9);
  tilt.attach(10);

  clickServo.write(75);

  pan.write(90);
  tilt.write(90);

  pinMode(laserPin, OUTPUT);
  digitalWrite(laserPin, HIGH);
}

void loop() {

  if (Serial.available()) {

    String data = Serial.readStringUntil('\n');

    // Tracking command: "x,y"
    if (data.indexOf(',') > 0) {

      int comma = data.indexOf(',');

      int x = data.substring(0, comma).toInt();
      int y = data.substring(comma + 1).toInt();

      x = constrain(x, 10, 170);
      y = constrain(y, 20, 160);

      pan.write(x);
      tilt.write(y);
    }

    // Click servo command: "0" or "75"
    else {

      int angle = data.toInt();

      if (angle == 0 || angle == 75) {

        clickServo.write(angle);

        Serial.print("Click Servo -> ");
        Serial.println(angle);
      }
    }
  }
}
