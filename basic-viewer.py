from selenium import webdriver
from time import sleep
import requests

driver1 = webdriver.Chrome(executable_path="C:\\Users\\Utente\\Downloads\\chromedriver.exe")
driver2 = webdriver.Chrome(executable_path="C:\\Users\\Utente\\Downloads\\chromedriver.exe")
driver3 = webdriver.Chrome(executable_path="C:\\Users\\Utente\\Downloads\\chromedriver.exe")

driver1.get(URL)
driver2.get(URL)
driver3.get(URL)

a = 1
for a in range(100):
	driver1.refresh()
	driver2.refresh()
	driver3.refresh()
	print("Refresh: ", a)
	if(a % 10 == 0):
		print("Stopping for 10 seconds")
		sleep(10)

# Still to update. Do not use this version
