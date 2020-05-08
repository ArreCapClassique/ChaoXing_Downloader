from selenium import webdriver
import time,os,re,chaojiying

def captcha_discern():
    client = chaojiying.Chaojiying_Client('','','')     #依次输入超级鹰平台的 用户名，密码，软件ID
    with open('captcha.png', 'rb') as f:
        image = f.read()
        captcha = client.PostPic(image,1902)['pic_str']
    print('captcha discerned: '+captcha)
    return captcha

def login():
    username = driver.find_element_by_id('unameId')
    password = driver.find_element_by_id('passwordId')
    numcode = driver.find_element_by_id('numcode')
    button = driver.find_element_by_class_name('zl_btn_right')
    numVercode = driver.find_element_by_xpath('//*/img')
    numVercode.screenshot('captcha.png')
    username.send_keys('')                           #输入超星平台用户名
    password.send_keys('')                           #输入密码
    numcode.send_keys(captcha_discern())
    os.remove('captcha.png')
    time.sleep(1)
    button.click()

def downloader():
    if 'studentstudy' in link:
        driver.switch_to.frame('iframe')
        li = driver.find_elements_by_xpath('//*/iframe')
    elif 'coursedata' in link:
        li = driver.find_elements_by_xpath('//*/tr')
    li = [i.get_attribute('objectid') for i in li]
    for i in li :
        try:
            driver.get('http://d0.ananas.chaoxing.com/download/'+i)
            print('successfully downloaded '+'(ID: '+i+')')
        except Exception as ex:
            print(ex)
        finally:
            time.sleep(1)

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'download.default_directory': os.path.realpath(__file__)[:-7]+'Downloads'})   #下载路径
    link = input('Plz paste the link here: ')
    driver = webdriver.Chrome(executable_path=os.path.realpath(__file__)[:-7]+'chromedriver.exe',chrome_options=options)
    driver.get(link)
    time.sleep(1)
    login()
    print('successfully broke in')
    downloader()
