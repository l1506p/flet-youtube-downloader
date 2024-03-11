def convert(n):
    seconds = n % (48 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    if n <= 3599:
        return "%02d:%02d" % (minutes, seconds)
    else:
        return "%02d:%02d:%02d" % (hour, minutes, seconds)
