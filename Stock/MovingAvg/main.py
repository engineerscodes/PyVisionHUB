from colorama import Fore
from nsepy import get_history
from datetime import date
from datetime import datetime
from datetime import timedelta
from matplotlib import pyplot as plt
import pandas as pd

script = get_history(symbol="TCS",
                     start=date(2020, 10, 1),
                     end=date(2022, 12, 31))

Start_Date = "2020-11-1"  # make sure your having date of prev 21 days
Start_Date = datetime.strptime(Start_Date, "%Y-%m-%d")
plt_target_Date = Start_Date + timedelta(days=21)
print(f"Target Date is 21 + StartDate -> {plt_target_Date.date()}")
Closes = script["Close"]

plt_Closes = Closes[plt_target_Date.date():]
print(plt_Closes)
plt_dates = plt_Closes.index
# Blue Line 7 days
Blue_sum = 0
# Red Line 21 days
Red_sum = 0

tuple_df = zip(plt_Closes.index, plt_Closes)
# print(tuple_df)

# get first 21 days & 7 days avg
# Closes[plt_target_Date.date()]
# prev_7 = plt_target_Date.date() - timedelta(days=7) # few dates missing
# prev_21 = plt_target_Date.date() - timedelta(days=21) # few dates missing

# print(f"X-7 && X-21 DATE ->{type(prev_7)} && {prev_21}")

prev_7days = Closes.loc[:plt_target_Date.date()][-7:-1]
if len(prev_7days) != 6:
    print("Change start Date")
prev_21days = Closes.loc[:plt_target_Date.date()][-21:-1]
if len(prev_21days) != 20:
    print("Change start Date")

Blue_sum = sum(prev_7days)
Red_sum = sum(prev_21days)
Blue_Moving_avg = 0
Red_Moving_avg = 0
prev_Blue_stock_pr = 0
prev_Red_stock_pr = 0
print(prev_7days)
print(prev_21days)
print(f"Initial 6 days Sum : {Blue_sum}\nInitial 20 days Sum : {Red_sum}")

index = 0
x = []  # date on x-axis
y_blue = []  # price on y -axis
y_red = []
state = 0  # -1 down ,1 up
Blue_up_y1 = -1
Blue_up_date = -1
Stock_diff = -1
Stocks = pd.DataFrame(columns=["Start_date", "Starting_Price", "End_date", "Ending_Price", "Price_Difference"])
for date, stock_close_price in tuple_df:
    Blue_sum = Blue_sum + stock_close_price - prev_Blue_stock_pr
    Red_sum = Red_sum + stock_close_price - prev_Red_stock_pr
    print(f"Current BlueSum : {Blue_sum} && Red Sum {Red_sum} ")
    index = index + 1
    if index < 7:
        prev_Blue_stock_pr = prev_7days[index - 1]
    else:
        prev_Blue_stock_pr = plt_Closes[index - 7]
    if index < 21:
        prev_Red_stock_pr = prev_21days[index - 1]
    else:
        prev_Red_stock_pr = plt_Closes[index - 21]

    Blue_Moving_avg = Blue_sum / 7.0
    Red_Moving_avg = Red_sum / 21.0

    state = 1 if Blue_Moving_avg >= Red_Moving_avg else -1

    if state == 1:
        if Blue_up_y1 == -1:
            Blue_up_y1 = Blue_Moving_avg
            Blue_up_date = date
            print(Fore.RED + f"Blue line is going Up .... {Blue_up_y1}")
        print(Fore.RESET + "Blue Line is Above ..............................")
    else:
        if Blue_up_y1 != -1:
            # use the previous days price when it was just above red line  y_blue[-1]
            Stock_diff = abs(y_blue[-1] - Blue_up_y1)
            Stocks.loc[len(Stocks.index)] = [Blue_up_date, Blue_up_y1, x[-1], y_blue[-1], Stock_diff]
            print(Fore.RED + f"Absolute difference between y1 && y2 when blue line is above red = {Stock_diff}")
            Blue_up_y1 = -1
        print(Fore.RESET + "Red Line is Above ...............................")
    x.append(date)
    y_blue.append(Blue_Moving_avg)
    y_red.append(Red_Moving_avg)
    print(f"MovingAvg on Date {date}  Blue line {Blue_Moving_avg} && Red line {Red_Moving_avg} index {index}")
    print("---" * 40)

plt.plot(x, y_blue, label="Blue Line")
plt.plot(x, y_red, label="Red Line")
'''
the design gets messed
for x_i, y_i in zip(x, y_red):
    plt.annotate(text=str(y_i), xy=(x_i, y_i))
for x_i, y_i in zip(x, y_blue):
    plt.annotate(text=str(y_i), xy=(x_i, y_i))
plt.margins(x=0, y=0)
plt.xticks(x)
'''
# When blue line is above red line find diff in close price -> check console
print(Fore.MAGENTA)
print(Stocks)
plt.legend()
plt.show()
