import datetime

x = datetime.datetime.now()

current_time = x.strftime("%I" + ":" + "%M")

class_end_time = "02:19"

hours_to_mins_one = int(current_time[0:2]) * 60

current_time_mins = hours_to_mins_one + (int(current_time[3]) * 10) + (int(current_time[4]))

hours_to_mins_two = int(class_end_time[0:2]) * 60

end_time_mins = hours_to_mins_two + (int(class_end_time[3]) * 10) + (int(class_end_time[4]))

time_til_end = end_time_mins - current_time_mins

print("Time until end of class: " + str(time_til_end) + " minutes")
