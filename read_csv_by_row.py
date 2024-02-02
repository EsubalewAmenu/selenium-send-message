import csv
from send_message import send_message_to_user

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from messages import subject_selector, body_selector  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from send_message import prepare_image


def is_string_in_file(search_string):
    file_path = 'sent_to.txt'

    with open(file_path, 'r') as file:
        return search_string in file.read()


# Open file  
with open(r'scraped group/Catalyst Community Reviewers, Moderators, Advisors (copy).csv') as file_obj: 
      
    # Create reader object by passing the file  
    # object to reader method 
    reader_obj = csv.reader(file_obj) 

    # print(body_selector())
    # time.sleep(1000)
    

    options = Options()    
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    
    # url = "https://madebyevan.com/clipboard-test/"
    url = "https://web.telegram.org/a/#509706910"
    driver.get(url)

    time.sleep(4)
    # prepare_image(driver)
    # time.sleep(1000)

    # Maximize the window to full screen
    driver.maximize_window()


    # Find the input box by ID
    input_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, 'telegram-search-input'))
    )

    # Click the back button
    # back_button.click()

    # Iterate over each row in the csv  
    # file using reader object 
    for row_number, row in enumerate(reader_obj, 1):
        # print(f"Row {row_number}: {row}")

        # Print A and B column data
        if len(row) >= 5:

            result = is_string_in_file(row[1])

            if result:
                print(f'Already sent to {row[3]} ({row[1]} - {row[0]}) -  row {row_number}')
            else:
                # row[0] = 'esubalewA'
                # row[1] = '509706910'
                print(f'Next user is {row[0]}')
                send_message_to_user(row_number, row[0], row[1], row[3], driver)




print('All rows parsed successfully.')
