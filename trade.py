from logger import Logger
from datetime import datetime

class Trade:

    def id_generator(self,pair):
        with open("id.txt", "r") as f:
            old_id = int(f.read())

        new_id = old_id + 1
        with open("id.txt", "w") as f:
            f.write(str(new_id))
        Logger().log(pair, f"New TradeId generated for {pair}")
        return new_id,old_id

    def create_trade(self, pair, trigger, price, list_of_trades, close_prev_trade=False):
        if close_prev_trade is True:
            Logger().log(pair, f"New trade function: 'close previews trade'")
        elif close_prev_trade is False:
            Logger().log(pair, f"New trade function: 'create new trade'")

        trade_trigger = {"type": "opened", "strategy": "a trade was opened. waiting for close"}
        current_id, prev_tradeid = Trade().id_generator(pair)
        trade = {"Pair": pair, "type": trigger["type"], "strategy": trigger["strategy"],
                             "o_price": price, "c_price": "still_open", "return": "still_open"}

        list_of_trades[current_id] = trade

        with open(f"trades_open_{pair}.txt", "a") as f:
            f.write(str(trade))
            f.write("\n")


        Logger().log(pair, f"New Trade created: {trade}")

        if close_prev_trade is True:


            trade_trigger = {"type": "inactive", "strategy": "a trade was opened. waiting for close"}
            list_of_trades[current_id]["o_price"] = list_of_trades[prev_tradeid]["o_price"]
            list_of_trades[prev_tradeid]["c_price"] = price
            list_of_trades[current_id]["c_price"] = price
            list_of_trades[current_id]["closing_tradeid"] = current_id
            if list_of_trades[prev_tradeid]["type"] == "long":
                list_of_trades[prev_tradeid]["return"] = f'{(int(list_of_trades[prev_tradeid]["c_price"])-int(list_of_trades[prev_tradeid]["o_price"]))/int(list_of_trades[prev_tradeid]["o_price"])} %'
                list_of_trades[current_id]["return"] = f'{(int(list_of_trades[prev_tradeid]["c_price"]) - int(list_of_trades[prev_tradeid]["o_price"])) / int(list_of_trades[prev_tradeid]["o_price"])} %'
            elif list_of_trades[prev_tradeid]["type"] == "short":
                list_of_trades[prev_tradeid]["return"] = f'{(int(list_of_trades[prev_tradeid]["o_price"]) - int(list_of_trades[prev_tradeid]["c_price"])) / int(list_of_trades[prev_tradeid]["c_price"])} %'
                list_of_trades[current_id]["return"] = f'{(int(list_of_trades[prev_tradeid]["o_price"]) - int(list_of_trades[prev_tradeid]["c_price"])) / int(list_of_trades[prev_tradeid]["c_price"])} %'

        Logger().log(pair, f"Trade creation trigger: {trade_trigger}")
        return trade_trigger, current_id;

