# -*- coding: utf-8 -*-
import urllib.request
import json



# 天気クラス
class Weather:
    def __init__(self, data):

        # 日付
        self.date = data["date"]

        # テロップ
        self.telop = data["telop"]

        # 最高気温
        if data["temperature"]["max"] is not None:
            self.temperature_max = "{0}℃".format(data["temperature"]["max"]["celsius"])
        else:
            self.temperature_max = "--℃"

        # 最低気温
        if data["temperature"]["min"] is not None:
            self.temperature_min = "{0}℃".format(data["temperature"]["min"]["celsius"])
        else:
            self.temperature_min = "--℃"

    def print(self):
        print(self.date)
        print("  " + self.telop)
        print("  最高：{0}".format(self.temperature_max) + "\n" +"  最低：{0}".format(self.temperature_min) + "\n")

        file.write(self.date +  "\n")
        file.write("  " + self.telop +  "\n")
        file.write("  最高：{0}".format(self.temperature_max) + "\n" + "  最低：{0}".format(self.temperature_min) + "\n")


# Weather Hacks URL
URL = "http://weather.livedoor.com/forecast/webservice/json/v1?city={0}"

# 町コード：横浜市
ID = 140010

i=0

# リクエスト実行
req = urllib.request.Request(URL.format(ID))
with urllib.request.urlopen(req) as res:
    # レスポンス結果
    data = json.load(res)


    # 天気結果の取得
    weathers = []
    for forecast in data["forecasts"]:
        weathers.append(Weather(forecast))

    # 天気結果の出力
    for item in weathers:
        i+=1

        file_name='tenki_info' + str(i) + '.txt'
        print(file_name)
        file = open(file_name, 'w')
#        print(data["title"])
#        file.write(data["title"] + "\n")
        item.print()
