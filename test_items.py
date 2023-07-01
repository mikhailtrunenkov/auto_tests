from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_card_button(browser):
    browser.get(url)
    
    button = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button")))
    raw_text = button.text
    
    button_lang = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[selected='selected']")))
    button_lang_text = button_lang.text
    
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    if button_lang_text == "français":
        assert "Ajouter au panier" == raw_text, f"Кажется, нужно указать: {raw_text}"

    