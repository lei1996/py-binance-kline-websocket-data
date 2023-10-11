
import os
import time
import logging
import argparse
import pandas as pd

from datetime import datetime, timedelta
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient


parser = argparse.ArgumentParser()
parser.add_argument('--name', help='pm2启动名称 like: BTCUSDT_um_futures_bn')
parser.add_argument('--symbol', help='品种代码 like: BTC')
args = parser.parse_args()
print(f"args: {args}")


name = args.name
symbol = args.symbol


print(f"name: {name}, start!")
print(f"symbol: {symbol}")

my_client = UMFuturesWebsocketClient()
my_client.start()


# 每小时更新一次到 csv 文件
def message_handler(message):
    print(message)


def sub_kline(symbol: str, interval: str):
    my_client.kline(
        symbol=symbol,
        id=12,
        interval=interval,
        callback=message_handler,
    )


if __name__ == '__main__':
    sub_kline(symbol="btcusdt", interval="1m")

    logging.debug("closing ws connection")
    my_client.stop()
