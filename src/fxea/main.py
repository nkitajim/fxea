from fxea.api.gmo import GmoPublicAPI 
from fxea.api.gmo import GmoPublicWebSocketAPI 
import json

def main():
	api = GmoPublicAPI()
	# print(api.get_status())
	# print(json.dumps(api.get_ticker(), indent=2))
	# print(json.dumps(api.get_klines(), indent=2))
	# print(json.dumps(api.get_symbols(), indent=2))

	api = GmoPublicWebSocketAPI()
	api.run()


if __name__ == "__main__":
	main()
