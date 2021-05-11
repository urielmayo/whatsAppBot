from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://web.whatsapp.com/')

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#side > div.SgIJV > div > label > div > div._2_1wd.copyable-text.selectable-text')))
search_field = driver.find_element_by_css_selector('#side > div.SgIJV > div > label > div > div._2_1wd.copyable-text.selectable-text')
search_field.clear()

search_field.send_keys("ABCD")

WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#side > div.SgIJV > div > span > button > span')))

chat_button = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[5]').click()

text_field = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

text_field.clear()
text_field.send_keys('This is the python bot')

send_button = driver.find_element_by_css_selector('#main > footer > div.vR1LG._3wXwX.copyable-area > div:nth-child(3) > button > span')
send_button.click()