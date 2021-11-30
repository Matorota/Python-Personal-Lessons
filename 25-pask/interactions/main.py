from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL ="https://www.python.org/"
DRIVER_PATH = r"C:\Users\matas\Desktop\chromedriver.exe"


driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)

query_field = driver.find_element(By.NAME, "q")
query_field.send_keys("for")
query_field.send_keys(Keys.ENTER)

titles = driver.find_elements(By.CSS_SELECTOR, "ul.link-recent-events li h3")
print(titles)

for title in titles:
    print(title.text)

