from selenium import webdriver
from selenium.webdriver.common.by import By


def get_price():

    URL = "https://www.1a.lt/c/telefonai-plansetiniai-kompiuteriai/telefonai-ismanieji-laikrodziai/mobilieji-telefonai/2ps"
    DRIVER_PATH = r"C:\Users\Admin\Desktop\chromedriver.exe"

    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(URL)

    kaina = driver.find_element(By.XPATH, '    / html / body / div[2] / div[3] / div / div[2] / div[3] / div[4] / div / div[1] / div[2] / div[1] / div / span / \
      span[1]')
    return {"Kaina kompo": kaina}
