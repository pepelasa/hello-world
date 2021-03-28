import sys
import math


def profit(item):

    unit_profit = item["sell_price"] - item["cost_price"]
    quantity = item["inventory"]

    return int(round(unit_profit * quantity))


if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} cost_price sell_price inventory")
    exit()

cost = float(sys.argv[1])
sell = float(sys.argv[2])
inv = int(sys.argv[3])

if inv < 0:
    print("Inventory should be greater or equal to 0")
    quit()

result = profit({"cost_price": cost, "sell_price": sell, "inventory": inv})

print(f"{result} is the profit of selling {inv} at a winning of {sell - cost}")
