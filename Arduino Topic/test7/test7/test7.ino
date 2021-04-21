//--------------------------------------------------------------------------------------------------------//
#include <Bridge.h>
#include <Process.h>
#include <Console.h>
Process process;                                   //process類別執行指令
boolean hasPictured = false;                       //布爾值 是否有照片
boolean smokeTriggered = false;                    //是否有煙霧觸發
boolean msgSent = false;                           //是否有發送訊息
int pictureTimer = 5000;                           //5秒拍一次照
String path = "/mnt/sda1/";                        //字串路徑
int buzzerPin = 3;                                 //蜂鳴器連接角
int smoke = analogRead(A0);
int i = 200;
int Step = 12;
int led = 9;                                       //LED燈連接在9號引腳
int light = 0;                                     //LED亮度
int lightBuild = 5;                                //亮度漸變值
int fanPin = 2;                                    //風扇位置
int fanStatus = digitalRead(fanPin);

  
//--------------------------------------------------------------------------------------------------------// 

void setup() {                                     //程式指令宣告
  
//pinMode(switchPin, INPUT);                       //設定腳位 開/關
pinMode(buzzerPin,OUTPUT);                         //設定蜂鳴器為開
pinMode(led,OUTPUT);
pinMode(fanPin,OUTPUT);                            //風扇
digitalWrite(fanPin,HIGH);                         //設定繼電器的初始狀態

Bridge.begin();                                    //啟動Bridge，阻斷式呼叫
Console.begin();

//Console.println("Hello");

}

//--------------------------------------------------------------------------------------------------------//

void loop() {                                      //程式主內容,重複

  smoke = analogRead(A0);
  Console.println(smoke);
  fanStatus = digitalRead(fanPin);
  Console.print("風扇的狀態:");
  Console.println(fanStatus);
  
  if ( smoke > 250 ){                              //當煙霧達到500則響起

        if (!hasPictured) {                        //拍一張照片,儲存到SD卡
          delay(pictureTimer);           
          String fileName = takePicture();               
          hasPictured = true;
        }
         
        if ( msgSent == false ){                   //Line推播
          sendLineMessage("偵測到煙霧,請注意!!!");
          msgSent = true;
        }
        
//---------------------------------------------------------------------------// 
       
        digitalWrite(fanPin,LOW);                  //風扇打開      
        
//---------------------------------------------------------------------------// 
       
        tone(buzzerPin,i);                         //在四號埠輸出頻率
        i = i + Step;
        
        if (i >= 800) {
          Step = -12;
        } 
        else if (i <= 200) {
          Step = 12;
        }
        
//---------------------------------------------------------------------------// 
        
        analogWrite(led,light);
        light = light + lightBuild;
        if ( light == 0 || lightBuild == 255 ){
          lightBuild = -lightBuild;
        }
        Console.print("i = ");
        Console.println(i);
        delay(30);                                 //該頻率維持5毫秒
  }
  
  else if ( smoke < 200 ){

     msgSent = false;                              //推播初始化

     digitalWrite(fanPin,HIGH);                    //風扇關閉
      
     noTone(buzzerPin);                            //蜂鳴器關閉
     i = 200;
     
     analogWrite(led,0);                           //關燈

     hasPictured = false;                          //初始化照片
  }
 

}

//--------------------------------------------------------------------------------------------------------//  
  
String takePicture() {                                                       //照相
String filename = getCurrentTimeString() + ".jpg";                           //儲存Jpg檔
String filePathName = path + filename;                                       //路徑名稱
process.runShellCommand("fswebcam " + filePathName + " -r 800×600");         //runShellCommand屬於阻斷式呼叫，
while (process.running());                                                   //等到該方法回傳時，指令已執行完畢
hasPictured = true;                                                          //當process執行,拍一張照                                       
return filePathName;                                                         //返回
}

//---------------------------------------------------------------------------------------------------------// 

/*
void uploadPicture(String filePathName) {                                    //上傳照片
process.runShellCommand("python " + path + "upload.py " + filePathName);
while (process.running());
}
*/

//---------------------------------------------------------------------------------------------------------// 

void sendLineMessage(String msg) {                                           //LINE訊息
process.runShellCommandAsynchronously("python " + path + "line.py " + msg);
//while (process.running());                                                 //造成卡頓5s
}

//---------------------------------------------------------------------------------------------------------// 

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

//---------------------------------------------------------------------------------------------------------// 
