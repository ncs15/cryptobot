from data import Download_data
import threading
from logger import Logger
from compute import Compute
from time import sleep
from rules import Rules
from candle_checker import CheckCandle
from trade import Trade
from datetime import datetime




#define trading paris and strategy
#tp/sl is %. for example "tp":5 means 5%
pairs = {"BTCUSDT":{"strategy": "daily", "used_tf": ["1h","4h","1d"], "tp": 5, "sl": -5},
       }


def start(pair):
    data = Download_data()
    compute = Compute()
    rules = Rules()
    check_candle = CheckCandle()
    list_of_trades = {}
    #variable initialization
    timeframes = pairs[pair]["used_tf"]
    strategy = pairs[pair]["strategy"]
    tp = pairs[pair]["tp"]
    sl = pairs[pair]["sl"]
    #download the first set of data
    dataset, candle_update_time = data.download_data(pair, timeframes)

    while True:
        sleep(5)
        price = data.current_price(pair)
        #check if it is needed an chandle update
        dataset = check_candle.check_current_time(pair,timeframes, candle_update_time,dataset)
        #check the price vs the rules, if price is in range --> return trigger for a new trade
        trade_trigger = rules.check_rules(pair, price,timeframes,dataset,strategy,list_of_trades)
        print(float(dataset["1h"]['9ema'][-1:]))
        #if the trigger exist then create trade
        if trade_trigger["type"] != "inactive":
            trade_trigger, current_trade_id = Trade().create_trade(pair, trade_trigger, price, list_of_trades)
            print(trade_trigger)
            #change the trigger state after the trade creation
            while trade_trigger['type'] == "opened":
          
                
                price = data.current_price(pair)

                #check if it is needed an chandle update
                dataset = check_candle.check_current_time(pair, timeframes, candle_update_time, dataset)
                # verifica pretul prin reguli, returneaza trigger cu new trade pentru inchiderea primului daca e cazul, fie de la strategy, fie
                #check the price vs the rules, if price is in range/tp/sl --> return trigger for a new trade. close prev trade if needed
                trade_trigger = rules.check_rules(pair, price, timeframes, dataset, strategy,list_of_trades, tp=tp, sl=sl, current_trade_id=current_trade_id)


                if trade_trigger["type"] in ["long","short"]:
                    trade_trigger, current_trade_id = Trade().create_trade(pair, trade_trigger, price, list_of_trades, close_prev_trade=True)


#start one thread for one trading pair
threads = []
for pair in pairs:
    t = threading.Thread(target=start,args=[pair])
    threads.append(t)
    t.start()
    Logger().log(pair, f"Start thread for {pair}")