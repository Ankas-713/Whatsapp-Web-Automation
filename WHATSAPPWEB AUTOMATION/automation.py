
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
message = input("Enter the message you want to send : ")
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 100)
search_box = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]')))
list_of_contacts = []
n = int(input("Enter the number of contacts you want to send message to : "))
for i in range(n):
    s = input("Enter the name of contact " + str((i + 1)) + " : ")
    list_of_contacts.append(s)
for i in list_of_contacts:
    search_box.send_keys(i)
    search_box.send_keys(Keys.ENTER)
    chatbox = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
    chatbox.send_keys(message)
    chatbox.send_keys(Keys.ENTER)

