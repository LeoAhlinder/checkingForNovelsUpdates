import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

email_address = "gmail"
password = "password"

msg = MIMEMultipart()

def launchBrowser():
    options = webdriver.ChromeOptions()

    # Set Chrome options before creating the WebDriver instance
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Set the path to the Chrome WebDriver executable
    driver = webdriver.Chrome(service=Service(r"C:\Projects\Funnystuff\checkingForNovelsUpdates\chromedriver.exe"), options=options)


    return driver  # Return the driver instance


def booksToCheck():

    ##Books to check
    books = {
    }

    message = ""

    for name,url in books.items():
        driver = launchBrowser()

        driver.get(url)

        try:
            # Locate the <span> element with text "AGREE" and click it using XPath
            agree_span = driver.find_element(By.XPATH, "//span[contains(text(), 'AGREE')]")
            agree_span.click()
        except NoSuchElementException:
            print("Element with text 'AGREE' not found")

        try:
            update = driver.find_element(By.CLASS_NAME, "update")
            print(update.text,name)

            if "minutes" in update.text.lower() or "minute" in update.text.lower():
                message += name
            if "now" in update.text.lower() or "just" in update.text.lower():
                message += name
        except NoSuchElementException:
            print("Element with class 'update' not found")

        driver.quit()
    if (message != ""):
        msg['From'] = email_address
        msg['To'] = "to"
        msg['Subject'] = "novels update"
        body = message
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, password)
        text = msg.as_string()
        server.sendmail(email_address, "to", text)
        server.quit()
    

if __name__ == "__main__":
    booksToCheck()
