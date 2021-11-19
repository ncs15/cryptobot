from datetime import datetime
from logger import Logger
from data import Download_data


class CheckCandle:
    def check_current_time(self,pair,timeframes,time,dataset):
        new_candle = False
        prev_hour = time.strftime("%H")
        prev_day = time.strftime("%w")
        current_hour = datetime.now().strftime("%H")
        current_day = datetime.now().strftime("%w")
        prev_week = time.strftime("%U")
        current_week = datetime.now().strftime("%U")
        tf_for_update=[]
        if "1h" in timeframes:
            if current_hour != prev_hour:
                candle_update_time = datetime.now()
                new_candle = True    #checks if the chandle is new in order to download a new one for 4h.                        
                tf_for_update.append("1h")
                Logger().log(pair, f"Update 1h for {pair}")

        if "4h" in timeframes and new_candle is True:
            if current_hour in ["3", "6", "10", "14", "18", "22"]:
                tf_for_update.append("4h")
                Logger().log(pair, f"Update 4h for {pair}")
                # rethink, needs work

        if "1d" in timeframes:
            if current_day != prev_day:
                tf_for_update.append("1d")
                Logger().log(pair, f"Update 1d for {pair}")

        if "1w" in timeframes:
            if current_week != prev_week:
                tf_for_update.append("1w")
                Logger().log(pair, f"Update 1w for {pair}")

        if new_candle is True:
            dataset = Download_data().update(pair, tf_for_update, dataset)
            Logger().log(pair, f"Candle checker request for update on {pair}")


        return dataset;


