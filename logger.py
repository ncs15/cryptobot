from datetime import datetime

class Logger:
    def log(self, pair, message):
        with open(f"logs/{pair}.log", "a") as f:
            f.write(str(datetime.now()))
            f.write(":     ")
            f.write(str(message))
            f.write("\n")
