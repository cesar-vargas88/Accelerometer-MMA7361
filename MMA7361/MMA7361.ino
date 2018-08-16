// Proyecto 102 - Muestreo de aceleración en los ejes X, Y y Z usando el acelerometro MMA7361
// 02-05-2017
// Talos Electronics
// www.taloselectronics.com
// proyectos@taloselectronics.com
// Rafael Lozano, César Vargas

#include <math.h>
#include <AcceleroMMA7361.h>

AcceleroMMA7361 acelerometro;

void setup() 
{
  Serial.begin(115200);                           // Velocidad de la comunicación serial
  analogReference(EXTERNAL);                      // Indica que el ADC va a usar un voltaje externo commo referencia, usaremos 3.3 V

  acelerometro.begin(13, 12, 11, 10, A0, A1, A2); // Inicialización del acelerometro
  acelerometro.setARefVoltage(3.3);               // Establece el voltaje de referencia del acelerometro VAREF a 3.3V
  acelerometro.setSensitivity(HIGH);              // Establece la sensibilidad del acelerometro en +/-1.5G
  //acelerometro.calibrate();                     // Calibra el acelerometro    
}

void loop() 
{
    Serial.print(acelerometro.getXRaw());
    Serial.print(",");
    Serial.print(acelerometro.getYRaw());
    Serial.print(",");
    Serial.println(acelerometro.getZRaw());

    delay(10);  
}

