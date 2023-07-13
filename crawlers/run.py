
import requests
import pandas as pd
import concurrent.futures
from datetime import date


def fetch_pes():
    columns = {
        "BOARD_NAME": "行业",
        "PCF_OCF_TTM": "PCF",
        "PB_MRQ": "PB",
        "PEG_CAR": "PEG",
        "PE_LAR": "PE(静)",
        "PE_TTM": "PE(TTM)"
    }

    url = "https://datacenter-web.eastmoney.com/api/data/v1/get"

    params = {
        "reportName": "RPT_VALUEINDUSTRY_DET",
        "columns": "ALL",
        "pageNumber": "1",
        "sortColumns": "PE_TTM",
        "filter": "(TRADE_DATE='2023-07-13')"
    }

    try:
        res = requests.get(url, params=params)

        if (res.status_code != 200):
            raise ValueError(res.text)

        resJson = res.json()
        data = resJson["result"]["data"]
        df = pd.DataFrame(data)
        df.rename(
            columns=columns,
            inplace=True
        )
        df.to_csv("./data/pe-{}.csv".format(date.today()), index=False)
    except Exception as e:
        print("Error: " + e)


def fetch_etfs():
    columns = {
        "f12": "代码",
        "f14": "名称",
        "f2": "最新价",
        "f4": "涨跌额",
        "f3": "涨跌幅 %",
        "f5": "成交量",
        "f6": "成交额",
        "f17": "开盘价",
        "f15": "最高价",
        "f16": "最低价",
        "f18": "昨收",
        "f8": "换手率",
        "f21": "流通市值",
        "f20": "总市值",
    }

    url = "http://88.push2.eastmoney.com/api/qt/clist/get"

    params = {
        "pn": "1",
        "pz": "2000",
        "po": "1",
        "np": "1",
        "ut": "bd1d9ddb04089700cf9c27f6f7426281",
        "fltt": "2",
        "invt": "2",
        "wbp2u": "|0|0|0|web",
        "fid": "f3",
        "fs": "b:MK0021,b:MK0022,b:MK0023,b:MK0024",
        "fields": ','.join(list(columns.keys())),
        "_": "1672806290972",
    }
    try:
        res = requests.get(url, params=params)
        if (res.status_code != 200):
            raise ValueError(res)

        resJson = res.json()
        diff = resJson["data"]["diff"]
        df = pd.DataFrame(diff)
        df.rename(
            columns=columns,
            inplace=True
        )
        df.to_csv("./data/etf-{}.csv".format(date.today()), index=False)
    except Exception as e:
        print("Error: " + e)

def run():
    print("run")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(fetch_pes),
            executor.submit(fetch_etfs)
        ]

    concurrent.futures.as_completed(futures)


