from selenium import webdriver
from time import sleep
import requests
import argparse

def check(v, d, s):
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
	
		
parser = argparse.ArgumentParser(description="Youtube-AutoViewer by Rennaarenata (using this tool you may encounter a permanent ban from YouTube)")
parser.add_argument("url", help="The URL of the video")
parser.add_argument("-v", "--views", help="The approximate number of views you want to get (default 40)", default=40)
parser.add_argument("-d","--delay", help="Every how many requests stop the bot", default=20)
parser.add_argument("-s","--seconds", help="How many seconds to wait for each {-d} requests", default=15)

args = parser.parse_args()
url = args.url
views = args.views
delay = args.delay
seconds = args.seconds

check(views, delay, seconds)

driver1 = webdriver.Chrome(executable_path="PATHTOCHROMEDRIVER.EXE")
driver2 = webdriver.Chrome(executable_path="PATHTOCHROMEDRIVER.EXE")
driver3 = webdriver.Chrome(executable_path="PATHTOCHROMEDRIVER.EXE")

driver1.get(url)
driver2.get(url)
driver3.get(url)

sleep(6)

print("Sleeping for 6 seconds...")
a = 1
a1 = a+1

for a in range(int(views)):
	driver1.refresh()
	driver2.refresh()
	driver3.refresh()
	print("Refresh Number: ", a1)
	if(a % int(delay) == 0):
		print(f"Stopping for {seconds} seconds")
		sleep(int(seconds))
