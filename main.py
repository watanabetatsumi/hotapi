import requests
import json
import os
from dotenv import load_dotenv

# 環境変数（APIキー）の取得
load_dotenv()
HOTPEPPER_API_KEY = os.environ["HotPepper_API_KEY"]

# 引数に検索条件を指定して、HotPepperAPIにアクセス
def get_recommend(keyword,count,address,budget):
  global HOTPEPPER_API_KEY
  url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
  if budget == "はい":
    budget = "B001"
  else:
    budget = None
  params = {
    "key" : HOTPEPPER_API_KEY,
    "keyword" : keyword,
    "count" : count,
    "format" : "json",
    "address" : address,
    "budget" : budget, 
  }
  response = requests.get(url, params=params)
  # JSONのエンコードしてエラー処理
  data = response.json()

  if "error" in data:
    return "おススメの店舗情報が見つかりませんでした。"

  # レスポンスからお店の検索結果（店名＆住所）を取得
  shops = data["results"]["shop"]
  recommendations = []
  for shop in shops:
    name = shop["name"]
    address = shop["address"]
    recommendation = f"店名: {name}\n住所: {address}\n\n"
    recommendations.append(recommendation)

  return "\n".join(recommendations)
# 検索条件を標準入力する
address = input("お店の場所は?->")
keyword = input("検索ワードを入力してください->")
budget = input("予算は低め？（はい/いいえ）->")
count = int(input("知りたい店舗数は？->"))

recommendation = get_recommend(keyword,count,address,budget)
# 結果を表示する
print(recommendation)
