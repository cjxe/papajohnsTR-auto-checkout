from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
#from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe', options=chrome_options)

# GET
URL ='https://www.papajohns.com.tr' #1
menuAPI = '/menu' #3
promotionsAPI = '/#promosyonlar' #3.1
pizzasAPI = '/#pizzalar' #3.2
transac_confirmAPI = '/siparis-onay' #7

# POST
loginAPI = '/giris-yap' #2
add_to_basketAPI = '/sepete-ekle' #5
basketAPI = '/sepet' #6


EMAIL = input('Email adresini gir: ')
PASSWORD = input('Sifreni gir: ')
PRICE = input('Urunun fiyatini gir: ')



def siteye_baglan():
    """
    Siteye baglanir.
    """
    try:
        driver.get(URL+loginAPI)
        print('[BASARILI] "papajohns.com.tr" sitesine baglanildi.')
    except Exception as e:
        print('[HATA] "papajohns.com.tr" sitesine erisilemiyor!')
        print('Hata aciklamasi: ', e)    


def ilkSenHaberdarOl_pencere_kapa():
    """
    "İlk sen haberdar ol!" penceresini kapatir.
    """
    try: 
        driver.find_element_by_id("denyNotifications").click()
        print('[BASARILI] "DAHA SONRA" tusuna basildi.')
    except Exception as e:
        print('[HATA] "İlk sen haberdar ol!" ekrani bulunamadi!')
        print('Hata aciklamasi: ', e)


def tatli_pencere_kapa():
    """
    "Tatli" penceresini kapatir.
    """
    try:
        driver.find_element_by_xpath('//body/div[@id="page-wrapper"]/div[@class="popup-window"]/a').click()
        print('[BASARILI] "KAPAT" tusuna basildi.')
    except Exception as e:
        print('[HATA] "KAPAT" tusu bulunamadi!')
        print('Hata aciklamasi: ', e)


def email_gir():
    """
    Email kutusuna emailinizi girer.
    """
    try:
        driver.find_element_by_xpath('//body/div[@id="page-wrapper"]/div[@id="pages"]/section[@class="container maincontainer home"]/div[@class="right-side"]/div[@class="white-block padding-default color_brown"]/div[@class="row"]/div[@id="pageCenter"]/form[@id="loginPPageForm"]/div[@class="row"]/div[@class="col-xs-12 col-sm-8"]/input[@id="email"]').send_keys(EMAIL)
        print('[BASARILI] "Email" kutusuna giris yapildi.')
    except Exception as e:
        driver.find_element_by_id("email").send_keys(EMAIL)  # garanti email finder
        print('[HATA] "Email" girilecek kutu bulunamadi!')
        print('Hata aciklamasi: ', e)


def sifre_gir():
    """ 
    Sifre kutusuna sifrenizi girer.
    """
    try:
        driver.find_element_by_xpath('//body/div[@id="page-wrapper"]/div[@id="pages"]/section[@class="container maincontainer home"]/div[@class="right-side"]/div[@class="white-block padding-default color_brown"]/div[@class="row"]/div[@id="pageCenter"]/form[@id="loginPPageForm"]/div[@class="row"]/div[@class="col-xs-12 col-sm-6"]/input[@id="password"]').send_keys(PASSWORD)
        print('[BASARILI] "Sifre" kutusuna giris yapildi.')
    except Exception as e:
        driver.find_element_by_id("password").send_keys(PASSWORD) # garanti password finder    HANDLINGI DUZELT!
        print('[HATA] "Sifre" girilecek kutu bulunamadi!')
        print('Hata aciklamasi: ', e)


def login_button_bas():
    """ 
    Giris yap butonuna basar.
    """
    try:        
        driver.find_element_by_id("submit").click()
        print('[BASARILI] Hesaba giris yapildi.')
    except Exception as e:
        print('[HATA] Hesaba giris yapilamadi!')
        print('Hata sebebi: ', e)   


#driver.find_element_by_xpath('//p[@class="font_size_12"][contains(text(), "Call of Duty Menü sipariş ver, beta sürümüne ücretsiz katıl")]/../../div[@class="col-xs-4 col-sm-1 col-md-1 no-paddings col-xs-padding-right"]/a').click()
def urun_bul():
    """ 
    Istenilen urunu bulur.
    """
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f'//span[@class="opensanscondensed visible-xs bold color_green pull-right"][contains(text(), "{PRICE} TL")]/../../div[@class="col-xs-4 col-sm-1 col-md-1 no-paddings col-xs-padding-right"]/a')))
        driver.find_element_by_xpath(f'//span[@class="opensanscondensed visible-xs bold color_green pull-right"][contains(text(), "{PRICE} TL")]/../../div[@class="col-xs-4 col-sm-1 col-md-1 no-paddings col-xs-padding-right"]/a').click()
        print(f"[BASARILI] {PRICE} TL fiyatli urun bulundu.")
    except Exception as e:
        print(f"[HATA] {PRICE} TL fiyatli urun bulunamadi!")
        print('Hata aciklamasi: ', e)


def sepete_ekle():
    """ 
    Istenilen urunu sepete ekler.
    """
    try: 
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f'//*[contains(text(), "SEPETE EKLE")][@class="btn btn-red btn-block"]')))
        driver.find_element_by_xpath('//*[contains(text(), "SEPETE EKLE")][@class="btn btn-red btn-block"]').click()
        print(f"[BASARILI] {PRICE} TL fiyatli urun sepete eklendi.")
    except Exception as e:
        print(f"[HATA] {PRICE}'li urun sepete eklenilemedi!")
        print('Hata aciklamasi: ', e)


def satinAl_button_bas():
    """ 
    Satin alma butonuna basar.
    """
    try:        
        driver.find_element_by_id("submit").click()
        print('[BASARILI] Sepette "satin al" tusuna basildi.')
    except Exception as e:
        print('[HATA] Sepette "satin al" tusuna basilamadi!')
        print('Hata sebebi: ', e)  



siteye_baglan()
input("Baslamak icin ENTER'a bas")
start_time = time.time()
ilkSenHaberdarOl_pencere_kapa()
tatli_pencere_kapa()
email_gir()
sifre_gir()
login_button_bas()
#driver.wait_for_element_to_be_clickable()  #https://www.youtube.com/watch?v=uA9T4YL1pLs   2#https://www.youtube.com/watch?v=U6gbGk5WPws
#time.sleep(0.3)
urun_bul()
#time.sleep(0.3)   # birazcik daha hizli
sepete_ekle()
time.sleep(0.2)
#satinAl_button_bas()
elapsed_time = time.time() - start_time
print(f'Toplam islem suresi: {float(round(elapsed_time,2))} saniye')









