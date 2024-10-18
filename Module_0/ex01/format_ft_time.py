import time as tm

seconds_since_epoch = tm.mktime(tm.gmtime())
seconds_converted_to_actual_date = tm.ctime(seconds_since_epoch)

print(seconds_since_epoch)
print(seconds_converted_to_actual_date)

# days_from_epoch = ((tm.mktime(tm.gmtime()) / 60) / 60) / 24
# print(days_from_epoch)

