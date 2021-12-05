from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
import time

URL ="https://www.google.com/?hl=lt"
DRIVER_PATH = r"C:\Users\Admin\Desktop\chromedriver.exe"



window = Tk()
window.title("Scrapper")
window.minsize(width=400, height=200)


def button_used():

    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(URL)

    search_button = driver.find_element(By.ID,"L2AGLb")
    search_button.click()

    google_search = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    google_search.send_keys(Search_input.get())

    google_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
    google_button.click()

    headings = driver.find_elements_by_xpath('//div[@class= "g"]')
    for heading in headings:
        title = heading.find_elements_by_tag_name('h3')
        for t in title:
             print('titles:', t.text)

    time.sleep(100)



label = Label(text="Scrapper", font=("Arial", 14, "bold"))
label.pack()

Search_input = Entry(width=30)
Search_input.insert(END, string="Insert Search")
Search_input.pack()

button = Button(text="Submit", command=button_used)
button.pack()

window.mainloop()



