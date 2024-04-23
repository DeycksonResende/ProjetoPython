from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

def buscar_noticias(cidade):
    url = "https://news.google.com/topstories?hl=pt-BR&gl=BR&ceid=BR:pt-419"
    driver.get(url)
    
    # com o driver do selenium, automatizei achar o sistema de busca do site
    search_box = driver.find_element_by_class_name('gb_1d gb_Oe VISqTe')
    search_box.send_keys(cidade)
    search_box.send_keys(Keys.RETURN)
    
    #defini um tempo de espera pra não devolver NoSuchElementException
    driver.implicitly_wait(10)
    
    html = driver.page_source    
    soup = BeautifulSoup(html, 'html.parser')
    
    noticias = soup.find_all('h3', class_='PO9Zff kUVvS')

    for noticia in noticias:
        print(noticia.text)

# insere o nome da cidade no argumento da função
buscar_noticias()
