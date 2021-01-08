# ロボットシステム学　課題２

---

### 課題内容

第10回で作成したROSのパッケージを改造し、オリジナルのものをGitHubに置く。   
また、ROSでハードウェアを動かしている様子を撮影しYouTubeに公開する。

---

### 説明   

色の異なるLED５つを特定のコマンドを入力すると点灯します。   
各LEDとGPIOの接続は以下の通りです。   
|LED|GPIO|
|:---:|---|
|赤|GPIO4|
|黄|GPIO18|
|緑|GPIO25|
|青|GPIO12|
|白|GPIO26|

---

### 使用した物

・Raspberry Pi 4 Model B/4GB   
・ブレットボード   
・LED(赤、黄、緑、青、白)   
・抵抗 220Ω ×5   
・ジャンパー線　×10  

・ROS   


---

### 実行手順

```
$ cd ~/catkin_ws/src
$ git clone https://github.com/ChinaMihara/RobotSystemTask2.git
$ cd RobotSystemTask2/myled
$ make
$ chmod +x myled.c
$ sudo insmod myled.ko
$ sudo chmod 666 /dev/myled0
$ cd ..
$ cd scripts
$ chmod +x led_sub.py
$ chmod +x led_pub.py
```
ターミナルを３つ用意し以下のコマンドをそれぞれ入力する。   
１．
```
$ roscore
```
２．
```
$ rosrun RobotSystemTask2 led_sub.py
```
３．
```
$ rosrun RobotSystemTask2 led_pub.py
```

---

### 動画

[https://youtu.be/BJHqrDtc9TY](https://youtu.be/BJHqrDtc9TY)

---
### ライセンス

