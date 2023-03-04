year = input("歡迎使用日期轉換器，請輸入國曆年")
month = input("請輸入入國曆月")
day = input("請輸入入國曆日")
def date_tran(year, month, day):
    try:
        western_year = int(year) + 1911
        month = int(month)
        day = int(day)
    except:
        print("請使用阿拉伯數字輸入")
    date = str(western_year) + "/" + str(month) + "/" + str(day)
    return date