# fxea
## GMO
### API
[API](https://api.coin.z.com/fxdocs/#outline)
[Public API](https://forex-api.coin.z.com/public)
[Public WebSocket API](wss://forex-api.coin.z.com/ws/public)
[Private API](https://forex-api.coin.z.com/private)
[Private WebSocket API](wss://forex-api.coin.z.com/ws/private)
```
PYTHONPATH=src python3.10 src/fxea/main.py
```

## histdata
```
PYTHONPATH=src python3.10 src/fxea/hist.py
unzip *zip
cat DAT_ASCII_USDJPY_M1_202*csv | tr ';' ',' > USDJPY_M1_2025_03_05.csv
```
## oanda
### web-terminal
[HOME](https://www.oanda.jp/trade/practice)

[MT4-WEBTERMINAL](https://www.oanda.jp/fxproduct/mt4/mt4-webterminal)

