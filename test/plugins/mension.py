from slackbot.bot import respond_to


@respond_to('助けて')
def help_command(message):
    message.reply("""助けるよ⭐️
    検索 - @mr_search メシ [フリーワード(単語ごとにカンマ区切り)]
    """)


@respond_to('メシ')
def search_command(message):
    search_word = message.body['text']

    # TODO: search_wordは、'メシ'も含まれているので、その対策が必要

    # TODO: ぐるなびAPIを呼ぶ

    # TODO: responseを整形してreply

    print(search_word)
