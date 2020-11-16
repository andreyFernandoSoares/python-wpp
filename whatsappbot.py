# pip install selenium
# pip install webdriver_manager

#import libs
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#navegando até o wpp
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/");
time.sleep(5)

#definir contatos e grupos
contatos = ['Nossogrupo']
msg = "isso não é um span"

#campo pesquisa copyable-text selectable-text
#campo msg copyable-text selectable-text
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(msg):
    campo_msg = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_msg[1].click()
    time.sleep(3)
    campo_msg[1].send_keys(msg)
    campo_msg[1].send_keys(Keys.ENTER)

for n in range(100):
    for contato in contatos:
        buscar_contato(contato)
        enviar_mensagem(msg)