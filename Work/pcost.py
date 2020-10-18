# pcost.py
#
# Exercise 1.27

f = open("Work/Data/portfolio.csv", "rt")
[name_header, shares_header, price_header] = next(f).strip().split(",")
print(f"{name_header:10s} {shares_header:>10s} {price_header:>10s}")

total_spend = 0.0

for line in f:
    [symbol, shares_str, price_str] = line.strip().split(",")
    shares = int(shares_str)
    share_price = float(price_str)
    total_spend += shares * share_price
    print(f"{symbol:10s} {shares:10d} {share_price:10.2f}")

print("-------")
print(f"Total cost ${total_spend:0.2f}")
f.close()
