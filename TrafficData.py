from urllib import request
import io
import time
import datetime


def catch():
    url = 'http://restapi.amap.com/v3/traffic/status/circle?location=113.362691,' \
          '23.101022&level=6&extensions=all&output=JSON&radius=4999&key=14d652f05060b10a7ca3a36cfa4e4c3b '
    data = request.urlopen(url).read().decode("utf-8")
    now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    file_name = str(now)
    print(file_name)
    try:
        f = open('SourceData/'+file_name, 'w')
        f.write(str(data))
    finally:
        if f:
            f.close()


def weather_hz():
    url = 'http://restapi.amap.com/v3/weather/weatherInfo?city=440105&output=JSON&key=14d652f05060b10a7ca3a36cfa4e4c3b'
    data = request.urlopen(url).read().decode("utf-8")
    now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    file_name = 'w_hz' + str(now)
    print(file_name)
    try:
        f = open('SourceWeatherData/'+file_name, 'w')
        f.write(str(data))
    finally:
        if f:
            f.close()


def weather_th():
    url = 'http://restapi.amap.com/v3/weather/weatherInfo?city=440106&output=JSON&key=14d652f05060b10a7ca3a36cfa4e4c3b'
    data = request.urlopen(url).read().decode("utf-8")
    now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    file_name = 'w_th' + str(now)
    print(file_name)
    try:
        f = open('SourceWeatherData/'+file_name, 'w')
        f.write(str(data))
    finally:
        if f:
            f.close()


def weather_py():
    url = 'http://restapi.amap.com/v3/weather/weatherInfo?city=440113&output=JSON&key=14d652f05060b10a7ca3a36cfa4e4c3b'
    data = request.urlopen(url).read().decode("utf-8")
    now = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

    file_name = 'w_py' + str(now)
    print(file_name)
    try:
        f = open('SourceWeatherData/'+file_name, 'w')
        f.write(str(data))
    finally:
        if f:
            f.close()


flag = 0
while True:
    if datetime.datetime.now().hour == 4 and datetime.datetime.now().day == 16 and flag == 0:
        weather_hz()
        weather_th()
        weather_py()
        catch()
        flag = 1
    elif datetime.datetime.now().hour >= 6:
        if not (not (7 <= datetime.datetime.now().hour <= 10) and not (
                16 <= datetime.datetime.now().hour <= 20)):
            now_iteration = datetime.datetime.now()
            if now_iteration.minute % 60 == 0:
                weather_hz()
                weather_th()
                weather_py()
            if now_iteration.minute % 5 == 0:
                catch()
                time.sleep(300)
        else:
            now_iteration = datetime.datetime.now()
            catch()
            time.sleep(900)