# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename):
    f = open(filename, "rt")
    rows = csv.reader(f)
    [name_header, shares_header, price_header] = next(rows)
    print(f"{name_header:10s} {shares_header:>10s} {price_header:>10s}")

    total_spend = 0.0

    for row in rows:
        try:
            [symbol, shares_str, price_str] = row
            shares = int(shares_str)
            share_price = float(price_str)
            total_spend += shares * share_price
            print(f"{symbol:10s} {shares:10d} {share_price:10.2f}")
        except ValueError:
            print(f"WARNING: bad input line {row}")

    f.close()
    return total_spend

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Work/Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total cost ${cost:0.2f}")
