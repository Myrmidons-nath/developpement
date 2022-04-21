from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://youtu.be/6a-FnIqM0rI")
time.sleep(6)
# sb = driver.find_element_by_class_name("ytp-play-button ytp-button").click()
print("okk")




