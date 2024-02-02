import csv
import os

import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from messages import body_selector

def prepare_image(driver):
    print("preparing the image started")
    image_path = '/home/esubalew/Downloads/proposals.jpeg'

    try:
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'editable-message-text'))
        )
        print("set image in try")
    except:
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.input-scroller-content'))
        )
        print("set image in except")

    file_input.click()
    pyautogui.hotkey('ctrl', 'v')
    print("preparing the image finished")


def prepare_message(driver):
    print("preparing the message started")
    try:
        editable_message_text_modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'editable-message-text-modal'))
        )
        print("set text in try")
    except:  
        editable_message_text_modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.input-scroller-content'))
        )
        print("set text in except")

    editable_message_text_modal.click()
    time.sleep(2)

    # Set inner HTML of the element
    driver.execute_script("arguments[0].innerHTML = arguments[1];", editable_message_text_modal, body_selector())
    time.sleep(2)

    editable_message_text_modal.send_keys(" ")
    time.sleep(2)

    print("preparing the message finished")

    # editable_message_text_modal.send_keys("\n")

def click_send_button(driver):
    print("sending the message started")    
    try:
        editable_message_text_modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'editable-message-text-modal'))
        )
        print("set text in try")
    except:  
        editable_message_text_modal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.input-scroller-content'))
        )
        print("set text in except")

    editable_message_text_modal.send_keys("\n")
    print("sending the message finished")    


def send_message_to_user(row_number, username, user_id, name, driver):
    
    print("searching the user started")
    # Find the input box by ID
    input_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, 'telegram-search-input'))
    )

    # Type the username into the input box
    input_box.clear()
    input_box.send_keys(username)

    # Simulate loading time (20 seconds)
    time.sleep(10)



    avatar_divs = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.ListItem.chat-item-clickable.search-result .Avatar.size-large')))

    # Loop through each Avatar div
    for avatar_div in avatar_divs:
        # Extract the data-peer-id attribute value
        peer_id = avatar_div.get_attribute('data-peer-id')
        
        # Check if the peer_id matches the target_peer_id
        if peer_id == user_id:
            # Click the ListItem
            avatar_div.click()
            print(f"User {peer_id} avatar clicked")
            break  # Break out of the loop once the desired item is clicked

    # Simulate loading time (20 seconds)
    time.sleep(5)
    prepare_image(driver)
    time.sleep(3)
    prepare_message(driver)
    click_send_button(driver)
    time.sleep(5)
    with open('sent_to.txt', 'a') as file:
        file.write(f"\n({user_id}) {username} {name}")
        print(f"Messages sent successfully to {name} ({user_id})")

    sleep_duration = random.uniform(5 * 60, 7 * 60)
