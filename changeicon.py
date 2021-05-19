import sys
import os


#ライブラリがインストールされているかチェックする
try:
    import requests
except:
    print("requestsライブラリがインストールされていません。\npip install requestsでインストールしてください。")
    a = input()
    sys.exit()

try:
    import tweepy
except:
    print("tweepyライブラリがインストールされていません。pip install tweepyでインストールしてください。")
    b = input()
    sys.exit()

CK="" #twitterのapiキー
CS="" #twitterのapi secretキー
AT="" #twitterのaccess tokenキー
AS="" #twitterのaccess token secretキー

#Twitterと接続。
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)

#自分の情報を取得する。
me = api.me()


def downloadimage(path = "./",name = "image",extention = ".png",url = "https://www.python.org/static/img/python-logo.png"):
    
    #画像をurlから保存する関数
    #pathの例: ./icon/image/ 最後のスラッシュを入れ忘れないように。
    #nameの例: icon iconという名前として保存する。それだけ。
    #urlの例: googleのアイコンだったら=>"https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
    file_name = path + name + extention
    response = requests.get(url)
    image = response.content
    with open(file_name, "wb") as f:
        f.write(image)
        print("ファイルをダウンロードしました。")

def gettwittericon(iconurl):

    #twieepyを使用して、ユーザーのスクリーンネームからアイコンのURLを取得する関数
    status=api.user_timeline(id=iconurl)[0]
    url = status.user.profile_image_url_https
    url2 = url.replace('normal','400x400')
    return url2

def main():
    #自分の画像のURLを取得する処理。
    twname = input('ユーザーID:')
    filename = input('ファイル名:')
    extention = input('拡張子:')

    if filename == '':
        filename = 'default'
    
    if extention == '':
        extention = 'png'

    iconurl = gettwittericon(twname)

    filepath = "./icon"

    if (os.path.isdir(filepath) == True):
        try:
            downloadimage("./icon/",filename,f".{extention}",iconurl)
            print(gettwittericon(twname))
        except:
            print("ユーザーが見つかりませんでした。")
    else:
        print(f"{filepath}が存在しません。ファイルを作成してください。")

if __name__ == "__main__":
    main()