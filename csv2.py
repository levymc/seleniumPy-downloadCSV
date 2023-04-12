from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta
from bs4 import BeautifulSoup
from time import sleep

## Gerenciador de Tarefas - 13:45 da tarde todos os dias.
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
mes = date.today().month -1
hoje = date.today().strftime("%d-%m-%Y")
path = r'//NasTecplas/Public/3 ADMINISTRATIVO/FISCAL/CSV Etiquetas/'+ meses[mes] + '/' + hoje + r'/Tarde' 
options = webdriver.ChromeOptions()
options.headless = False
prefs = {
    'download.default_directory': path.replace('/', '\\'),
}
options.add_experimental_option('prefs', prefs)
navegador = webdriver.Chrome(chrome_options=options)

# Acessando a página do sistema
navegador.get("http://192.168.0.50/tecplas/producao/producao_nff_etiq.asp")


# Data Inicial 394, 279
yesterday = date.today() - timedelta(days=1)
yesterday = yesterday.strftime("%d/%m/%Y")
navegador.find_element(By.XPATH, '//*[@id="filtro1"]').send_keys(f'{yesterday}')

# Data Final
today = date.today().strftime("%d/%m/%Y")
navegador.find_element(By.XPATH, '//*[@id="filtro2"]').send_keys(f'{today}')

# Selecinando o checkbox "Deixar todas selecionadas"
navegador.find_element(By.XPATH, '//*[@id="sel"]').click()

# Clicando em "Confirma" 1ª vez
navegador.find_element(By.XPATH, '/html/body/div/div/table/tbody/tr/td/div/table[2]/tbody/tr/td[1]/div/input').click()

# Espera a página carregar e clica em "Confirma" 2ª vez
wait = WebDriverWait(navegador, 10) # aguarda por 10 segundos
element = wait.until(EC.presence_of_element_located((By.ID, 'form')))
navegador.find_element(By.XPATH, '//*[@id="form"]/table[2]/tbody/tr/td/strong/input').click()

# Espera a página carregar e clica em "Clique Aqui", para realizar o download do csv
wait = WebDriverWait(navegador, 10) # aguarda por 10 segundos
element2 = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Clique")))
navegador.find_element(By.PARTIAL_LINK_TEXT, "Clique").click()

sleep(5)
navegador.quit()

