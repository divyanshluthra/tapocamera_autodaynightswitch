# tapocamera_autodaynightswitch
The tapo cameras dont automatically switch to day and night mode due to street light and other external conditions, so this python script can be edited as per your location(edit longitude latitude and time zone in the script) so that day and night mode can be switched on based on sunrise and sunset times locally.  
You can schedule the python script from cron(for mac) of scheduler for windows in an always running system(or raspberry pi) for 4.30AM and  4.30PM for dawn script and dusk script, and it will wait for the time between 4.30 and the sunrise/sunset time (+-15 mins) to run the script to switch day/night mode on.    
**Dependencies:**    
Python 3.13 ONLY(not latest)  
install Tapo using: pip3 install tapo   (or pip install tapo)  
Sun: pip3 install sun  
pip3 install datetime  
pip3 install timedelta    

Then put your Tapo CLOUD password(not local/RTSP account) in the script.  
Put LAN Host IP address of the tapo camera.  
Put latitude, longitude of your location.  
Put timezone from this list : https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568    
test it using your python 3.13 installation, i did in this way on mac:  
   /Users/myuser/Downloads/tapopython/.venv/bin/python /Users/myuser/Downloads/tapopython/tapodusk.py;  
   /Users/myuser/Downloads/tapopython/.venv/bin/python /Users/myuser/Downloads/tapopython/tapodawn.py;  
then schedule them in crontab (linux/mac) or windows using scheduler for  4.30AM and  4.30PM.  
