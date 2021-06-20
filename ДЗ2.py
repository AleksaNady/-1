sec = int(input('Введите время в секундах: '))
sec_hours = 3600
min_hours = 60

hours = sec//sec_hours
mins = sec%sec_hours//min_hours
secs = (sec%sec_hours)%60

print(f"Время в формате чч:мм:сс {hours} : {mins} : {secs}")

#print(sec//sec_hours)
#print(sec%sec_hours//min_hours)
#print(sec%sec_hours-((sec%sec_hours//min_hours)*min_hours))

#time = int(input("Введите время в секундах "))
#hours = time // 3600
#minutes = (time - hours * 3600) // 60
#seconds = time - (hours * 3600 + minutes * 60)
#print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")