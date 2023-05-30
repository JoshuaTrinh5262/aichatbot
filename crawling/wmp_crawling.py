from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import dotenv
import re

import domain_extraction

config = dotenv.dotenv_values("./.env")
url = config['URL']
domain = domain_extraction.get_domain_from_url(url)
# Path to the downloaded ChromeDriver executable
driver_path = './crawling/'

# Create a Service object
service = Service(driver_path)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service = service)
# Navigate to a webpage

driver.get(url)

# Find an element by its ID
questions = driver.find_elements(By.CLASS_NAME, 'accordion-term')

print('please wait...')
for question in questions:
    classAttribute = question.get_attribute("class")

    if "is-active" not in classAttribute.split():
        question.click()

    answer = question.find_element(By.XPATH, './following-sibling::dd[contains(@class, "accordion-def")]')

   
    with open("server/store/wmp_example.txt", "a", encoding="utf-8") as file:
        # Get the text content without the number
        newQuestionString = re.sub(r'\d+', '', question.text.replace('\n', ' '))
        print(newQuestionString)
        file.write("User: " + newQuestionString + "\n")
        file.write("User: " + answer.text.replace('\n', ' ') + "\n")

    time.sleep(1)

# Close the browser
print('finished crawling')
driver.quit()