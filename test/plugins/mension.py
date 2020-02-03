import os
from slackbot.bot import respond_to

import requests


@respond_to('助けて')
def help_command(message):
    message.reply("""助けるよ⭐️
    検索 - @mr_search メシ [フリーワード(単語ごとにカンマ区切り)]
    """)


@respond_to('メシ')
def search_command(message):
    # search_wordは、'メシ'も含まれているので、スペースでsplit
    search_word = message.body['text'].split()[1]

    # ぐるなびAPIを呼ぶ
    # レストラン検索APIのURL
    url = "https://api.gnavi.co.jp/RestSearchAPI/v3/"

    # パラメータの設定
    params = {"keyid": os.environ["GURUNAVI_API_TOKEN"], "freeword": search_word, "hit_per_page": 5}

    # リクエスト結果
    result_api = requests.get(url, params).json()

    # responseを整形してreply
    rest_list = result_api['rest']
    if len(rest_list) == 0:
        message.send("お店が見つかりませんでした・・・・")

    for rest in rest_list:
        message.send(rest['url'])
