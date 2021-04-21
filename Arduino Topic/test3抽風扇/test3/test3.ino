#include <Bridge.h>
#include <Process.h>

Process process;                          //process類別執行指令
boolean hasPictured = false;              //布爾值 是否有照片
int MILIS_TO_WAIT_DOOR_OPEN = 5000;       //到達時門打開
int switchPin = 2;                        //開關
String path = "/mnt/sda1/";               //字串路徑

//*int fanPin = 3;                           //風扇位置
//*int relayPin = 4;                         //繼電器位置
//*int relayState = HIGH;                    //繼電器初始狀態為HIGH


void setup() {                            //程式指令宣告
pinMode(switchPin, INPUT);                //設定腳位 開/關

//*pinMode(fanPin,INPUT);
//*pinMode(relayPin,OUTPUT);
//*digitalWrite(relayPin,relayState);        //設定繼電器的初始狀態

Bridge.begin();                           //啟動Bridge，阻斷式呼叫
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
