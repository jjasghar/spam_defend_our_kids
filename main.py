from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from faker import Faker
import os
from os.path import exists

file_exists = os.path.exists('chromedriver')
if file_exists:
    PATH = "./chromedriver"
else:
    print("#######")
    print("You need to install the ChromeDriver: https://chromedriver.chromium.org/downloads before continuing")
    print("#######")
    exit(1)
driver = uc.Chrome(use_subprocess=True)
fake = Faker()

wait = WebDriverWait(driver, 20)
driver.get("https://defendkidstx.com/#popup")

name = fake.name()
email = fake.free_email()
address = fake.address()
lorem = fake.paragraph(nb_sentences=15)


# name
wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/form/p[1]/input'))).send_keys(name)
# email address
wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/form/p[2]/input'))).send_keys(email)
# address 
wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/form/p[3]/input'))).send_keys(address)
# lorem
wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/form/p[4]/textarea'))).send_keys(lorem)
wait.until(EC.visibility_of_element_located((By.NAME, 'et_builder_submit_button'))).click()

print(f"I just sent {name} at {email} with the address of {address}")

