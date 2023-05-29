import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
HOTPEPPER_API_KEY = os.environ["HotPepper_API_KEY"]

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
  data = response.json()

  if "error" in data:
    return "おススメの店舗情報が見つかりませんでした。"

  shops = data["results"]["shop"]
  recommendations = []
  for shop in shops:
    name = shop["name"]
    address = shop["address"]
    recommendation = f"店名: {name}\n住所: {address}\n\n"
    recommendations.append(recommendation)

  return "\n".join(recommendations)

address = input("お店の場所は?->")
keyword = input("検索ワードを入力してください->")
budget = input("予算は低め？（はい/いいえ）->")
count = int(input("知りたい店舗数は？->"))

recommendation = get_recommend(keyword,count,address,budget)
print(recommendation)
