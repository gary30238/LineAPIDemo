import requests


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # LINE Notify 權杖
    token = '2wyNxGpvhPZUSV2Xv5gsyx3hg6r7nrCLZ4gVEEJOsQN'

    # 要發送的訊息
    message = 'Chat'

    # HTTP 標頭參數與資料
    headers = {"Authorization": "Bearer " + token}
    data = {'message': message}

    # 以 requests 發送 POST 請求
    requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)
