from fxea.api.gmo import GmoPublicAPI 
from fxea.api.gmo import GmoPublicWebSocketAPI
from fxea.models.google_timesfm import get_forecast, finetune
import datetime
import pandas as pd
import json

def main():
	api = GmoPublicAPI()
	# print(api.get_status())
	# print(json.dumps(api.get_ticker(), indent=2))
	data = api.get_klines()["data"]
	# print(json.dumps(api.get_symbols(), indent=2))

	# api = GmoPublicWebSocketAPI()
	# api.run()
	finetune()

	df = pd.read_json(json.dumps(data))
	df["ds"] = pd.to_datetime(df["openTime"] / 1000, unit='s')
	df["unique_id"] = "FX_USD_JPY_BID_1min"

	pd.set_option('display.max_rows', 1000)

	df["vx"] = df["open"].diff()
	df["vx"].fillna(0)
	df["max"] = df["high"] - df["open"]
	df["min"] = df["low"] - df["open"]

	#print(df)
	#forecast_df = get_forecast(df, "max")
	#print(forecast_df.head(5))
	#forecast_df = get_forecast(df, "min")
	#print(forecast_df.head(5))
	forecast_df = get_forecast(df, "vx", "timesfm_fx_model.pth")
	print(forecast_df.head(5))

	pass


if __name__ == "__main__":
	main()