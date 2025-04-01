from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # To automatically install ChromeDriver
import time


url = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"


options = Options()
options.headless = False 

)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    
    driver.get(url)

    
    time.sleep(5)  

    
    rows = driver.find_elements(By.CSS_SELECTOR, 'table[data-test="historical-prices"] tbody tr')

    
    for row in rows:
        try:
            w
            date = row.find_element(By.CSS_SELECTOR, 'td[data-test="date"] span').text
            close_price = row.find_element(By.CSS_SELECTOR, 'td[data-test="close"] span').text
            print(f"Date: {date}, Close Price: {close_price}")
        except Exception as e:
            print(f"Error extracting data from row: {e}")
    
except Exception as e:
    print(f"Error fetching data: {e}")

finally:

    driver.quit()
if __name__ == "__main__":
    print("Running scrapper two...")
