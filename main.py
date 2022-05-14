from selenium import webdriver
import time,os,random


class chaoxing:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--hide-scrollbars')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("detach", True)
        options.add_experimental_option('prefs', {
            'profile.default_content_settings.popups': 0,
            'download.default_directory': os.path.realpath(__file__)[:-7]+'Downloads'})
        self.driver = webdriver.Chrome(
            executable_path = os.path.dirname(__file__)+'/chromedriver.exe',
            options = options)
        self.driver.implicitly_wait(10)
        self.driver.get('https://i.chaoxing.com/')
        self.driver.find_element_by_xpath('//*[@id="phone"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        time.sleep(1)
        print("Initialized")

    def login(self):
        self.driver.get(self.domain)
        self.driver.find_element_by_xpath('//*[@id="phone"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="pwd"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
        time.sleep(1)

    def DownloadFile(self):
        link = input("文件链接: ")
        self.driver.get(link)
        self.driver.switch_to.frame(0)
        li,lii = self.driver.find_elements_by_xpath('//*/iframe'), {}
        for i in li:
            try:
                lii[i.get_attribute('objectid')] = ast.literal_eval(i.get_attribute('data'))['name']
            except Exception as e:
                pass
        print("{} files detected".format(len(lii)))
        for k,v in lii.items():
            print("Downloading {}".format(v))
            self.driver.get('https://cs-ans.chaoxing.com/download/' + k)
            time.sleep(1)

    def run(self):
        self.login()
        self.crawl()


if __name__ == "__main__":
    chaoxing("","").run() #用户名,密码
