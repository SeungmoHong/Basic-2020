import datetime
current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
year , month , day = map(int, input('생일 입력>').split())
if current_month > month :
elif current_month < month :
    age = current_year - year - 1
else:
    if current_day < birth_day :
            age = current_year - year - 1
print(age)
print('만 나이는 %d 입니다.' %age)