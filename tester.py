from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def launchBrowser():
    options = webdriver.ChromeOptions()

    # Set Chrome options before creating the WebDriver instance
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Set the path to the Chrome WebDriver executable
    driver = webdriver.Chrome(service=Service(r"C:\Projects\Funnystuff\checkingForNovelsUpdates\chromedriver.exe"), options=options)
    return driver  # Return the driver instance

def scrape_novels():
    driver = launchBrowser()

    books = [
        "https://www.lightnovelworld.com/novel/paragon-of-sin-14072105",
        "https://www.lightnovelworld.com/novel/my-three-wives-are-beautiful-vampires-30071448",
        "https://www.lightnovelworld.com/novel/rebirth-of-the-nameless-immortal-god-14072106",
        "https://www.lightnovelworld.com/novel/dimensional-descent-30071448",
        "https://www.lightnovelworld.com/novel/shadow-slave-30071448"
    ]

    agree = True

    try:
        for book in books:
            driver.get(book)
            print(book)
            if agree == True:
                try:
                    # Locate the <span> element with text "AGREE" and click it using XPath
                    agree_span = driver.find_element(By.XPATH, "//span[contains(text(), 'AGREE')]")
                    agree_span.click()
                except NoSuchElementException:
                    print("Element with text 'AGREE' not found")

            agree = False
            try:
                update = WebDriverWait(driver, 50).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, "update"))
                )
                print(update.text)
            except NoSuchElementException:
                print("Element with class 'update' not found")

            driver.get("about:blank")

    finally:
        print("done")
        #driver.quit()  # Make sure to close the browser when done

if __name__ == "__main__":
    scrape_novels()
