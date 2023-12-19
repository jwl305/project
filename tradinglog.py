import pandas as pd
from datetime import datetime

# Initialize an empty DataFrame to store your trades
columns = ['Date', 'Crypto', 'Size', 'Buy/Sell', 'Amount', 'Entry Price', 
           'Exit Price', 'TP', 'SL', 'Fee', 'Balance', 'Strategy', 
           'Leverage', 'Profit/Loss', 'Cumulative P/L', 'Notes']
trade_journal = pd.DataFrame(columns=columns)

# Function to add a trade
def add_trade(crypto, size, buy_sell, amount, entry_price, exit_price,
              target_price, stop_loss, fee, total_balance, strategy,
              leverage, notes=''):
    global trade_journal
    profit_loss = (exit_price - entry_price) * amount if buy_sell.lower() == 'buy' else (entry_price - exit_price) * amount
    cumulative_pl = trade_journal['Profit/Loss'].sum() + profit_loss

    trade = {
        'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'Crypto': crypto,
        'Size': size,
        'Buy/Sell': buy_sell,
        'Amount': amount,
        'Entry Price': entry_price,
        'Exit Price': exit_price,
        'TP': target_price,
        'SL': stop_loss,
        'Fee': fee,
        'Balance': total_balance,
        'Strategy': strategy,
        'Leverage': leverage,
        'Profit/Loss': profit_loss,
        'Cumulative P/L': cumulative_pl,
        'Notes': notes
    }
    # Append the trade to the journal
    trade_journal = trade_journal.append(trade, ignore_index=True)

# Example of adding trades
add_trade('BTC', 0.1, 'Buy', 0.1, 35000, 36000, 37000, 34000, 50, 100000, 'Trend Following', 10, 'Bullish pattern observed')
add_trade('ETH', 2, 'Sell', 2, 2500, 2400, 2600, 2550, 30, 102000, 'Mean Reversion', 5, 'Reached target price')

# Save the journal to a CSV file
trade_journal.to_csv('crypto_trade_journal.csv', index=False)

# Print the journal
print(trade_journal)