def make_readable(n):
    seconds = n % (60)
    hour = n // 360
    print("hour: " + str(hour))
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d:%02d" % (hour, minutes, seconds)


# Driver program
n = 36000
print(make_readable(n))
