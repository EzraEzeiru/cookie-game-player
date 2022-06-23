import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("/Users/ezeiruezra/Development/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.ID, value="cookie")


def get_all_items():
    all_products = driver.find_element(By.CSS_SELECTOR, value="#store")
    prices = all_products.find_elements(By.CSS_SELECTOR, value="b")
    store_dict = {}
    for price in prices:
        try:
            formatted_price = price.text.split("-")[1]
            if "," in formatted_price:
                new_price = formatted_price.replace(",", "")
                formatted_price = new_price
            formatted_price_int = int(formatted_price)
            formatted_name = price.text.split("-")[0].strip(" ")
            store_dict[f"{formatted_name}"] = formatted_price_int

        except IndexError:
            pass
    return store_dict


def check_for_upgrade(money):
    price_list = [value for (key, value) in all_items.items()]
    new_list = [price for price in price_list if money > price]
    max_price_available = max(new_list)
    for key, value in all_items.items():
        if value == max_price_available:
            return key


def check_total_clicks():
    all_clicks = driver.find_element(By.CSS_SELECTOR, value="#money")
    if "," in all_clicks.text:
        formatted_money = all_clicks.text.replace(",", "")
        total_clicks_int = int(formatted_money)
        return total_clicks_int
    total_clicks_int = int(all_clicks.text)
    return total_clicks_int


continue_game = True
time_later_sec = datetime.datetime.now() + datetime.timedelta(seconds=10)
five_sec_later = time_later_sec.second
time_later_min = datetime.datetime.now() + datetime.timedelta(minutes=5)
five_min_later = time_later_min.minute

continue_game = True
while continue_game:
    cookie.click()
    current_time = datetime.datetime.now().second
    current_min = datetime.datetime.now().minute
    if current_min == five_min_later:
        CPS = driver.find_element(By.CSS_SELECTOR, value="#cps")
        print(CPS.text)
        driver.quit()
        continue_game = False
    elif current_time == five_sec_later:
        time_later_sec = datetime.datetime.now() + datetime.timedelta(seconds=10)
        five_sec_later = time_later_sec.second
        all_items = get_all_items()
        total_clicks = check_total_clicks()
        click_this = check_for_upgrade(money=total_clicks)
        click_this = driver.find_element(By.CSS_SELECTOR, value=f"#buy{click_this}")
        click_this.click()
