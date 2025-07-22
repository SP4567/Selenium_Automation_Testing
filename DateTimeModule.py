import datetime
print(datetime.date.today())
print(datetime.datetime.today())

current_date = datetime.date.today()
print(current_date)
current_time = datetime.datetime.now().time()
print(current_time)

current_date_time = datetime.datetime.today()

filename = current_date_time.strftime('%Y-%m-%d-%H-%M-%S-%f')
print(filename)