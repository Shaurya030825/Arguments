
bill_amount= int(input("please enter the bill: "))
tip_perc= int(input("Please enter the tip percent you would like to give: "))
def total_calc(bill_amount, tip_perc):
    total= bill_amount * (1 + 0.01*tip_perc)
    total= round(total,2)
    print(f"Please pay ${total}")
total_calc(bill_amount, tip_perc)