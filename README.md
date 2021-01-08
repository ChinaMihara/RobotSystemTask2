# ロボットシステム学　課題２

---

### 課題内容

第10回で作成したROSのパッケージを改造し、オリジナルのものをGitHubに置く。   
また、ROSでハードウェアを動かしている様子を撮影しYouTubeに公開する。

---

### 説明   

色の異なるLED５つが特定の文字を入力すると点灯します。   
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

・ Raspberry Pi 4 Model B/4GB   
・ ブレットボード   
・ LED(赤、黄、緑、青、白)   
・ 抵抗 220Ω  ×5   
・ ジャンパー線　 ×10   
   
 以下をインストール   
・ ubuntu 20.04   
・ ROS-noetic   

---

### 実行手順

ワークスペースの準備
```
$ mkdir -p catkin/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace
```

ダウンロードとセットアップ
```
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
```
r:Red  y:Yellow  g:Green  b:Blue  w:White  E:Erase >>  
```
|入力文字||
|:---:|:---:|
|r|LED(赤)点灯|
|y|LED(黄)点灯|
|g|LED(緑)点灯|
|b|LED(青)点灯|
|w|LED(白)点灯|
|E|全LED消灯|

---

### 動画

[https://youtu.be/BJHqrDtc9TY](https://youtu.be/BJHqrDtc9TY)
