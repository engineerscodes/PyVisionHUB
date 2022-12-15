import pandas as pd
import requests
from datetime import date
import asyncio

URL = "https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json"


async def get_data(url: str) -> list[str]:
    print(url)
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'}
    r = requests.get(url, timeout=3, headers=headers)
    stock = r.json()
    list_cmp = stock['data']
    Symbols = []
    for i in list_cmp:
        Symbols.append(i['symbol'])
    if len(Symbols) != 50:
        raise Exception(f"No of Symbol is Less < 50 ,expected 50 got ->{len(Symbols)}")

    return Symbols


async def Company_cmp(Csv_Url: str, fn_Symbols):
    # CmpSymbol = fn_df.iloc[:, 2]
    # CmpSymbol
    # fix column names & cleaning xlsx file
    fn_df = pd.read_excel(Csv_Url)
    fn_df.rename(columns={
        'Stock Screener, Technical Analysis Scanner': 'Sr.',
        'Unnamed: 1': 'Stock Name', 'Unnamed: 2': 'Symbol', 'Unnamed: 3': 'Links', 'Unnamed: 4': '% Chg',
        'Unnamed: 5': 'Price',
        'Unnamed: 6': 'Volume'
    },
        inplace=True)
    # print(fn_df.columns)
    Nifty = {}
    Index_list = []
    for index, row in fn_df.iterrows():
        symbol = row['Symbol']
        if symbol in fn_Symbols:
            print("---" * 50)
            print(f"Found {symbol} at index {index}")
            Index_list.append(index)
    print("---" * 50)
    Targeted_rows = fn_df.loc[Index_list]
    new_df = pd.DataFrame(Targeted_rows)
    print(new_df.columns)
    filename = Csv_Url.split('\\')[-1].split('.')[0] + date.today().strftime("%d-%m-%Y")
    print(filename)
    new_df.to_csv(f"Result_{filename}.csv", index=False)
    print(f"\t\t\t\t\t\t\t\t MATCHING COMPANY DETAILS  \n {new_df.to_string()}")


'''Symbols = get_data(URL)
print(Symbols)
Company_cmp("Files\\Stock Screener, Technical Analysis Scanner (1).xlsx", Symbols)

# Testing with second scv file
Company_cmp("Files\\Stock Screener, Technical Analysis Scanner (2).xlsx", Symbols)
'''


async def main():
    Symbols = await get_data(URL)
    print(Symbols)
    f1 = loop.create_task(Company_cmp("Files\\Stock Screener, Technical Analysis Scanner (1).xlsx", Symbols))
    f2 = loop.create_task(Company_cmp("Files\\Stock Screener, Technical Analysis Scanner (2).xlsx", Symbols))
    await asyncio.wait([f1, f2])


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
