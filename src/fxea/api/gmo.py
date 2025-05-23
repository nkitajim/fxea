import sys
import requests
import datetime

import json
import websocket

class GmoPublicAPI:
	def __init__(
		self,
		base_url = "https://forex-api.coin.z.com",
	):
		self.base_url = base_url
		pass

	def request_api(self, method, path):
		url = self.base_url + path
		if "GET" == method.upper():
			res = requests.get(
				url,
				headers={"Content-Type": "application/json"},
			)
			if res.status_code >= 300:
				raise Exception("APIError." + res.text)

			return res.json()
		else:
			raise Exception("This Method Not Support")

	def get_status(self):
		jx = self.request_api("GET", "/public/v1/status")
		if jx["status"] == 0:
			return True

		return False

	def get_ticker(self):
		jx = self.request_api("GET", "/public/v1/ticker")
		return jx

	def get_klines(
		self,
		symbol="USD_JPY",
		priceType="BID",
		interval="1min",
		date=format(datetime.date.today(), "%Y%m%d"),
	):
		param = f"symbol={symbol}&priceType={priceType}&interval={interval}&date={date}"
		jx = self.request_api("GET", f"/public/v1/klines?{param}")
		return jx

	def get_symbols(self):
		jx = self.request_api("GET", "/public/v1/symbols")
		return jx

class GmoPublicWebSocketAPI:
	def __init__(
		self,
		url = "wss://forex-api.coin.z.com/ws/public/v1"
	):
		self.url = url

		pass

	def run(
		self,
		symbol = "USD_JPY",
	):
		# websocket.enableTrace(True)
		ws = websocket.WebSocketApp(self.url)

		def on_open(self):
			message = {
				"command": "subscribe",
				"channel": "ticker",
				"symbol": symbol,
			}
			ws.send(json.dumps(message))

		def on_message(self, message):
			print(message)

		ws.on_open = on_open
		ws.on_message = on_message

		ws.run_forever()
