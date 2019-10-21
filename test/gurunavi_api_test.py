import requests
import pprint
import json

#レストラン検索APIのURL
url = "https://api.gnavi.co.jp/RestSearchAPI/v3/"

#パラメータの設定
params={}
params["keyid"] = "***************" #取得したアクセスキー
params["freeword"] = "新橋,ランチ,10000"


if __name__ == "__main__":
    # リクエスト結果
    result_api = requests.get(url, params)
    result_api = result_api.json()  # 読まなきゃいけない！じゃないと<Response [200]>とでるだけ。
    # print(result_api) # 整形せずにそのまま表示
    # pprint.pprint(result_api) # 整形して表示

    print(result_api['rest'][0]['address'])
    # 無事に住所が表示されました
    print(result_api['rest'][0]['name'])
    # カナも表示されました
    print(result_api['rest'][0]['code']['areaname'])
    # 関東
    print(result_api['rest'][0]['code']['category_name_l'][:2])
    # ['すし・魚料理・シーフード', '日本料理・郷土料理']リストは2個しかないから、全部出るんだけどね。
    print(result_api['rest'][0]['budget'])
