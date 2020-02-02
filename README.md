# MrSearch
美味しいものを検索するSlackBot

## 環境
### Pipenv
- [pipenvのインストール方法](https://qiita.com/anvinon/items/5d9c128ef8b65b866dfe)
  - [Homebrewのインストール方法(Mac)](https://qiita.com/krtsato/items/ba567acacb93a7a02dd9)
  - [pipのインストール方法(Win, Mac, Linux)](https://qiita.com/suzuki_y/items/3261ffa9b67410803443)
- 当プロジェクトでは既にPipfileが用意されているので、導入後プロジェクト直下で`pipenv install`を実行すれば良い

### 各APIKey
- 必要なAPIKeyは、環境変数から読み込む仕様にしている
- SlackBot
  - `SLACK_BOT_API_TOKEN`へセット
- ぐるなびAPI
  - `GURUNAVI_API_TOKEN`へセット
  
- APIKey設定方法
  - .bash_profile
    - ```
        export SLACK_BOT_API_TOKEN=*********
        export GURUNAVI_API_TOKEN=*********
      ```
  - PyCharm
    - `run` -> `Edit Config` -> `Environment variables` -> key,valueで設定 

## Gitについて
- [Git入門](https://qiita.com/nnahito/items/e546b27f73e7be131d4e)
- [Gitのインストール方法](https://qiita.com/toshi-click/items/dcf3dd48fdc74c91b409)
- [GitのGUIツールであるSourcetreeのインストール方法、使い方](https://tracpath.com/bootcamp/learning_git_sourcetree.html)
- [Githubの使い方](https://techacademy.jp/magazine/6235)

## slackbotについて
- [slackbot](https://github.com/lins05/slackbot)
- [slackbotのチュートリアル](https://qiita.com/sukesuke/items/1ac92251def87357fdf6)

## ぐるなびAPIについて
- [ぐるなびのレストラン検索API仕様](https://api.gnavi.co.jp/api/manual/restsearch/)
- [Python3におけるぐるなびAPIのサンプル](https://qiita.com/ume1126/items/14e9c1b0662acc289b19)
