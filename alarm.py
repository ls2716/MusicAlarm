import datetime
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from config import user, password

class Alarm():

    def __init__(self,alarm_hour,alarm_minute):
        self.login,self.password = user, password
        self.now = datetime.datetime.now()
        self.alarm_hour = alarm_hour
        self.alarm_minute = alarm_minute
        self.already_played = False
        self.alarm_time = alarm_hour*60+alarm_minute
        print("Alarm set at %d:%d"%(alarm_hour,alarm_minute))

    def Evaluate(self):
        now = datetime.datetime.now()
        print("Evaluating:",now)

        now_time = now.hour*60+now.minute
        if (now_time==self.alarm_time-2 and (not self.already_played)):
            self.SetupBluetooth()
            self.Play("MusicAlarm")
            self.already_played=True

    def SetupBluetooth(self):
        print("Setting up bluetooth")
        subprocess.call([r'C:\Users\Łukasz\Documents\MusicAlarm\connect.bat'])


    def Play(self,playlist):
        driver = webdriver.Chrome()
        driver.get("https://open.spotify.com/browse/featured")
        assert "Spotify" in driver.title
        time.sleep(2)
        elem = driver.find_element_by_xpath(\
        '//*[@id="main"]/div/div[5]/div[1]/nav/div[2]/div/p[2]/button')
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath(\
        '//*[@id="app"]/body/div[1]/div[2]/div/div[2]/div/a')
        elem.click()

        elem = driver.find_element_by_id("email")
        elem.send_keys(self.login)
        elem = driver.find_element_by_id("pass")
        elem.send_keys(self.password)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        elem = driver.find_element_by_xpath(\
        '//span[text()="MusicAlarm"]')
        elem.click()
        time.sleep(4)
        elem = driver.find_element_by_xpath(\
        '//div[text()="Macho"]')
        action_chain = ActionChains(driver)
        while True:
            now = datetime.datetime.now()
            now_time = now.hour*60+now.minute
            if (now_time>=self.alarm_time):
                action_chain.double_click(elem).perform()
                self.already_played=True
                break
            time.sleep(0.5)
        

if __name__ == "__main__":
    a = Alarm(7,15)

    while True:
        a.Evaluate()
        a.already_played=False
        time.sleep(15)
