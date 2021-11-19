from binance.client import Client
import pandas as pd
from logger import Logger
from datetime import datetime
from compute import Compute

api_key = 'your api binance key'
api_secret = 'binance secret key'
client = Client(api_key, api_secret)



class Download_data:


    def download_data(self, pair, timeframes):
        return_list={}
        if "5m" in timeframes:
            candle5m = client.get_historical_klines(pair, "5m", f"1 day ago UTC+3", limit=200)

            df5m = pd.DataFrame(candle5m, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                   'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol',
                                                   'takerBuyQuoteVol',
                                                   'ignore'])
            df5m.dateTime = pd.to_datetime(df5m.dateTime, unit='ms')
            df5m.closeTime = pd.to_datetime(df5m.closeTime, unit='ms')
            df5m.set_index('dateTime', inplace=True)
            df5m.to_csv(f'dataset/{pair}_candle_5m.csv')
            Logger().log(pair, f"Download data for {pair}_5m")
            return_list["5m"] = df5m

        if "15m" in timeframes:
            candle15m = client.get_historical_klines(pair, "15m", f"2 day ago UTC+3", limit=200)

            df15m = pd.DataFrame(candle15m, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                   'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol',
                                                   'takerBuyQuoteVol',
                                                   'ignore'])
            df15m.dateTime = pd.to_datetime(df15m.dateTime, unit='ms')
            df15m.closeTime = pd.to_datetime(df15m.closeTime, unit='ms')
            df15m.set_index('dateTime', inplace=True)
            df15m.to_csv(f'dataset/{pair}_candle_15m.csv')
            Logger().log(pair, f"Download data for {pair}_15m")
            return_list["15m"] = df15m

        if "1h" in timeframes:

            candle1h = client.get_historical_klines(pair, "1h", f"9 day ago UTC+3", limit=200)

            df1h = pd.DataFrame(candle1h, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                   'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol',
                                                   'takerBuyQuoteVol',
                                                   'ignore'])
            df1h.dateTime = pd.to_datetime(df1h.dateTime, unit='ms')
            df1h.closeTime = pd.to_datetime(df1h.closeTime, unit='ms')
            df1h.set_index('dateTime', inplace=True)
            df1h.to_csv(f'dataset/{pair}_candle_1h.csv')
            Logger().log(pair, f"Download data for {pair}_1h")
            return_list["1h"] = df1h

        if "4h" in timeframes:
            candle4h = client.get_historical_klines(pair, "4h", f"25 day ago UTC+3", limit=100)
            df4h = pd.DataFrame(candle4h, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                   'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol',
                                                   'takerBuyQuoteVol',
                                                   'ignore'])
            df4h.dateTime = pd.to_datetime(df4h.dateTime, unit='ms')
            df4h.closeTime = pd.to_datetime(df4h.closeTime, unit='ms')
            df4h.set_index('dateTime', inplace=True)
            df4h.to_csv(f'dataset/{pair}_candle_4h.csv')
            Logger().log(pair, f"Download data for {pair}_4h")
            return_list["4h"] = df4h

        if "1d" in timeframes:
            candle1d = client.get_historical_klines(pair, "1d", f"205 day ago UTC+3", limit=100)
            df1d = pd.DataFrame(candle1d, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                   'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol',
                                                   'takerBuyQuoteVol',
                                                   'ignore'])
            df1d.dateTime = pd.to_datetime(df1d.dateTime, unit='ms')
            df1d.closeTime = pd.to_datetime(df1d.closeTime, unit='ms')
            df1d.set_index('dateTime', inplace=True)
            df1d.to_csv(f'dataset/{pair}_candle_1d.csv')
            Logger().log(pair, f"Download data for {pair}_1d")
            return_list["1d"] = df1d

        if "1w" in timeframes:
            candle1w = client.get_historical_klines(pair, "1w", f"205 week ago UTC+3", limit=100)
            df1w = pd.DataFrame(candle1w, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                   'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol',
                                                   'takerBuyQuoteVol',
                                                   'ignore'])
            df1w.dateTime = pd.to_datetime(df1w.dateTime, unit='ms')
            df1w.closeTime = pd.to_datetime(df1w.closeTime, unit='ms')
            df1w.set_index('dateTime', inplace=True)
            df1w.to_csv(f'dataset/{pair}_candle_1w.csv')
            Logger().log(pair, f"Download data for {pair}_1w")
            return_list["1w"] = df1w
        dataset_computed = Compute().ema(pair, return_list, timeframes)
        candle_update_time = datetime.now()
        return dataset_computed,candle_update_time;

    def update(self,pair,timeframes,dataset):
        return_list = {}
        if "5m" in timeframes:
            old_df = dataset["5m"]
            candle5m = client.get_historical_klines(pair, "5m", f"5 minute ago UTC+3", limit=200)

            df5m = pd.DataFrame(candle5m, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                   'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol',
                                                   'takerBuyQuoteVol',
                                                   'ignore'])
            df5m.dateTime = pd.to_datetime(df5m.dateTime, unit='ms')
            df5m.closeTime = pd.to_datetime(df5m.closeTime, unit='ms')
            df5m.set_index('dateTime', inplace=True)
            new_df = df5m
            df5m = old_df.append(new_df)
            df5m.to_csv(f'dataset/{pair}_candle_5m.csv')
            Logger().log(pair, f"Update data for {pair}_5m")

            return_list["5m"] = df5m

        if "15m" in timeframes:
            old_df = dataset["15m"]
            candle15m = client.get_historical_klines(pair, "15m", f"15 minute ago UTC+3", limit=200)

            df15m = pd.DataFrame(candle15m, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                     'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol',
                                                     'takerBuyQuoteVol',
                                                     'ignore'])
            df15m.dateTime = pd.to_datetime(df15m.dateTime, unit='ms')
            df15m.closeTime = pd.to_datetime(df15m.closeTime, unit='ms')
            df15m.set_index('dateTime', inplace=True)
            new_df = df15m
            df15m = old_df.append(new_df)
            df15m.to_csv(f'dataset/{pair}_candle_15m.csv')
            Logger().log(pair, f"Update data for {pair}_15m")
            return_list["15m"] = df15m

        if "1h" in timeframes:
            old_df = dataset["1h"]
            candle1h = client.get_historical_klines(pair, "1h", f"1 hour ago UTC+3", limit=200)

            df1h = pd.DataFrame(candle1h, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                   'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol',
                                                   'takerBuyQuoteVol',
                                                   'ignore'])
            df1h.dateTime = pd.to_datetime(df1h.dateTime, unit='ms')
            df1h.closeTime = pd.to_datetime(df1h.closeTime, unit='ms')
            df1h.set_index('dateTime', inplace=True)
            new_df = df1h
            df1h = old_df.append(new_df)
            df1h.to_csv(f'dataset/{pair}_candle_1h.csv')
            Logger().log(pair, f"Update data for {pair}_1h")
            return_list["1h"] = df1h

        if "4h" in timeframes:
            old_df = dataset["4h"]
            candle4h = client.get_historical_klines(pair, "4h", f"4 hour ago UTC+3", limit=100)
            df4h = pd.DataFrame(candle4h, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                   'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol',
                                                   'takerBuyQuoteVol',
                                                   'ignore'])
            df4h.dateTime = pd.to_datetime(df4h.dateTime, unit='ms')
            df4h.closeTime = pd.to_datetime(df4h.closeTime, unit='ms')
            df4h.set_index('dateTime', inplace=True)
            new_df = df4h
            df4h = old_df.append(new_df)
            df4h.to_csv(f'dataset/{pair}_candle_4h.csv')

            Logger().log(pair, f"Update data for {pair}_4h")
            return_list["4h"] = df4h

        if "1d" in timeframes:
            old_df = dataset["1d"]
            candle1d = client.get_historical_klines(pair, "1d", f"1 day ago UTC+3", limit=100)
            df1d = pd.DataFrame(candle1d, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                   'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol',
                                                   'takerBuyQuoteVol',
                                                   'ignore'])
            df1d.dateTime = pd.to_datetime(df1d.dateTime, unit='ms')
            df1d.closeTime = pd.to_datetime(df1d.closeTime, unit='ms')
            df1d.set_index('dateTime', inplace=True)
            new_df = df1d
            df1d = old_df.append(new_df)
            df1d.to_csv(f'dataset/{pair}_candle_1d.csv')
            Logger().log(pair, f"Update data for {pair}_1d")
            return_list["1d"] = df1d

        if "1w" in timeframes:
            old_df = dataset["1w"]
            candle1w = client.get_historical_klines(pair, "1w", f"1 week ago UTC+3", limit=100)
            df1w = pd.DataFrame(candle1w, columns=['dateTime', 'open', 'high', 'low', 'close', 'volume', 'closeTime',
                                                   'quoteAssetVolume', 'numberOfTrades', 'takerBuyBaseVol',
                                                   'takerBuyQuoteVol',
                                                   'ignore'])
            df1w.dateTime = pd.to_datetime(df1w.dateTime, unit='ms')
            df1w.closeTime = pd.to_datetime(df1w.closeTime, unit='ms')
            df1w.set_index('dateTime', inplace=True)
            new_df = df1w
            df1w = old_df.append(new_df)
            df1w.to_csv(f'dataset/{pair}_candle_1w.csv')
            Logger().log(pair, f"Update data for {pair}_1w")
            return_list["1w"] = df1w
        candle_update_time = datetime.now()
        dataset_computed = Compute().ema(pair, return_list, timeframes)
        Logger().log(pair, f"Update and compute data for {pair}")

        return dataset_computed,candle_update_time;

    def current_price(self,pair):
        price = float(client.get_symbol_ticker(symbol=pair)['price'])
        return price;

        

