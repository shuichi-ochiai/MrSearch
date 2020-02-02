import os
from slackbot.bot import respond_to  # @botname: で反応するデコーダ
from slackbot.bot import listen_to  # チャネル内発言で反応するデコーダ
from slackbot.bot import default_reply  # 該当する応答がない場合に反応するデコーダ

import requests
import pprint
import json


# @respond_to('string')     bot宛のメッセージ
#                           stringは正規表現が可能 「r'string'」
# @listen_to('string')      チャンネル内のbot宛以外の投稿
#                           @botname: では反応しないことに注意
#                           他の人へのメンションでは反応する
#                           正規表現可能
# @default_reply()          DEFAULT_REPLY と同じ働き
#                           正規表現を指定すると、他のデコーダにヒットせず、
#                           正規表現にマッチするときに反応
#                           ・・・なのだが、正規表現を指定するとエラーになる？

# message.reply('string')   @発言者名: string でメッセージを送信
# message.send('string')    string を送信
# message.react('icon_emoji')  発言者のメッセージにリアクション(スタンプ)する
#                               文字列中に':'はいらない
@respond_to('メンション')
def mention_func(message):
    message.reply('私にメンションと言ってどうするのだ')  # メンション


@listen_to('リッスン')
def listen_func(message):
    message.send('誰かがリッスンと投稿したようだ')  # ただの投稿
    message.reply('君だね？')  # メンション


@listen_to('ぐるなび')
def gurunavi_func(message):
    # レストラン検索APIのURL
    url = "https://api.gnavi.co.jp/RestSearchAPI/v3/"

    # パラメータの設定
    params = {}
    params["keyid"] = os.environ["GURUNAVI_API_TOKEN"]  # 取得したアクセスキー
    params["freeword"] = "新橋,ランチ,10000"

    # リクエスト結果
    result_api = requests.get(url, params)
    result_api = result_api.json()  # 読まなきゃいけない！じゃないと<Response [200]>とでるだけ。
    # print(result_api) # 整形せずにそのまま表示
    # pprint.pprint(result_api) # 整形して表示

    message.send(result_api['rest'][0]['address'])
    # 無事に住所が表示されました
    message.send(result_api['rest'][0]['name'])
    # カナも表示されました
    message.send(result_api['rest'][0]['code']['areaname'])
    # 関東
    # message.send(result_api['rest'][0]['code']['category_name_l'][:2])
    # ['すし・魚料理・シーフード', '日本料理・郷土料理']リストは2個しかないから、全部出るんだけどね。
    budget = result_api['rest'][0]['budget']
    message.send(str(budget))

