from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from helpers import init

def main(driver_path: str, path_to_visit: str):
    # NOTE: FOR EASINESS PURPOSES ON COLLAB, UNCOMMENT THIS LINE AND COMMENT THE LINES BELOW
    driver = init(
        driver_path=driver_path,
        headless=True,
        detach=False
    )

    # NOTE: FOR VISUALIZATION PURPOSES ON TEXT EDITOR, UNCOMMENT THIS LINE AND COMMENT THE LINES ABOVE
    # driver = init(
    #     driver_path=driver_path,
    #     headless=False,
    #     detach=True
    # )
    driver.get(path_to_visit)

    # wait element to be exist
    # Get this XPATH from Google DevConsole 
    # 1. Inspect the element you want to get
    # 2. Right click --> Copy as XPATH
    scroll_element_xpath = '//*[@id="content"]/div/div/div/div[@class="jscroll-inner"]'
    init_text = driver.find_element(By.XPATH, scroll_element_xpath)
    init_wait = WebDriverWait(driver, timeout=30)

    print("Waiting the initial text to be displayed before doing infinite scroll")
    init_wait.until(lambda _: init_text.is_displayed())

    # infinite scroll begins
    current_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        print(f"Current height: {current_height}")
        driver.execute_script("window.scroll(0, document.body.scrollHeight);")
        time.sleep(3)

        # let's say we want to stop the scroll after reach at least 10K height (in pixels)
        current_height = driver.execute_script("return document.body.scrollHeight")
        if current_height >= 1000:
            break
        
    # DO SOMETHING AFTER SCROLL ENDS

        
driver_path = "chromedriver_mac64/chromedriver"
path_to_visit = "https://the-internet.herokuapp.com/infinite_scroll"
main(driver_path, path_to_visit)