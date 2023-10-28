#include<Servo.h>
Servo servo_on; // Servo için Tanımlamalar
Servo servo_arka;
Servo servo_el;
Servo servo_alt;
int IRSensor = 2; // connect ir sensor to arduino pin 2
int statusSensor;
int motor=3;
int x;
void setup() { //Giriş ayarları olarak servolar aktif hale geldi attach komudu ile
  servo_arka.attach(5);
  servo_on.attach(10);
  servo_el.attach(9);
  servo_alt.attach(6);
  pinMode (IRSensor, INPUT); // sensor pin INPUT //Sensörün giriş olduğu karar verildi.
  pinMode (motor, OUTPUT); // sensor pin output  //Motorun sürücüye çıkan out olduğu karar verildi
  bekleme(); // bekleme fonksiyonunda gidilir
 Serial.begin(115200); // Serial haberleşme yapıldı
 Serial.setTimeout(1); //serial haberleşme beklemesi
}
/*
 bandan alma için 
 on:85
 arka:160
 alt:90
 el:0
 bekleme için
 on:45
 arka:180
 el:120
 alt:90
 sağ ön için
 el:0
 alt:45
 on:
 arka:

*/
void loop(){


analogWrite(motor,180); //Motor Çalıştırıldı
bekleme(); // Bekleme konumuna geldi
delay(1000); 
while(digitalRead (IRSensor)); //Sesnörden bilgi gelinceye kadar döngü beklendi

delay(350);
analogWrite(motor,0); // Sensörden bilgi gelince motor durudurludu
delay(1000);
//motor durduruldu
Serial.print(1);
while (!Serial.available());
x = Serial.readString().toInt(); //Serial haberleşemeden gelen bilgiler alındı. 
 //Gideceği Yön Belirlendi x ile belirlendi
if(x==1)
{
  al();
  solon();
}
if(x==2)
{
  al();
  solarka();
}
if(x==3)
{
  al();
  sagon();
}
if(x==4)
{
  al();
  sagarka();
}



//
}
//Serial haberleşemeden gelen konuma göre robot kolun hareketleri aşagıdaki fonksiyonlardaki gibidir. Robot kol istenilen konuma göre hareket etmektedir. Servonun belirli açıda hareket etmesi gerekmektedir. Servo hareketini aşgıdaki fonksiyonalr ile yapılmaktadır.
void bekleme()
{
servo_el.write(120);
servo_on.write(45);
servo_arka.write(180);
servo_alt.write(90); 
}
void al()  // alma fonksiyonu
{
   for (int i = 45; i<=130; i++)
  { 
    servo_on.write(i); delay(5); //servo hareketi sağlanır 45 derece
  }
     for (int i = 180; i>=155; i--)
  { 
    servo_arka.write(i); delay(5); //servo hareketi sağlanır 180 derece
  }
  delay(500);
   for (int i = 120; i>=0; i--)
  { 
    servo_el.write(i); delay(5);  //servo hareketi sağlanır 120 derece
  }
   for (int i = 130; i>=90; i--)
  { 
    servo_on.write(i); delay(5); //servo hareketi sağlanır 130 derece
  }
     for (int i = 155; i<180; i++)
  { 
    servo_arka.write(i); delay(5);
  }
  delay(500);
  
  
}
void solon(){
for (int i = 90; i<135; i++)
  { 
    servo_alt.write(i); delay(5);
  }
for (int i = 85; i<160; i++)
  { 
    servo_on.write(i); delay(5);
  }
for (int i = 160; i>=110; i--)
  { 
    servo_arka.write(i); delay(5);
  }
  delay(500);
  servo_el.write(180);
delay(500);
    servo_el.write(40);
    
    
for (int i = 150; i>=45; i--)
  { 
    servo_on.write(i); delay(5);
  }
for (int i = 120; i<160; i++)
  { 
    servo_arka.write(i); delay(5);
  }
for (int i = 135; i>=90; i--)
  { 
    servo_alt.write(i); delay(5);
  }
    
    
  }

  
void solarka(){
  for (int i = 90; i<180; i++)
  { 
    servo_alt.write(i); delay(5);
  }
  for (int i = 85; i<160; i++)
  { 
    servo_on.write(i); delay(5);
  }
  for (int i = 160; i>=110; i--)
  { 
    servo_arka.write(i); delay(5);
  }
  delay(500);
  servo_el.write(180);
  delay(500);
      servo_el.write(40);
  for (int i = 150; i>=45; i--)
  { 
    servo_on.write(i); delay(5);
  }
  for (int i = 120; i<160; i++)
  { 
    servo_arka.write(i); delay(5);
  }
  for (int i = 180; i>=90; i--)
  { 
    servo_alt.write(i); delay(5);
  }


  }


  
void sagon(){
    for (int i = 90; i>=45; i--)
  { 
    servo_alt.write(i); delay(5);
  }
  for (int i = 85; i<160; i++)
  { 
    servo_on.write(i); delay(5);
  }
  for (int i = 160; i>=110; i--)
  { 
    servo_arka.write(i); delay(5);
  }
  delay(500);
  servo_el.write(180);
  
  delay(500);
  servo_el.write(40);
  for (int i = 150; i>=45; i--)
  { 
    servo_on.write(i); delay(5);
  }
  for (int i = 120; i<160; i++)
  { 
    servo_arka.write(i); delay(5);
  }
  for (int i = 45; i<=90; i++)
  { 
    servo_alt.write(i); delay(5);
  }
    

  }


  
void sagarka(){
      for (int i = 90; i>0; i--)
  { 
    servo_alt.write(i); delay(5);
  }
  for (int i = 85; i<160; i++)
  { 
    servo_on.write(i); delay(5);
  }
  for (int i = 160; i>=110; i--)
  { 
    servo_arka.write(i); delay(5);
  }
  delay(500);
  servo_el.write(180);
  delay(500);
  servo_el.write(40);
  for (int i = 150; i>=45; i--)
  { 
    servo_on.write(i); delay(5);
  }
  for (int i = 120; i<160; i++)
  { 
    servo_arka.write(i); delay(5);
  }
  for (int i = 0; i<=90; i++)
  { 
    servo_alt.write(i); delay(5);
  }
    

  }
