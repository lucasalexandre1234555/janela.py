from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome(executable_path="C:/Users/User/Desktop/chromedriver.exe")
# caso queira deixar na mesma pasta do seu código
# navegador = webdriver.Chrome(\"chromedriver.exe\")

navegador.get( "https://www.google.com/" )

# Passo 1: Pegar a cotação do Dólar
navegador.find_element( By.XPATH,
                        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input' ).send_keys(
    "cotação dólar" )

navegador.find_element( By.XPATH,
                        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input' ).send_keys( Keys.ENTER )

cotacao_dolar = navegador.find_element( By.XPATH,
                                        '//*[@id=\"knowledge-currency__updatable-data-column\"]/div[1]/div[2]/span[1]' ).get_attribute(
    "data-value" )
print( cotacao_dolar )

# Passo 2: Pegar a cotação do Euro
navegador.get( "https://www.google.com/" )
navegador.find_element( By.XPATH,
                        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input' ).send_keys(
    "cotação euro" )
navegador.find_element( By.XPATH,
                        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input' ).send_keys( Keys.ENTER )

cotacao_euro = navegador.find_element( By.XPATH,
                                       '//*[@id=\"knowledge-currency__updatable-data-column\"]/div[1]/div[2]/span[1]' ).get_attribute(
    "data-value" )
print( cotacao_euro )

# Passo 3: Pegar a cotação do Ouro
navegador.get( "https://www.melhorcambio.com/ouro-hoje" )

cotacao_ouro = navegador.find_element( By.XPATH, '//*[@id=\"comercial\"]' ).get_attribute( "value" )
cotacao_ouro = cotacao_ouro.replace( ",", "." )
print( cotacao_ouro )
navegador.quit()
