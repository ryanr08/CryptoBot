import sys, os
sys.path.insert(0, os.path.abspath("./src"))
import coinbase_api as cb
import algorithms as alg
import time
from datetime import datetime
import utils

def main():

    ticker = "XLM-USD"
    acct_balance = 1000000 # Amount in dollars of available paper money

    high_frequency_algorithm = alg.HighFreqTrading(ticker, acct_balance, cb.calculateSMA, utils.buy, utils.sell, cb.getCurrentPrice)

    # Daemon
    utils.writelog(f"CryptoBot has started and is actively tracking {ticker}.")
    counter = 0
    while (counter < 51840):
        counter += 1    # Stops cryptobot from running after 72 hours.
        # Run trading algorithm
        high_frequency_algorithm.run()
        # Run calculations every 5 seconds.
        time.sleep(5)

    # Get final balance
    acct_balance += high_frequency_algorithm.sell_all()
    utils.writelog(str(datetime.now()))
    utils.writelog(f"FINAL BALANCE: ${acct_balance}\n")

if __name__ == "__main__":
    main()