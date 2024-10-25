import time as tm

# Retrieve current date from struct_time
get_my_date = tm.gmtime()

# Format struct time into desired format
seconds_since_epoch = tm.time()
formated_date = tm.strftime("%b %d %Y", get_my_date)

print("Seconds since January 1, 1970:", f"{seconds_since_epoch:,}", "or", f"{seconds_since_epoch:.9}", "in scientific notation")
print(formated_date)
