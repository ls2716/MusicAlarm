from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from config import user, password
driver = webdriver.Chrome()
driver.get("https://open.spotify.com/browse/featured")
assert "Spotify" in driver.title
time.sleep(1)
elem = driver.find_element_by_xpath(\
'//*[@id="main"]/div/div[5]/div[1]/nav/div[2]/div/p[2]/button')
elem.click()
time.sleep(2)
elem = driver.find_element_by_xpath(\
'//*[@id="app"]/body/div[1]/div[2]/div/div[2]/div/a')
elem.click()

elem = driver.find_element_by_id("email")
elem.send_keys(user)
elem = driver.find_element_by_id("pass")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_xpath(\
'//span[text()="MusicAlarm"]')
elem.click()
elem = driver.find_element_by_xpath(\
        '//div[text()="Immigrant Song - Remaster"]')
action_chain = ActionChains(driver)
action_chain.double_click(elem).perform()
