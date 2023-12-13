import pandas as pd
from datetime import datetime

# Initialize an empty DataFrame to store your trades
columns = ['Date', 'Crypto', 'Buy/Sell', 'Amount', 'Price', 'Notes']
trade_journal = pd.DataFrame(columns=columns)

# Function to add a trade
def add_trade(crypto, buy_sell, amount, price, notes=''):
    global trade_journal
    trade = {
        'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Crypto': crypto,
        'Buy/Sell': buy_sell,
        'Amount': amount,
        'Price': price,
        'Notes': notes
    }
    # Append the trade to the journal
    trade_journal = trade_journal.append(trade, ignore_index=True)

# Example of adding trades
add_trade('BTC', 'Buy', 0.1, 35000, 'Bullish pattern observed')
add_trade('ETH', 'Sell', 2, 2500, 'Reached target price')

# Save the journal to a CSV file
trade_journal.to_csv('crypto_trade_journal.csv', index=False)

# Print the journal
print(trade_journal)
