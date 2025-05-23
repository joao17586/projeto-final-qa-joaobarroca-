!pip install selenium
!apt-get update 
!apt install -y chromium-chromedriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time

# Configuração do ChromeDriver para o Colab
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executa em modo sem interface gráfica
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

class TestSelenium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('chromedriver', options=options)
        cls.driver.implicitly_wait(10)  # Espera implícita de 10 segundos
    
    def test_pesquisa_google(self):
        """Testa uma pesquisa no Google"""
        driver = self.driver
        driver.get("https://www.google.com")
        
        # Rejeitar cookies se o popup aparecer
        try:
            reject_button = driver.find_element(By.XPATH, '//button[contains(., "Rejeitar tudo")]')
            reject_button.click()
        except:
            pass
        
        # Localizar campo de pesquisa e pesquisar
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Python Selenium" + Keys.RETURN)
        
        # Verificar se resultados aparecem
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        self.assertGreater(len(results), 3, "Deveria ter mais de 3 resultados")
    
    def test_wikipedia(self):
        """Testa busca na Wikipedia"""
        driver = self.driver
        driver.get("https://www.wikipedia.org")
        
        search_box = driver.find_element(By.ID, "searchInput")
        search_box.send_keys("Selenium (software)" + Keys.RETURN)
        
        # Verificar título do artigo
        title = driver.find_element(By.ID, "firstHeading")
        self.assertIn("Selenium", title.text)
        
        # Verificar tabela de conteúdo
        toc = driver.find_element(By.ID, "toc")
        self.assertTrue(toc.is_displayed())
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # Fecha o navegador após todos os testes

# Executando os testes no Colab
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
