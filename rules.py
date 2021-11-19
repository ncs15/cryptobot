from logger import Logger
class Rules:
    def check_rules(self, pair, price, timeframes, dataset, strategy,list_of_trades, tp=None, sl=None, current_trade_id = None):

        ema_min = 0.9999
        ema_max = 1.0001

        if current_trade_id is not None:
            trigger = {"type": "opened", "strategy": "a trade was opened. waiting for close"}
            opened_trade_type = list_of_trades[current_trade_id]["type"]

            if tp is not None:
                o_price = list_of_trades[current_trade_id]["o_price"]

                if opened_trade_type is "long":
                    unrealized_proffit = (price - o_price) / o_price * 100
                    if unrealized_proffit >= tp:
                        trigger = {"type": "short", "strategy": "cloase at TP"}
                        Logger().log(pair, f"TP is hit")
                if opened_trade_type is "short":
                    unrealized_proffit = (o_price - price) / price * 100
                    if unrealized_proffit >= tp:
                        trigger = {"type": "long", "strategy": "cloase at TP"}
                        Logger().log(pair, f"TP is hit")
            if sl is not None:
                o_price = list_of_trades[current_trade_id]["o_price"]

                if opened_trade_type is "long":
                    unrealized_proffit = (price - o_price) / o_price * 100
                    print(unrealized_proffit)
                    if unrealized_proffit <= sl:
                        trigger = {"type": "short", "strategy": "cloase at SL"}
                        Logger().log(pair, f"SL is hit")
                if opened_trade_type is "short":
                    unrealized_proffit = (o_price - price) / price * 100
                    print(unrealized_proffit)
                    if unrealized_proffit <= sl:
                        trigger = {"type": "long", "strategy": "cloase at SL"}
                        Logger().log(pair, f"SL is hit")
        else:
            trigger = {"type": "inactive", "strategy": "no trade was opened"}



        if "5m" in timeframes:
            ema9_5m = float(dataset["5m"]['9ema'][-1:])
            ema21_5m = float(dataset["5m"]['21ema'][-1:])
            ema55_5m = float(dataset["5m"]['55ema'][-1:])
            ema100_5m = float(dataset["5m"]['100ema'][-1:])
            last_ema9_5m = float(dataset["5m"]['9ema'][-2:-1])
            last_ema21_5m = float(dataset["5m"]['21ema'][-2:-1])
            prev_close_5m = float(dataset["5m"]['close'][-2:-1])
            prev_open_5m = float(dataset["5m"]['open'][-2:-1])
        if "15m" in timeframes:
            ema9_15m = float(dataset["15m"]['9ema'][-1:])
            ema21_15m = float(dataset["15m"]['21ema'][-1:])
            ema55_15m = float(dataset["15m"]['55ema'][-1:])
            ema100_15m = float(dataset["15m"]['100ema'][-1:])
            last_ema9_15m = float(dataset["15m"]['9ema'][-2:-1])
            last_ema21_15m = float(dataset["15m"]['21ema'][-2:-1])
            prev_close_15m = float(dataset["15m"]['close'][-2:-1])
            prev_open_15m = float(dataset["15m"]['open'][-2:-1])
        if "1h" in timeframes:
            ema9_1h = float(dataset["1h"]['9ema'][-1:])
            ema21_1h = float(dataset["1h"]['21ema'][-1:])
            ema55_1h = float(dataset["1h"]['55ema'][-1:])
            ema100_1h = float(dataset["1h"]['100ema'][-1:])
            last_ema9_1h = float(dataset["1h"]['9ema'][-2:-1])
            last_ema21_1h = float(dataset["1h"]['21ema'][-2:-1])
            prev_close_1h = float(dataset["1h"]['close'][-2:-1])
            prev_open_1h = float(dataset["1h"]['open'][-2:-1])
            # prev_close_1h = int(input("prev close"))
            # prev_open_1h = int(input("prev open"))

        if "4h" in timeframes:
            ema9_4h = float(dataset["4h"]['9ema'][-1:])
            ema21_4h = float(dataset["4h"]['21ema'][-1:])
            ema55_4h = float(dataset["4h"]['55ema'][-1:])
            ema100_4h = float(dataset["4h"]['100ema'][-1:])
            last_ema9_4h = float(dataset["4h"]['9ema'][-2:-1])
            last_ema21_4h = float(dataset["4h"]['21ema'][-2:-1])
            prev_close_4h = float(dataset["4h"]['close'][-2:-1])
            prev_open_4h = float(dataset["4h"]['open'][-2:-1])
        if "1d" in timeframes:
            ema9_1d = float(dataset["1d"]['9ema'][-1:])
            ema21_1d = float(dataset["1d"]['21ema'][-1:])
            ema55_1d = float(dataset["1d"]['55ema'][-1:])
            ema100_1d = float(dataset["1d"]['100ema'][-1:])
            last_ema9_1d = float(dataset["1d"]['9ema'][-2:-1])
            last_ema21_1d = float(dataset["1d"]['21ema'][-2:-1])
            prev_close_1d = float(dataset["1d"]['close'][-2:-1])
            prev_open_1d = float(dataset["1d"]['open'][-2:-1])
        if "1w" in timeframes:
            ema9_1w = float(dataset["1w"]['9ema'][-1:])
            ema21_1w = float(dataset["1w"]['21ema'][-1:])
            ema55_1w = float(dataset["1w"]['55ema'][-1:])
            ema100_1w = float(dataset["1w"]['100ema'][-1:])
            last_ema9_1w = float(dataset["1w"]['9ema'][-2:-1])
            last_ema21_1w = float(dataset["1w"]['21ema'][-2:-1])
            prev_close_1w = float(dataset["1w"]['close'][-2:-1])
            prev_open_1w = float(dataset["1w"]['open'][-2:-1])


        if strategy == "daily":
            if (ema_min * ema9_1h <= price < ema_max * ema9_1h) and prev_close_1h < ema9_1h and (
                    ema21_1h > prev_open_1h or prev_open_1h > ema21_1h):
                trigger = {"type":"short","strategy":"daily-ema9_1h"}
            elif (ema_min * ema21_1h <= price < ema_max * ema21_1h) and prev_close_1h < ema21_1h:
                trigger = {"type": "short", "strategy": "daily-ema21_1h"}
            elif prev_close_1h > ema9_1h and (ema_min * ema9_1h <= price < ema_max * ema9_1h):
                trigger = {"type": "long", "strategy": "daily-ema9_1h"}
            elif (ema_min * ema21_1h <= price < ema_max * ema21_1h) and prev_close_1h > ema21_1h:
                trigger = {"type": "long", "strategy": "daily-ema21_1h"}
            elif prev_close_1h > ema100_1h and (ema_min * ema100_1h <= price < ema_max * ema100_1h):
                trigger = {"type": "long", "strategy": "daily-ema100_1h"}
            elif prev_close_1h < ema100_1h and (ema_min * ema100_1h <= price < ema_max * ema100_1h):
                trigger = {"type": "short", "strategy": "daily-ema100_1h"}
            elif (ema_min * ema9_4h <= price < ema_max * ema9_4h) and prev_close_4h < ema9_4h and (
                    ema21_4h > prev_open_4h or prev_open_4h > ema21_4h):
                trigger = {"type": "short", "strategy": "daily-ema9_4h"}
            elif (ema_min * ema21_4h <= price < ema_max * ema21_4h) and prev_close_4h < ema21_4h:
                trigger = {"type": "short", "strategy": "daily-ema21_4h"}
            elif prev_close_4h > ema9_4h and (ema_min * ema9_4h <= price < ema_max * ema9_4h):
                trigger = {"type": "long", "strategy": "daily-ema9_4h"}
            elif (ema_min * ema21_4h <= price < ema_max * ema21_4h) and prev_close_4h > ema21_4h:
                trigger = {"type": "long", "strategy": "daily-ema21_4h"}
            elif prev_close_4h > ema100_4h and (ema_min * ema100_4h <= price < ema_max * ema100_4h):
                trigger = {"type": "long", "strategy": "daily-ema100_4h"}
            elif prev_close_4h < ema100_4h and (ema_min * ema100_4h <= price < ema_max * ema100_4h):
                trigger = {"type": "short", "strategy": "daily-ema100_4h"}


        if trigger["type"] is not "inactive" and current_trade_id is not None and trigger["type"] == opened_trade_type:

            trigger = {"type": "opened", "strategy": "a trade was opened. waiting for close"}
            Logger().log(pair, f"New trigger rejected because the type is like the type of the current trade that is open --> {opened_trade_type}")


        Logger().log(pair, f"Price:{price}, ema9_1h:{round(ema9_1h * ema_min,2)}-{round(ema9_1h * ema_max,2)},ema21_1h:{round(ema21_1h * ema_min,2)}-{round(ema21_1h * ema_max,2)}")
        Logger().log(pair, f"Price:{price}, ema9_4h:{round(ema9_4h * ema_min,2)}-{round(ema9_4h * ema_max,2)},ema21_4h:{round(ema21_4h * ema_min,2)}-{round(ema21_4h * ema_max,2)}")
        Logger().log(pair, f"Price:{price}, ema9_1d:{round(ema9_1d * ema_min,2)}-{round(ema9_1d * ema_max,2)},ema21_1d:{round(ema21_1d * ema_min,2)}-{round(ema21_1d * ema_max,2)}")
        Logger().log(pair,f"Rule trigger: {trigger}")
        return trigger;