from selenium import webdriver
import time,os,random


class chaoxing:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.domain = 'https://i.chaoxing.com/'
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument('log-level=3')
        options.add_experimental_option("detach", True)
        options.add_experimental_option('prefs', {'download.default_directory': os.path.realpath(__file__)[:-7]+'Downloads'})   #下载路径
        self.driver = webdriver.Chrome(executable_path=os.path.dirname(__file__)+'/chromedriver.exe',options=options)
        self.driver.implicitly_wait(10)

    def login(self):
        self.driver.get(self.domain)
        self.driver.find_element_by_xpath('//*[@id="phone"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        time.sleep(1)

    def crawl(self):
        link = input("Plz paste the link here: ")
        self.driver.get(link)
        self.driver.switch_to.frame(0)
        li = self.driver.find_elements_by_xpath('//*/iframe')
        li = {i.get_attribute('objectid') for i in li}
        for i in li:
            self.driver.get('https://cs-ans.chaoxing.com/download/' + i)
            time.sleep(1)

    def run(self):
        self.login()
        self.crawl()


if __name__ == "__main__":
    chaoxing("","").run()
