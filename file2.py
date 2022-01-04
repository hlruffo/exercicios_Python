import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# define a busca
pesquisa = input("O que precisa buscar? Insira aqui : ")

# chama o exe que abre o navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://google.com/")

# acha o campo de busca
campo = driver.find_element(By.XPATH, '//input[@aria-label="Pesquisar"]')
time.sleep(2)
campo.send_keys(pesquisa)
time.sleep(2)
campo.send_keys(Keys.RETURN)
time.sleep(2)

# importando dados do resultado da pesquisa
resultados = driver.find_element(By.XPATH, '//*[@id="result-stats"]').text
print(resultados)

# descrever resultados
numero_resultados = float(resultados.split('Aproximadamente')[1].split('resultados')[0].replace('.', ''))
numero_paginas = numero_resultados / 10
print(numero_resultados)
print("Número de paginas:", numero_paginas)

# navegar entre as páginas de resultado
url_pagina = driver.find_element(By.XPATH, '//a[@aria-label="Page 2"]').get_attribute('href')
pagina_atual = 0
start = 10
lista_resultados = []
while pagina_atual < 9:

    if not pagina_atual == 0:
        url_pagina = url_pagina.replace('start=%s' % start, 'start=%s' % (start + 10))
        start = start + 10
        driver.get(url_pagina)
    pagina_atual = pagina_atual + 1
    time.sleep(2)

    # retorna as informações de pesquisa

    divs = driver.find_elements(By.XPATH, '//div[@class="g"]')
    for div in divs:
        nome = div.find_element(By.TAG_NAME, 'h3')
        link = div.find_element(By.TAG_NAME, "a")
        resultado = "%s; %s" % (nome.text, link.get_attribute("href"))
        print(resultado)

        # envia resultados para um arquivo externo via lista
        lista_resultados.append(resultado)
    with open('Resultados.txt', 'w') as arquivo:
        for resultado in lista_resultados:
            arquivo.write('%s\n' % resultado)
        arquivo.close()
    print('%s resultados encontrados no Google e salvos no arquivo Resultados.txt' % len(lista_resultados))
