from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.metric-conversions.org/")
textbox_from = driver.find_element_by_name("queryFrom")
textbox_to = driver.find_element_by_name("queryTo")
textbox_from.clear()
textbox_to.clear()

textbox_from.send_keys("Meters")
time.sleep(0.5)

textbox_to.send_keys("Feet")   
time.sleep(1.0)

textbox_value = driver.find_element_by_class_name("argument") 
textbox_value.send_keys("20")  
textbox_value.send_keys(Keys.RETURN)
time.sleep(3)

driver.quit()
