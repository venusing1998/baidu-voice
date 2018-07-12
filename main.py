from aip import AipSpeech
import os

# AppID, API KEY, Secret Key
APP_ID = "11526272"
API_KEY = "cbge3NwOW09R7DFnTon9tfU9"
SECRET_KEY = "aajYaGP35P1wgY3AY4PEmePctblQdbkf"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(BASE_DIR, "dist")

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# text you input
text = "你好百度"
per = {
    "女声": 0,
    "男声": 1,
    "情感合成-度逍遥": 3,
    "情感合成-度丫丫": 4,
}
result = client.synthesis(text, "zh", 1, {
    "vol": 5, "per": per.get("女声")
})


# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    if not os.path.exists(DIST_DIR):
        os.makedirs(DIST_DIR)
    with open("dist/auido.mp3", "wb") as f:
        f.write(result)
