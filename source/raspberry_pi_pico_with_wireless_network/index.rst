.. meta::
   :description: raspberry pi pico with wireless network
   :keywords: raspberry_pi_pico, wireless_network, micropython


============================================================
PyCon JP 2024 発表資料
============================================================

MicroPythonとRaspberry Pi Pico Wで始めるワイヤレス通信
------------------------------------------------------------
中村草介(Sousuke NAKAMURA)

1.1. はじめに
--------------------
+ 15分の枠での発表です
+ 概要のあと、5分のLTが二つ続くイメージで用意しています

1.2. 自己紹介
----------------------
+ 中村草介
+ Raspberry Piもくもく会スタッフ
+ Raspberry Piもくもく会はポスターセッションでも出展しています

.. image:: ../_static/raspberry_pi_pico_with_wireless_network/75330.jpeg
   :width: 160px
   :align: right

1.2.1. 自己紹介(お仕事の紹介)
--------------------------------------------

+ ソフトウェアエンジニア絶賛募集中です

.. image:: https://urbanx-tech.com/wp-content/uploads/2022/08/cropped-Logo@3x.png
   :width: 172px
   :align: center

1.3. Raspberry Pi Picoとは
--------------------------------------------
+ RP2040というマイクロコントローラーを使ったボードです

  + Linuxが動作するRaspberry Piとは違います
  + RP2350というマイクロコントローラーを搭載したRaspberry Pi Pico 2が2024/8/8に発表されましたが、wifiなどは搭載されていないので今回は対象としていません

image:: ../_static/raspberry_pi_pico_with_wireless_network/raspberry_pi_pico_w.jpg
   :width: 200px
   :align: right

https://www.raspberrypi.com/products/raspberry-pi-pico/


1.4. MicroPythonとは
--------------------------------------------
+ Python3のサブセットで、マイクロコントローラー向けに最適化された言語です
+ 使い慣れたPythonとライブラリを使うことでArduinoなどに比べて簡単に開発できます
+ ※標準ライブラリ全ては含まれていないほか、サブセットとしていくつかの機能が省かれています

https://micropython.org


1.4.1. ライブラリ一覧
--------------------------------------------

.. code-block:: python

   >>> help('modules')
   __main__          asyncio/__init__  hashlib           rp2
   _asyncio          asyncio/core      heapq             select
   _boot             asyncio/event     io                socket
   _boot_fat         asyncio/funcs     json              ssl
   _onewire          asyncio/lock      lwip              struct
   _rp2              asyncio/stream    machine           sys
   _thread           binascii          math              time
   _webrepl          bluetooth         micropython       tls
   aioble/__init__   builtins          mip/__init__      uasyncio
   aioble/central    cmath             neopixel          uctypes
   aioble/client     collections       network           urequests
   aioble/core       cryptolib         ntptime           vfs
   aioble/device     deflate           onewire           webrepl
   aioble/l2cap      dht               os                webrepl_setup
   aioble/peripheral ds18x20           platform          websocket
   aioble/security   errno             random
   aioble/server     framebuf          re
   array             gc                requests/__init__
   Plus any modules on the filesystem

1.4.1 ArduinoでのLチカ(LED点滅)
--------------------------------------------
+ Arduinoのチュートリアルにあるサンプルコード

.. code-block:: arduino

   void setup() {
      pinMode(LED_BUILTIN, OUTPUT);
   }

   void loop() {
      digitalWrite(LED_BUILTIN, HIGH);
      delay(1000);
      digitalWrite(LED_BUILTIN, LOW);
      delay(1000);
   }

https://docs.arduino.cc/tutorials/uno-rev3/Blink/

1.4.2 MicroPythonでのLチカ
--------------------------------------------
+ Arduinoのサンプルコードと同じような流れでLEDを点滅させることができます

.. code-block:: python

   import machine
   import time

   led = machine.Pin('LED', machine.Pin.OUT)

   while True:
       led.value(1)
       time.sleep(1)
       led.value(0)
       time.sleep(1)

1.4.3 MicroPythonでのLチカ
--------------------------------------------
+ Timerオブジェクトのコールバックにlambdaを使ってシンプルに

.. code-block:: python

   import machine
   led = machine.Pin('LED', machine.Pin.OUT)
   timer = machine.Timer()
   timer.init(freq=2.5, mode=machine.Timer.PERIODIC, callback=lambda _: led.toggle())


1.5. MicroPythonのインストール
--------------------------------------------

1.6. 開発環境の準備
--------------------------------------------


1.6.1. 開発環境の準備
--------------------------------------------
+ RaspberryPiの公式ドキュメントではthonnyがお勧めされています
+ VS Codeでもプラグインをインストールすることで開発できます

.. image:: ../_static/raspberry_pi_pico_with_wireless_network/thonny.png
   :width: 400px
   :align: center

+ https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico
+ https://thonny.org


1.6.2. Replへの接続
--------------------------------------------


2.1. wifiの設定
--------------------------------------------

HTTPリクエストを送信する
--------------------------------------------

+ requestsライブラリが利用可能
.. code-block:: python

   import urequests as requests
   import time

   # setup wifi

   while True:
      if codey.wifi.is_connected():
         codey.led.show(0,0,255)
         res = requests.get(url='https://api.open-meteo.com/v1/forecast?latitude=35.6322596&longitude=139.7885507&hourly=temperature_2m&timezone=Asia%2FTokyo&forecast_days=1&models=jma_seamless')
         print(res.text)
         break
      else:
         time.sleep(3)


HTTPサーバーを立てたい
--------------------------------------------
.. code:: 

  添付されている標準モジュールの一覧
  Positional-only Parameters
  array
  builtins
  json
  os
  random
  struct
  sys

+ httpモジュールがないのでhttp.serverモジュールもない
+ urllibモジュールもないのでurllib.parseなど便利なモジュールが使えない
+ https://docs.micropython.org/en/latest/genrst/index.html

簡易的なHTTPサーバーを実装する
--------------------------------------------


bluetooth
--------------------------------------------




https://github.com/Heerkog/MicroPythonBLEHID



wifiからのhttpリクエストでBluetoothを操作する




