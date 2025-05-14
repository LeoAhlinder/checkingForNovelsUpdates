from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

book = "https://novelbin.com/b/shadow-slave#tab-chapters-title"

def launchBrowser():
    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service)

def booksToCheck(url):
    driver.get(url)
    time.sleep(3)

    try:
        cookie_banner = driver.find_element(By.CLASS_NAME, "fc-dialog-container")
        button = cookie_banner.find_element(By.CLASS_NAME, "fc-button-label")
        button.click()

        div = driver.find_element(By.CLASS_NAME, "chr-c")
        paragraphs = div.find_elements(By.TAG_NAME, "p")
        chapter_title = div.find_element(By.TAG_NAME, "h4").text.strip()
        safe_title = re.sub(r'[\\/*?:"<>|]', "_", chapter_title)

        with open(f"{safe_title}.txt", "w", encoding="utf-8") as f:
            for p in paragraphs:
                print(p.text)
                f.write(p.text + "\n")

        print(f"Saved chapter '{chapter_title}' with {len(paragraphs)} paragraphs.")
    except NoSuchElementException:
        print("Element not found.")

def goToChapter(url):
    driver.get(url)

    try:
        chaptersContainer = driver.find_element(By.CLASS_NAME, "panel-body")
        chap = chaptersContainer.find_element(By.XPATH, '//*[contains(@title, "Chapter 5")]')
        chap.click()
        time.sleep(5)
        print("Found chapter with title:", chap.get_attribute("title"))
    except NoSuchElementException:
        print("Chapter with title containing 'Chapter 5' not found.")


if __name__ == "__main__":
    launchBrowser()
    goToChapter(book)
