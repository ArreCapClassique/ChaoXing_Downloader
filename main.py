from selenium import webdriver
import time,os,re


def initialize():
    username = driver.find_element_by_id('unameId')
    password = driver.find_element_by_id('passwordId')
    numcode = driver.find_element_by_id('numcode')
    login = driver.find_element_by_class_name('zl_btn_right')
    username.send_keys('')                           #输入用户名
    password.send_keys('')                           #输入密码
    numcode.send_keys(input('Plz input the captcha here: '))    #在【Python终端】输入验证码
    time.sleep(1)
    login.click()

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {'download.default_directory': os.path.realpath(__file__)[:-7]+'Downloads'})   #下载路径
link = input('Plz copy the link here: ')
driver = webdriver.Chrome(executable_path=os.path.realpath(__file__)[:-7]+'chromedriver.exe',chrome_options=options)
driver.get(link)
time.sleep(1)
initialize()
driver.switch_to.frame('iframe')
li = driver.find_elements_by_xpath('//*/iframe')
li = [i.get_attribute('objectid') for i in li]
for i in li :
    try:
        driver.get('http://d0.ananas.chaoxing.com/download/'+i)
        print('successfully downloaded')
    except Exception as ex:
        print(ex)
    finally:
        time.sleep(1)