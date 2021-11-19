from logger import Logger


class Compute:

    def ema(self,pair,dataset,timeframes):
        return_list = {}
        for tf in timeframes:
            dataset[tf]['9ema'] = dataset[tf].close.ewm(span=9, adjust=False).mean()
            dataset[tf]['21ema'] = dataset[tf].close.ewm(span=21, adjust=False).mean()
            dataset[tf]['55ema'] = dataset[tf].close.ewm(span=100, adjust=False).mean()
            dataset[tf]['100ema'] = dataset[tf].close.ewm(span=100, adjust=False).mean()
            return_list[tf] = dataset[tf]
            Logger().log(pair, f"EMA was computed for {pair}on timeframe: {tf}")
        return return_list;