import requests


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # LINE Notify 權杖
    token = 'Line_Token'

    # 要發送的訊息
    message = 'Chat'

    # HTTP 標頭參數與資料
    headers = {"Authorization": "Bearer " + token}
    data = {'message': message}

    # 以 requests 發送 POST 請求
    requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)
