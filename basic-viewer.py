# ----------------------- # Imports
import requests
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
parser.add_argument("-d","--delay", help="Every how many requests stop the bot.", default=20)
parser.add_argument("-s","--seconds", help="How many seconds the bot has wait every {-d} request(s)", default=15)

args = parser.parse_args()
url = args.url
views = args.views
delay = args.delay
seconds = args.seconds

# ------------ # Check
argscheck(views, delay, seconds)

# ------------ # Driver Things
driver1 = webdriver.Chrome(executable_path="PATHTOCHROMEDRIVERE")
driver2 = webdriver.Chrome(executable_path="PATHTOCHROMEDRIVERE")
driver3 = webdriver.Chrome(executable_path="PATHTOCHROMEDRIVERE")
driver4 = webdriver.Chrome(executable_path="PATHTOCHROMEDRIVERE")

driver1.get(url)
driver2.get(url)
driver3.get(url)
driver4.get(url)

print("Sleeping for 6 seconds...")
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