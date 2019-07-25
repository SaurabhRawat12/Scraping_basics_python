from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path = r'E:\Downloads\Compressed\chromedriver.exe')
driver.get("https://www.linkedin.com/")

sleep(5)
driver.maximize_window()

#driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

signin = driver.find_element_by_class_name('nav__button-secondary')
signin.click()
sleep(5)

email = driver.find_element_by_xpath('//*[@id="username"]')
email.send_keys("Saurabhrawat125@gmail.com")
sleep(3)

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys("")
sleep(3)

login = driver.find_element_by_xpath('//*[@id="app__container"]/main/div/form/div[3]/button')
login.click()
sleep(3)
