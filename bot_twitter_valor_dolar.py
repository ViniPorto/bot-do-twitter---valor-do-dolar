from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def main() -> None:
    bot()


def pegar_hora_atual() -> str:
    hora_atual = datetime.now()
    hora = hora_atual.strftime('%H:%M')
    return hora


def pegar_valor_dolar() -> float:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'}
    page = requests.get("https://www.google.com/search?q=dolar&oq=dolar&aqs=chrome.0.69i59j0j0i10i433j69i60j69i61l2j0.1615j0j1&sourceid=chrome&ie=UTF-8", headers=headers)

    page_pesquisa = BeautifulSoup(page.content, 'html.parser')

    valor_extraido = page_pesquisa.find_all("span", class_="DFlfde SwHCTb")[0]

    valor_dolar = valor_extraido['data-value']

    return round(float(valor_dolar), 2)


def bot() -> None:
    driver = webdriver.Chrome(executable_path=r"C://Users//porto//chromedriver.exe")  # path do chromedriver.exe
    driver.get("https://twitter.com/login")
    sleep(5)
    driver.find_element_by_name("session[username_or_email]").send_keys("@********")  # usuário ou email de conta válida
    driver.find_element_by_name("session[password]").send_keys("******")  # senha de conta válida
    driver.find_element_by_name("session[password]").send_keys(Keys.RETURN)
    sleep(5)
    while True:
        driver.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
        sleep(2)
        driver.find_element_by_class_name("notranslate").click()
        driver.find_element_by_class_name("notranslate").send_keys(f"Valor do dólar: R${pegar_valor_dolar()} às {pegar_hora_atual()}")
        driver.find_element_by_xpath("//div[@data-testid='tweetButton']").click()
        sleep(300)


if __name__ == '__main__':
    main()
