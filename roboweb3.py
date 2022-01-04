import time
import xlrd

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#cria arquivo para resultado ser escrito
arquivo = open('resultado.txt', 'w')


# chama o exe que abre o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://registro.br/")

#abre planilha do excel com nomes a consultar
planilha = xlrd.open_workbook(r'C:\Users\hlruf\OneDrive\Documentos\Bots Python\nomes.xls')
sheet = planilha.sheet_by_name('Plan1')
rows = sheet.nrows
colms = sheet.ncols

for curr_row in range(0, rows):
    #lê a celula da planilha
    x = sheet.cell_value(curr_row, 0)
    # faz a pesquisa
    search = driver.find_element(By.ID, "is-avail-field")
    time.sleep(2)
    search.clear()
    time.sleep(2)
    search.send_keys(x)
    time.sleep(2)
    search.send_keys(Keys.RETURN)
    time.sleep(2)

    #busca por negrito disponível ou não
    driver.find_element(By.XPATH, '/html/body/div/main/section/div[2]/div/p/span/strong')

    #escreve resultado em arquivo txt
    texto ="Domínio %s %s \n" % (x, driver.find_element(By.XPATH, '/html/body/div/main/section/div[2]/div/p/span/strong').text)
    arquivo.write(texto)

arquivo.close

# encerra o navegador
time.sleep(6)
driver.close()
