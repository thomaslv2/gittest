import csv
import os

path = "D:\股票分析\A股半年数据.csv"

n = 0
flag = True
date_lst = []
price_lst = []
with open(path, newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        if flag:
            date_lst = row
            with open("stockeq0306.txt", "w") as f:
                new_lst1 = ["stockcode", "stockname", "maxprice", "minprice"]
                wline_str = "/".join(new_lst1)
                f.write(wline_str + "\r\n")
            flag = False
            continue
        else:
            stockcode = row[0]
            stockname = row[1]
            price_lst = row[2:]
        if price_lst:
            length = len(price_lst)
            for num, prc in enumerate(price_lst):
                if num >= 5 and num <= length - 6:
                    if prc > max(price_lst[num - 5:num]) and prc > max(price_lst[num + 1:num + 6]):
                        maxprice = prc
                    if prc < min(price_lst[num - 5:num]) and prc < min(price_lst[num + 1:num + 6]):
                        minprice = prc
            with open("stockeq0306.txt", "a") as f:
                new_lst = [stockcode, stockname, maxprice, minprice]
                wline_str = "/".join(new_lst)
                f.write(wline_str + "\r\n")
            new_lst.clear()
