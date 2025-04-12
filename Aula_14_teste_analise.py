# Passo 1: Instalar o Selenium e baixar o ChromeDriver
pip install selenium
# Baixar o ChromeDriver compatível com a versão do seu Chrome em https://sites.google.com/chromium.org/driver/

# Passo 2: Criar um script de teste funcional
echo "
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inicializa o navegador (Chrome)
driver = webdriver.Chrome(executable_path='path/to/chromedriver')

# Passo 3: Navegar até a página de teste
driver.get('https://example.com')

# Verificar se o título da página está correto
assert 'Example Domain' in driver.title

# Encontrar o elemento de link e clicar nele
elem = driver.find_element_by_xpath('//a[text()=\"More information...\"]')
elem.click()

# Verificar se a navegação foi bem-sucedida
assert 'IANA' in driver.title

# Fechar o navegador
driver.quit()
" > test_selenium.py

# Passo 4: Executar o script e analisar os resultados
python test_selenium.py
