import random
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.common.keys import Keys
import pandas as pd

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None

driver = webdriver.Firefox()

link = "https://www.naukri.com/information-technology-jobs"
total_pages_to_scrap = 10



skills = {}
job_url = []


for x in range(1,total_pages_to_scrap+1):
	print("**********************************************\n page {} \n **********************************************".format(x))
	if x==1:
		browse = link
	else:
		browse = link+"-"+str(x)
	driver.get(browse)
	wait = ui.WebDriverWait(driver, 10)
	wait.until(page_is_loaded)
	page_url=driver.find_elements_by_xpath("//a[@class='content']")
	page_links = [lk.get_attribute("href") for lk in page_url]

	for lnk in page_links:
		driver.get(lnk)
		wait = ui.WebDriverWait(driver, 10)
		wait.until(page_is_loaded)

		try:
			skll = driver.find_elements_by_class_name("hlite")
			skill_lst = [lst.text for lst in skll]
			skill_lst = [ll.lower() for ll in skill_lst]
			for dat in skill_lst:
				if dat in skills:
					skills[dat]+=1
				else:
					skills.update({dat:1})
			print(skills)
		except:
			pass

df = pd.DataFrame.from_dict(skills, orient="index")
df.to_csv("stat.csv")
print("finished!")




