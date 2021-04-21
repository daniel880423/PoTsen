#include <Bridge.h>
#include <Process.h>
#include <Console.h>
Process process;                          //process類別執行指令
boolean hasPictured = false;              //布爾值 是否有照片
int MILIS_TO_WAIT_DOOR_OPEN = 5000;       //到達時門打開
int switchPin = 2;                        //開關
String path = "/mnt/sda1/";               //字串路徑

int buzzerPin = 3;                        //蜂鳴器連接角
int smoke = analogRead(A0);

void setup() {                            //程式指令宣告
pinMode(switchPin, INPUT);                //設定腳位 開/關

pinMode(buzzerPin,OUTPUT);                //設定蜂鳴器為開

Bridge.begin();                           //啟動Bridge，阻斷式呼叫
Console.begin();

Console.println("Hello");

}

void loop() {                             //程式主內容,重複
if (digitalRead(switchPin) == LOW) {
  if (!hasPictured) {
  
    delay(MILIS_TO_WAIT_DOOR_OPEN);           
    String fileName = takePicture();          //當棉打開照一張像
    hasPictured = true;
    //uploadPicture(fileName);
    //logToGoogleDrive(fileName);               //登錄到google雲端
  }
} else {
    hasPictured = false;
}

  smoke = analogRead(A0);
  Console.println(smoke);
  if ( smoke > 400 ){                      //當煙霧達到500則響起
     for( int i=200;i<=800;i++ ){          //用循環的方式將頻率從200HZ 增加到800HZ
        tone(buzzerPin,i);                         //在四號埠輸出頻率
        delay(5);                          //該頻率維持5毫秒
     }
     delay(3000);                          //最高頻率下維持4秒鐘
     for( int i=800;i>=200;i--){
        tone(buzzerPin,i);
        delay(5);
     }
  }else{
     noTone(buzzerPin);
  }
 

}
   
String takePicture() {                                                 //照相
String filename = getCurrentTimeString() + ".jpg";                     //儲存Jpg檔
String filePathName = path + filename;                                 //路徑名稱
process.runShellCommand("fswebcam " + filePathName + " -r 800×600");   //runShellCommand屬於阻斷式呼叫，
while (process.running());                                             //等到該方法回傳時，指令已執行完畢
hasPictured = true;             //當process執行,拍一張照                                       
return filePathName;            //返回
}

void uploadPicture(String filePathName) {                              //上傳照片
process.runShellCommand("python " + path + "upload.py " + filePathName);
while (process.running());
}

String getCurrentTimeString() {
String currentTimeStr;
process.runShellCommand("date +%Y-%m-%d-%H-%M-%S");
while (process.running());

while (process.available() > 0) {
char c = process.read();
currentTimeStr += c;
}
currentTimeStr.trim();
return currentTimeStr;
}

void logToGoogleDrive(String filePathName) {
}
