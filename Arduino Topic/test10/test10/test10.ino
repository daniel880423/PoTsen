/*
  http://arduino.local/sd/SmokeSensor
  http://arduino.local:8080/?action=stream
  mjpg_streamer -i "input_uvc.so -f 60 -d /dev/video0" -o "output_http.so"
  Gmail SMTP:chzhbzrimelofsbl (465/587)
 */

#include <Process.h> 
#include <Console.h>
#include <Bridge.h>
#include <BridgeServer.h>
#include <BridgeClient.h>

Process process;                                   //process類別執行指令
Process webcam;
boolean hasPictured = false;                       //布爾值 是否有照片
boolean smokeTriggered = false;                    //是否有煙霧觸發
boolean mute = false;                              //是否有靜音
boolean msgSent = false;                           //是否有發送訊息
boolean noFlash =false;                            //是否有亮燈
boolean noFan =false;                              //是否有風扇轉動
//int pictureTimer = 5000;                           //5秒拍一次照
String path = "/mnt/sda1/";                        //字串路徑
int buzzerPin = 3;                                 //蜂鳴器連接角
int smoke = analogRead(A0);                        //煙霧感測器     
int i = 200;                                       //蜂鳴器底聲
int Step = 12;                                     //蜂鳴器遞減
int led = 9;                                       //LED燈連接在9號引腳
int light = 0;                                     //LED亮度
int lightBuild = 5;                                //亮度漸變值
int fanPin = 2;                                    //風扇位置
//int webcamInitialCount = 0;

//--------------------------------------------------------------------------------------------------------// 

BridgeServer server;
String startString;


void setup() {

  pinMode(buzzerPin,OUTPUT);                         //設定蜂鳴器為開
  pinMode(led,OUTPUT);
  pinMode(fanPin,OUTPUT);                            //風扇
  digitalWrite(fanPin,HIGH);                         //設定繼電器的初始狀態

  Bridge.begin();                                    //啟動Bridge，阻斷式呼叫
  Console.begin();

  server.listenOnLocalhost();
  server.begin();


  Process startTime;                                 //Linex時間
  startTime.runShellCommand("date");
  while (startTime.available()) {
    char c = startTime.read();
    startString += c;
    
  }

  /*
  //WebcamServer();
  Process webcam;
  while (!webcam.running()){
    webcam.runShellCommandAsynchronously("mjpg_streamer -i \"input_uvc.so -d /dev/video0\" -o \"output_http.so\"");
  }
  */
  
}

void loop() {

  smoke = analogRead(A0);
  //Console.println(smoke);
  
  if ( smoke > 260 ){                              //當煙霧達到500則響起

        if (!hasPictured) {                        //拍一張照片,儲存到SD卡
          //delay(pictureTimer);           
          //String fileName = takePicture();               
          hasPictured = true;
        }
         
        if ( msgSent == false ){                   //Line推播
          sendLineMessage("偵測到煙霧,請注意!http://172.20.10.4/sd/SmokeSensor/ &");
          msgSent = true;
        }
        
//---------------------------------------------------------------------------// 
        if (noFan == false){
          digitalWrite(fanPin,LOW);                  //風扇打開 (低電位處發)     
        }else{
          digitalWrite(fanPin,HIGH);
        }
//---------------------------------------------------------------------------// 
        if (mute == false){                        //Buzzer
          tone(buzzerPin,i);                       //在四號埠輸出頻率
        }else{
          noTone(buzzerPin);
        }
        i = i + Step;                              //警報器
        if (i >= 800) {
          Step = -12;
        } 
        else if (i <= 200) {
          Step = 12;
        }
        
//---------------------------------------------------------------------------// 
        if (noFlash == false){
        analogWrite(led,light);                      //呼吸燈
        light = light + lightBuild;
        if ( light == 0 || lightBuild == 255 ){
          lightBuild = -lightBuild;
        }
        //Console.print("i = ");
        //Console.println(i);
        //delay(30);                                 //該頻率維持5毫秒
        }else{
          analogWrite(led,0);
        }
  }
  
//---------------------------------------------------------------------------//  

  else if ( smoke < 250 ){

     msgSent = false;                              //Line推播初始化

     digitalWrite(fanPin,HIGH);                    //風扇關閉

     noFan = false;
      
     noTone(buzzerPin);                            //蜂鳴器關閉
     
     i = 200;
     
     mute = false;                                 //重置mute
     
     analogWrite(led,0);                           //關燈

     noFlash = false;

     hasPictured = false;                          //初始化照片
  }
  
//---------------------------------------------------------------------------// 

  BridgeClient client = server.accept();

  if (client) {
    String command = client.readString();
    command.trim();                                //kill whitespace
    Console.println(command);

    if (command == "smoke") {
      client.println(smoke);
    }else if(command == "mute"){
      mute = true;  
    }else if(command == "unmute"){
      mute = false;   
    }else if(command == "stopflash"){
      noFlash = true;
    }else if(command == "onflash"){
      noFlash = false;
    }else if (command == "stopfan"){
      noFan = true;
    }else if (command == "onfan"){
      noFan = false;
    }
    
    client.stop();                                 //重置client
  }
  
  delay(50);                                       // 循環時間
}

void sendLineMessage(String msg) {                                             //LINE訊息
  process.runShellCommandAsynchronously("python " + path + "line.py " + msg);
  //while (process.running());                                                 //造成卡頓5s
}

  
