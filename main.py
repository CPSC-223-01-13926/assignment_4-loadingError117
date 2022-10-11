from weather import *

myfile = "weather.dat"
switch = 0
while (switch != 9) :
    print("	      *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n")
    print("1. Set data filename\n2. Add weather data\n3. Print daily report\n4. Print historical report\n9. Exit the program\n")
    switch = int(input("Enter menu choice: "))
    weather = read_data(myfile)
    if(switch == 1) :
        myfile = input("Please input a new filename: ")
    elif (switch == 2) :
        date = input("Enter date: ")
        time = input("Enter time: ")
        temp = int(input("Enter temperature: "))
        humi = int(input("Enter humidity: "))
        rain = float(input("Enter rain: "))
        weather[date+time] = {'t': temp, 'h' : humi, 'r' : rain}
        write_data(weather, myfile)
    elif (switch == 3) :
        date = input("Please input a date to parse: ")
        print (report_daily(weather, date))
    elif (switch == 4) :
        print(report_historical(read_data(myfile)))
    elif (switch == 9) :
        break