# import the library
import pendulum

# There are several different methods available to create a new `DateTime` instance.
# First there is the main `datetime()` helper.
dt = pendulum.datetime(2015, 2, 5)
print(dt)  # 2015-02-05T00:00:00+00:00

print(type(dt))  # <class 'pendulum.datetime.DateTime'>

print(dt.timezone.name)  # UTC

# datetime() sets the time to 00:00:00 if it's not specified, and the timezone (the tz keyword argument) to UTC. 
# Otherwise it can be a Timezone instance or simply a string timezone value.
dt_paris = pendulum.datetime(2015, 2, 5, tz='Europe/Paris')
print(dt_paris.timezone.name)  # Europe/Paris

tz = pendulum.timezone('Europe/Paris')
dt_paris_2 = pendulum.datetime(2015, 2, 5, tz=tz)
print(dt_paris_2.timezone.name)  # Europe/Paris

# The special local string is also supported and will return your current timezone.
dt_local = pendulum.datetime(2015, 2, 5, tz='local')
print(dt_local.timezone.name)  # Asia/Karachi

dt_local_2 = pendulum.local(2015, 2, 5)
print(dt_local.timezone.name)  # Asia/Karachi
# `local()` is just an alias for `datetime(..., tz='local')`.

# There is also the `now()` method.
dt_now = pendulum.now('America/Toronto')
print(dt_now)
print(dt_now.timezone.name)  # America/Toronto

dt_now_2 = pendulum.now()
print(dt_now_2.timezone.name)  # local timezone

# To accompany now(), a few other static instantiation helpers exist to create known instances. 
# The only thing to really notice here is that today(), tomorrow() and yesterday(), besides behaving as expected, 
# all accept a timezone parameter and each has their time value set to 00:00:00.
dt_today = pendulum.today(tz='Asia/Calcutta')
print(dt_today)

dt_yesterday = pendulum.yesterday()
print(dt_yesterday)  # local time zone

dt_tomorrow = pendulum.tomorrow()
print(dt_tomorrow)  # local time zone

# Pendulum enforces timezone aware datetimes, and using them is the preferred and recommended way of using the 
# library. However, if you really need a naive `DateTime` object, the `naive()` helper is there for you.
dt_naive = pendulum.naive(2015, 2, 5)
print(dt_naive.timezone)  # None

# `from_format()`, is similar to the native `datetime.strptime()` function but uses custom tokens to create a 
# `DateTime` instance.
dt_custom = pendulum.from_format("2021/31/12 12", "YYYY/DD/MM HH", tz='Asia/Karachi')
print(dt_custom)  # 2021-12-31T12:00:00+05:00
print(dt_custom.timezone.name)  # default => UTC | but can also change as shown above
# To see all the available tokens, check out this page
# https://pendulum.eustace.io/docs/#formatter

# if you find yourself inheriting a `datetime.datetime` instance,
# you can create a `DateTime` instance via the instance() function.
import datetime
dt_native = datetime.datetime(2008, 1, 1)
p = pendulum.instance(dt_native)
print(p)