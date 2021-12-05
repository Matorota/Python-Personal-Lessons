from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter import *
import time

URL ="https://dienynas.tamo.lt/Prisijungimas/Login?logout=true"
DRIVER_PATH = r"C:\Users\Admin\Desktop\chromedriver.exe"

window = Tk()
window.title("Tamo Login")
window.minsize(width=400, height=200)

def button_used():

    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(URL)

    tamo_username = driver.find_element(By.XPATH, '//*[@id="UserName"]')
    tamo_username.send_keys(username_input.get())

    tamo_password = driver.find_element(By.XPATH, '//*[@id="Password"]')
    tamo_password.send_keys(password_input.get())

    tamo_button = driver.find_element(By.XPATH, '//*[@id="main_form"]/div/div[3]/a')
    tamo_button.click()

    tamo_namuDarbai = driver.find_element(By.XPATH, '//*[@id="s_menu"]/ul/li[6]/ol/li[4]')
    tamo_namuDarbai.click()

    URL_NAMU_DARBAI = 'https://dienynas.tamo.lt/Darbai/NamuDarbai'
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(URL_NAMU_DARBAI)

    headings = driver.find_elements_by_xpath('//*[@id="namu_darbai_artimiausi"]')
    for heading in headings:
        title = heading.find_elements_by_xpath('//*[@id="namu_darbai_artimiausi"]/div[1]/div[3]/div[2]')
        namu_darbai = heading.find_elements_by_xpath('//*[@id="namu_darbai_artimiausi"]/div[1]/div[4]/div/div')


        #< a href = "/Darbai/NamuDarbai" > Namųdarbai < / a >
        print(namu_darbai, "-")
        for t in title:
             print('titles:', t.text)

    time.sleep(100)

label = Label(text="Tamo n.d", font=("Arial", 14, "bold"))
label.pack()

username_input = Entry(width=30)
username_input.insert(END, string="Insert Username")
username_input.pack()

password_input = Entry(width=30)
password_input.insert(END, string="Insert password")
password_input.pack()

button = Button(text="Submit", command=button_used)
button.pack()

window.mainloop()
