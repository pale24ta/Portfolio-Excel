from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date

# Funcion para descargar el archivo .dat desde el navegador

def donwload_file():
    url = 'https://www.bolsadecaracas.com/diario-de-la-bolsa/#'
    today = date.today()

    # creamos los datos necesario
    day,mouth,year = today.
    # cargamos el driver del navegador
    driver = webdriver.Chrome()


    driver.get(url)
    assert "el diario de la bolsa" in driver.title

    info_necesaria = driver.find_element(By.NAME,'')

donwload_file()