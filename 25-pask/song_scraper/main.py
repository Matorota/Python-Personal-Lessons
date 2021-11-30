from selenium import webdriver
from selenium.webdriver.common.by import By

URL ="https://www.insider.com/best-songs-every-year-2017-8"
DRIVER_PATH = r"C:\Users\matas\Desktop\chromedriver.exe"


driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(URL)

#get_song_btn = driver.find_elements(By.CLASS_NAME, "slide-title-text")
#get_song_btn.click()

song = driver.find_elements(By.CSS_SELECTOR, "ul.slide-title-text ")
print(song)

#for songe in song:
#    print(songe.text)


