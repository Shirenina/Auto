from selenium import webdriver
from selenium.webdriver.common.by import By                  

driver = webdriver.Chrome('C:\\chromedriver.exe')

driver.implicitly_wait(10)

driver.get('https://mail.yandex.ru/')
enter_btn = driver.find_element(By.XPATH, '//*[@id="index-page-container"]/div/div[2]/div/div/div[4]/a[2]').click()

post = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div/div[1]/form/div[1]/div[1]/button').click()

login = driver.find_element(By.XPATH, '//*[@id="passp-field-login"]')
login.clear()
login.send_keys("e.a.shirenina")

enter_btn2 = driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').click()

password = driver.find_element(By.XPATH, '//*[@id="passp-field-passwd"]')
password.clear()
password.send_keys("Yandex1234567")

enter_fin = driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').click()

write_btn = driver.find_element(By.XPATH, '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[3]/nav/div[3]/div/div/div/a').click()

to_whom = driver.find_element(By.XPATH, '//*[@id="js-apps-container"]/div[2]/div[10]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[1]/div/div/div/div/div')
to_whom.clear()
to_whom.send_keys("e.a.shirenina@yandex.ru")

theme = driver.find_element(By.XPATH, '//*[@id="js-apps-container"]/div[2]/div[10]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/div[3]/div/div/input')
theme.clear()
theme.send_keys('Automation')

text = driver.find_element(By.XPATH, '//*[@id="cke_1_contents"]/div/div')
text.clear()
text.send_keys("Привет!")

send_btn = driver.find_element(By.XPATH, '//*[@id="js-apps-container"]/div[2]/div[10]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div[1]/button').click()

update_btn = driver.find_element(By.XPATH, '//*[@id="js-apps-container"]/div[2]/div[7]/div/div[3]/nav/div[3]/div/div/div/button').click()