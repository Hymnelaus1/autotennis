from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

##Login kismi
driver.get("https://online.spor.istanbul/uyegiris")

driver.find_element(By.ID, "txtTCPasaport").send_keys("19784256664") 
driver.find_element(By.ID, "txtSifre").send_keys("06841297")        

driver.find_element(By.ID, "btnGirisYap").click()

#pop uplari ins kapayacak şuankine göre yaptim salaklar id değişmezse yeni pop-up için de çalışır static

try:
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "closeModal"))
    ).click()
    print("Pop-up kapatıldı.")
except:
    print("Pop-up görünmedi.")

#tesis secimi idleri tenis ve bostanci icin eger baska bir sey icin yapılacaksa elementsden idleri cekilmeli
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "contacttab6"))
).click()
print('test1')

Select(driver.find_element(By.ID, "ddlKiralikBransFiltre")).select_by_value("59b7bd71-1aab-4751-8248-7af4a7790f8c")
print('test2')

Select(driver.find_element(By.ID, "ddlKiralikTesisFiltre")).select_by_value("bdef460a-c8b1-49de-9c5e-666d622b9458")
print('test3')

search_button = driver.find_element(By.ID, "pageContent_ucUrunArama_lbtnKiralikAra")
driver.execute_script("arguments[0].click();", search_button)
print('test4') ## app aprroved to this step after that i am going to reserve a court but there is some sms specific problems i am gonna solve it later. see ya
target_button_id = "pageContent_rptList_rpChild_3_lbRezervasyon_3"

WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, target_button_id))
    )
rezervasyon_button = driver.find_element(By.ID, target_button_id)
driver.execute_script("arguments[0].click();", rezervasyon_button)
WebDriverWait(driver, 10).until(EC.alert_is_present())
driver.switch_to.alert.accept()
time.sleep(5)

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "rblKiralikTenisSatisTuru_1")))
radio_button = driver.find_element(By.ID, "rblKiralikTenisSatisTuru_1")
driver.execute_script("arguments[0].click();", radio_button)
print("🎯 Satış türü seçildi.")
time.sleep(3)

WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "pageContent_lbtnSepeteEkle"))
    )
sepete_ekle_btn = driver.find_element(By.ID, "pageContent_lbtnSepeteEkle")
driver.execute_script("arguments[0].click();", sepete_ekle_btn)

time.sleep(10)

