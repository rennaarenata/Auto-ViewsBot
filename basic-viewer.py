# ----------------------- # Imports
import argparse
# ----------------------- # Froms
from selenium import webdriver
from time import sleep
# ----------------------- # End

def argscheck(v, d, s):
	exitm = False
	if(v == None):
		print("Define -v parameter")
		exitm = True
	if(d == None):
		print("Define -d parameter")
		exitm = True
	if(s == None):
		print("Define -s parameter")
		exitm = True
	if(exitm == True):
		print("Exiting...")
	
# ----------- # ARGS handling
parser = argparse.ArgumentParser(description="Youtube-AutoViewer by Rennaarenata (using this tool you may encounter a permanent ban from YouTube)")
parser.add_argument("url", help="The URL of the video.")
parser.add_argument("-v", "--views", help="The approximate number of views you want to get (default 40), do not exceed 100 views in one hour.", default=40)
parser.add_argument("-d","--delay", help="Every how many requests stop the bot. - default: 20", default=20)
parser.add_argument("-s","--seconds", help="How many seconds the bot has wait every {-d} request(s) - default: 15", default=15)

args = parser.parse_args()
url = args.url
views = args.views
delay = args.delay
seconds = args.seconds

print("[+]Starting...")
print("[i]Views: " + str(views))
print("[i]Delay: " + str(delay))
print("[i]Seconds: " + str(seconds))
if (int(views) >= 100 and int(seconds) < 15):
	print("[!!]Warning: You are trying to get more than 100 views, this may result in a permanent ban from YouTube. Please consider lowering the number of views or increasing the seconds (-s).")
	sleep(10)


# ------------ # Check
argscheck(views, delay, seconds)

options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")

# ------------ # Driver Stuff
driver1 = webdriver.Chrome(executable_path="PATHTOCHROMEDRIVER.EXE", service_log_path="chromedriver.log", options=options)
driver2 = webdriver.Chrome(executable_path="PATHTOCHROMEDRIVER.EXE", service_log_path="chromedriver.log", options=options)
driver3 = webdriver.Chrome(executable_path="PATHTOCHROMEDRIVER.EXE", service_log_path="chromedriver.log", options=options)
driver4 = webdriver.Chrome(executable_path="PATHTOCHROMEDRIVER.EXE", service_log_path="chromedriver.log", options=options)
print("[*]Sleeping for 6 seconds...Accept cookies in the meantime.")

driver1.get(url)
driver2.get(url)
driver3.get(url)
driver4.get(url)
sleep(6)


for a in range(int(views) + 1):
	driver1.refresh()
	driver2.refresh()
	driver3.refresh()
	driver4.refresh()
	print(f"Refresh: {a}")
	if(a % int(delay) == 0):
		print(f"Sleeping for {seconds} seconds")
		sleep(int(seconds))

print(f"Enjoy!\n")
driver1.close()
driver2.close()
driver3.close()
driver4.close()
