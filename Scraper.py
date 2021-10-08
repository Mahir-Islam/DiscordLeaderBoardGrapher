from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys as k
from selenium.webdriver.common.by import By
from selenium import webdriver as wd
import time
from webdriver_manager.chrome import ChromeDriverManager

import Grapher as GP



def SCRAPE(URL_ID, INDEX):
	"""PATH = "C:\Program Files (x86)\chromedriver.exe"

	driver = wd.Chrome(PATH)"""
	driver = wd.Chrome(ChromeDriverManager().install())


	driver.get(f"https://mee6.xyz/leaderboard/{URL_ID}")

	index = {}
	msgDex= []
	expDex= []
	"""
	index is a dictionary with each username having its ranking as the value
	msgDex is the list of number of messages
	expDex is the list of experience scores
	"""

	try:

		#title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='sc-1kdz257-4 jpTyHV']"))).text

		main = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "leaderboardPlayersList")))
		#the driver will wait 5 seconds, then it will search for an element of id "leaderboardPlayersList"

		title = driver.find_element(By.XPATH, "//div[@class='sc-1kdz257-4 jpTyHV']").text
		user = main.find_elements_by_class_name("leaderboardPlayer")

		msgDex = [0 for x in range(0,INDEX)]
		expDex = [0 for x in range(0,INDEX)]

		for x in range(0,INDEX):
			rank = user[x].find_element_by_class_name("leaderboardRank").text
			name = user[x].find_element_by_class_name("leaderboardPlayerUsername").text

			score= user[x].find_elements_by_class_name("leaderboardPlayerStatValue")
			msgs = str(GP.PROCESS(score[0].text))
			exp  = str(GP.PROCESS(score[1].text))

			index[name] = int(rank)
			msgDex[x] = int(msgs)
			expDex[x] = int(exp)

	finally:
		driver.quit()

	return [index, msgDex, expDex, title]

