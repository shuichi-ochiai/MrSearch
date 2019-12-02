from slackbot.bot import respond_to


@respond_to('助けて')
def help_command(message):
    message.reply("""助けるよ⭐️
    検索 - @mr_search メシ [フリーワード(単語ごとにカンマ区切り)]
    """)
