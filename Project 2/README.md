## Project 2

### Setup Hardware

Hardware
-   NodeMCU ESP8266
-   Sensor DHT22
-   Kabel Jumper
-   Breadboard
-   Raspberry Pi
-   Led

Konfigurasi Hardware
-   DHT22 Pin **OUT** - ESP8266 Pin **D1** (GPIO5)
-   DHT22 pin **(+)** - ESP8266 pin **3V**
-   DHT22 pin **(-)** - ESP8266 pin **GND**
-   Led pin **(-)** - Rasberry Pi pin **GND**
-   Led pin **(+)** - Raspberry Pi pin **12**

### Setup MQTT Broker

Kode untuk NodeMCU & Sensor DHT22 dapat dilihat pada [file berikut](/Project%202/code/mqtt.ino)

Kode untuk Raspberry Pi mqtt Publisher dapat dilihat pada [file berikut](/Project%202/code/mqtt_pub.py)

Kode untuk Raspberry Pi mqtt Subscriber dapat dilihat pada [file berikut](/Project%202/code/mqtt_sub.py)

Kode untuk menampilkan output suhu dari sensor DHT 22 dan melakukan on/off LED melalui website dapat dilihat pada [file berikut](/Project%202/code/index.html)

### Dokumentasi

Berikut adalah dokumentasi selama pengerjaan proyek ini

![1](/Project%202/dokumentasi/1.png)

![2](/Project%202/dokumentasi/2.png)

![3](/Project%202/dokumentasi/3.png)

### Video Penjelasan

Video penjelasan terkait dengan proyek ini dapat dilihat pada [link berikut](https://youtu.be/oH-x2QYfXsM?si=RSHeB1j34df-oyhb)