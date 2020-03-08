import csv
import os

path = "D:\股票分析\源数据\stock_data"

filename_lst = os.listdir(path)
# sFileName = "D:\股票分析\源数据\stock_data\sh600000.csv"

#
# sFileName='ClosedTicketsAPJ.csv'

title_flag = True

n = 1
# stock_6month_lst = []

for name in filename_lst:
    flag = False
    date_lst = []
    price_lst = []
    sFileName = os.path.join(path, name)
    with open(sFileName, newline='') as csvfile:
        rows = csv.reader(csvfile)
        for row in rows:
            if len(row) >= 7:
                if row[2] == "2019-09-02":
                    flag = True
                    stockcode = row[0]
                    stockname = row[1].upper()
                if flag:
                    date_lst.append(row[2])
                    price_lst.append(row[6])
    # if title_flag:
    #     with open("stock.txt", "w") as f:
    #         new_lst1 = ["stockcode", "stockname"]
    #         new_lst1.extend(date_lst)
    #         wline_str = "/".join(new_lst1)
    #         f.write(wline_str + "\r\n")
    #     title_flag = False
    # print(name)
    # if price_lst:
    #     with open("stock.txt", "a") as f:
    #         new_lst = [stockcode, stockname]
    #         new_lst.extend(price_lst)
    #         wline_str = "/".join(new_lst)
    #         f.write(wline_str + "\r\n")
    #     new_lst.clear()
    if title_flag:
        with open("stock1.txt", "w") as f:
            new_lst1 = ["stockcode", "stockname", "maxprice", "minprice","last5up","last2prince","lastprince"]
            wline_str = "/".join(new_lst1)
            f.write(wline_str + "\r\n")
        title_flag = False
    print(name)
    if price_lst:
        length = len(price_lst)
        for num, prc in enumerate(price_lst):
            if num >= 5 and num <=length - 11:
                if prc > max(price_lst[num-5:num]) and prc > max(price_lst[num+1:num+6]):
                    maxprice = prc
                if prc < min(price_lst[num-5:num]) and prc < min(price_lst[num+1:num+6]):
                    minprice = prc
        last5up=(float(max(price_lst[-5:]))-float(price_lst[-6]))/float(price_lst[-6])*100
        with open("stock1.txt", "a") as f:
            new_lst = [stockcode, stockname, maxprice, minprice,str(last5up),str(price_lst[-7]),str(price_lst[-6])]
            # new_lst.extend(price_lst)
            wline_str = "/".join(new_lst)
            f.write(wline_str + "\r\n")
        new_lst.clear()
    n += 1
    # if n > 10:
    #     break

# print(date_lst, price_lst)
