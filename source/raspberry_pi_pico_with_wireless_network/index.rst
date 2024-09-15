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

1.4.1 ArduinoでのLチカ
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

+ uf2ファイルをダウンロード https://micropython.org/download/RPI_PICO_W/
+ Rasppeberry Pi Pico WのBOOTSELボタンを押しながらUSBケーブルをコンピューターに接続
+ USBストレージとして認識されるので、MicroPythonのuf2ファイルをコピーします
+ コピーが終わると自動的に再起動(アンマウント)されます

1.5.1 mpremoteを使って動作確認
--------------------------------------------

+ MicroPythonのREPLが起動しているのでシリアルコンソールで接続することができます

.. code-block:: shell-session

  $ pip install mpremote
  $ mpremote connect list
  /dev/cu.usbmodem101 e661385283776133 2e8a:0005 MicroPython Board in FS mode
  $ mpremote connect /dev/cu.usbmodem101
  Connected to MicroPython at /dev/cu.usbmodem101
  Use Ctrl-] or Ctrl-x to exit this shell
  
  >>> import sys
  >>> sys.implementation
  (name='micropython', version=(1, 23, 0, ''), _machine='Raspberry Pi Pico W with RP2040', _mpy=4870)
  >>> 

1.6. 開発環境の準備
--------------------------------------------


1.6.1. 開発環境の準備
--------------------------------------------
+ RaspberryPiの公式ドキュメントではThonny (https://thonny.org) がお勧めされています

+ https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico


1.6.2. Thonnyについて
--------------------------------------------

+ ファイル(ローカル、デバイス)、エディター、REPL、デバッグ用のペインが揃っています

.. image:: ../_static/raspberry_pi_pico_with_wireless_network/thonny.png
   :width: 500px
   :align: center

2.1. wifiの設定
--------------------------------------------

+ wifi接続はnetworkモジュールを使います

.. code-block:: python

   import network
   import rp2
   import time

   rp2.country('JP')

   wlan = network.WLAN(network.STA_IF)
   wlan.active(True)
   wlan.connect('SSID', 'password')

   while not wlan.isconnected() and wlan.status() >= 0:
      print("Waiting to connect:")
      time.sleep(1)

   print(wlan.ifconfig())

HTTPリクエストを送信する
--------------------------------------------

+ requestsライブラリが利用可能

.. code-block:: python

   import json
   import network
   import rp2
   import time
   import urequests


   # 'https://api.open-meteo.com/v1/forecast?latitude=35.6322596&longitude=139.7885507&hourly=temperature_2m&timezone=Asia%2FTokyo&forecast_days=1&models=jma_seamless'
   WEATHER_API_URL = 'https://api.open-meteo.com/v1/forecast?latitude=35.680959106959&longitude=139.76730676352&current=temperature_2m,wind_speed_10m'

   rp2.country('JP')

   wlan = network.WLAN(network.STA_IF)
   wlan.active(True)

   wlan.connect('SSID', 'password')

   while not wlan.isconnected() and wlan.status() >= 0:
      print("Waiting to connect:")
      time.sleep(1)

   print(wlan.ifconfig())

   response = urequests.get(WEATHER_API_URL)
   response_body = json.loads(response.text)

   print(f"temperature_2m:{response_body['current']['temperature_2m']}")
   print(f"wind_speed_10m:{response_body['current']['wind_speed_10m']}")

   wlan.disconnect()


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

+ aioble
+ https://github.com/micropython/micropython-lib/tree/master/micropython/bluetooth/aioble


プロトコル
--------------------------------------------

+ GAP→デバイスの発見、接続、ペアリングなど
+ GATT→デバイス間のデータ、サービスの定義、のやり取り、GATTプロファイルを使ってデータのやりとりをおこなう


aiobleを使ってBLEデバイスをスキャンする
--------------------------------------------

.. code-block:: python

   import aioble
   import asyncio

   async def instance1_task():

      async with aioble.scan(duration_ms=5000) as scanner:
         async for result in scanner:
               print(result, result.name(), result.rssi, result.services())

   asyncio.run(instance1_task())

aiobleを使ってサービスを提供する
--------------------------------------------

.. code-block:: python

   import aioble
   import asyncio
   import bluetooth

   # https://www.bluetooth.com/specifications/assigned-numbers/
   _ENV_SENSE_UUID = bluetooth.UUID(0x181A) # Environmental Sensing Service 0x181A Environmental Sensing Service
   _ENV_SENSE_TEMP_UUID = bluetooth.UUID(0x2A6E) # Temperature characteristic 0x2A6E Temperature
   _GENERIC_THERMOMETER = const(0x0300) # Generic Thermometer appearance 0x00C 0x0300 to 0x033F Thermometer

   _ADV_INTERVAL_US = const(250000)

   temp_service = aioble.Service(_ENV_SENSE_UUID)
   temp_char = aioble.Characteristic(temp_service, _ENV_SENSE_TEMP_UUID, read=True, notify=True)

   aioble.register_services(temp_service)

   async def instance1_task():
      while True:
         async with await aioble.advertise(
                  _ADV_INTERVAL_US,
                  name="temperature sensor",
                  services=[_ENV_SENSE_UUID],
                  appearance=_GENERIC_THERMOMETER,
                  manufacturer=(0xabcd, b"1234"),
               ) as connection:
            print("Connection from", connection.device)
            await connection.disconnected(timeout_ms=None)
      
   asyncio.run(instance1_task())

確認する
--------------------------------------------

.. image:: ../_static/raspberry_pi_pico_with_wireless_network/lightblue_1-1.jpeg
   :width: 150px

.. image:: ../_static/raspberry_pi_pico_with_wireless_network/lightblue_1-2.jpeg
   :width: 150px

.. image:: ../_static/raspberry_pi_pico_with_wireless_network/lightblue_1-3.jpeg
   :width: 150px

+ LightBlueを使って確認する
+ https://punchthrough.com/lightblue/


aiobleを使ってCPUの温度をBLEで送信する
-------------------------------------------- 

+ ドキュメント
+ https://github.com/micropython/micropython-lib/blob/master/micropython/bluetooth/aioble/README.md


aiobleを使ってCPUの温度をBLEで送信する
-------------------------------------------- 

+ サンプルコード
+ https://github.com/micropython/micropython-lib/blob/master/micropython/bluetooth/aioble/examples/temp_sensor.py


https://github.com/Heerkog/MicroPythonBLEHID



wifiからのhttpリクエストでBluetoothを操作する




