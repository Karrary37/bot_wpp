# ATENÇAO
# Antes de rodar o codigo é necessario copiar a mensagem  que deseja enviar para seus grupos.

# Importar bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys

# Navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

# Buscar contatos/grupos
contatos = ['PROJETOS', 'FAMILIA MM']


# Selecionar contato e entrar na conversa
def buscar_contato(contato):
    campo_pesquisa = driver.find_element("xpath", '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


# Enviar mensagem e foto
def enviar_mensagem():
    # Selecionar campo de mensagem
    time.sleep(1)
    clip = driver.find_element("xpath", '//div[contains(@title,"Mensagem")]')
    clip.click()

    # Colar mensagem
    time.sleep(1)
    clip.send_keys(Keys.CONTROL + "v")
    time.sleep(2)

    # Enviar mensagem
    clip.send_keys(Keys.ENTER)
    print("Enviamos sua mensagem no grupo " + contato)
    time.sleep(5)


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem()
