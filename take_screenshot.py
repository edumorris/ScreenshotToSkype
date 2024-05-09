from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from skpy import Skype
import os
from dotenv import load_dotenv

def upload_to_skype(sk, group_id, filename, dlt):
    retries = 3
    while retries > 0:
        try:
            chat = sk.chats[group_id]  # Access the chat using Skype group ID
            chat.sendFile(open(filename, "rb"), filename)
            if os.path.exists(filename) and dlt:
                os.remove(filename)
                print('File was delete')
            print("File uploaded successfully!")
            break
        except Exception as e:
            print(f"Error uploading file: {e}")
            retries -= 1
            if retries == 0:
                print("Max retries exceeded. Exiting...")
                break
            else:
                print(f"Retrying upload. {retries} attempts left...")
                time.sleep(1)  # Add a short delay before retrying
            
def take_screenshot(url, driver):
    driver.get(url)
    screenshot_name = f'screenshot_{driver.title}_{int(time.time())}.png'
    screenshot_file = f'screenshots/{screenshot_name}'
    driver.save_screenshot(screenshot_file)
    return screenshot_file
    
if __name__ == '__main__':
    load_dotenv()
    sk = Skype(os.getenv('skype_usr'), os.getenv('skype_pwd'))
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    url = "https://google.com"  # URL of the webpage to capture
    screenshot_filename = take_screenshot(url, driver)
    upload_to_skype(sk, os.getenv('skype_group_id'), screenshot_filename, False)
    driver.quit()
    
