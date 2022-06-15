from aip import AipImageClassify

""" 你的 APPID AK SK """
APP_ID = '23521368'
API_KEY = 'ZsU4yX9sebQmW06s7xc3oaaG'
SECRET_KEY = '94OsjVY5GwbaD8QZRLqzRGQgWhwdWcTq'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('1.jpg')

""" 调用通用物体识别 """
print(client.advancedGeneral(image))
