from datetime import datetime
alarm_time = ("Enter the time of alarm: HH:MM:SS\n")
alarm_hour = alarm_time[0:2]
alar_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm:...")
while True:
    now = datetime.now()
    current_period = now.strftime("%p")
    current_hour = now.strftime("%H")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    if (alarm_time==current_period):
        if(alarm_time==current_hour):
            if(alarm_time==current_minute):
                if(alarm_time==current_second):
                    print("wakeUp")
                    break
    


