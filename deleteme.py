from selenium import webdriver
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.support.wait import WebDriverWait

PROFILE_PATH = None
myprofile = FirefoxProfile(PROFILE_PATH)
driver = webdriver.Firefox(myprofile)
driver.implicitly_wait(10) #Setting a max ten second wait time
driver.get("https://myactivity.google.com/myactivity")
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Item view'])[2]/following::a[1]").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Delete by date'])[1]/following::span[1]").click()
driver.find_element_by_id("select_option_9").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Before'])[1]/following::button[1]").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Cancel'])[1]/following::button[1]").click()