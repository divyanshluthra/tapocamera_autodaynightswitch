from pytapo import Tapo
import sys
from suntime import Sun
from datetime import datetime, timedelta
import pytz
import time


password_cloud = "password" # Tapo cloud password 
host = "192.168.0.160" # ip of the camera, example: 192.168.1.52


# 1. Define location (Gurgaon)
latitude = 28.4595
longitude = 77.0266
sun = Sun(latitude, longitude)

# 2. Get local sunrise time for today
# Ensure timezone is set to IST (India Standard Time)
local_tz = pytz.timezone('Asia/Kolkata')
today_date = datetime.now(local_tz)
sun_sunset = sun.get_sunset_time(today_date)
local_sunset = sun_sunset.astimezone(local_tz)

# 3. Add 15 minutes using timedelta
target_time = local_sunset  + timedelta(minutes=15)

# 4. Print the result
print(f"Sunset in Gurgaon: {local_sunset.strftime('%H:%M:%S')}")
print(f"Target Time (+15 min): {target_time.strftime('%H:%M:%S')}")
now = datetime.now(local_tz)
time_difference = target_time.replace(tzinfo=None) - now.replace(tzinfo=None)
# Get the total number of seconds as a floating-point number
sleep_seconds = time_difference.total_seconds()

print(f"Current time: {now}")
print(f"Target time: {target_time}")
print(f"Pausing for {sleep_seconds:.2f} seconds until target time...")
time.sleep(sleep_seconds)
print("Resuming execution. Current time is now:", datetime.now(local_tz))
tapo = Tapo(host, "admin", password_cloud, password_cloud, printDebugInformation=False)
tapo.setDayNightMode("on")
print("night mode is now: "+ tapo.getDayNightMode())
