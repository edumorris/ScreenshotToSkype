from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from skpy import Skype
import os
from dotenv import load_dotenv

# Initialize Chrome driver instance
driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

def upload_to_skype(pic):
    load_dotenv()
    sk = Skype(os.getenv('skype_usr'), os.getenv('skype_pwd'))
    chat = sk.chats[os.getenv('skype_group_id')]  # Access the chat using Skype group ID
    chat.sendFile(open(pic, "rb"), pic)
    
    

def take_screenshot(url):
    driver.get(url)
    screenshot_name = f'screenshot_{driver.title}_{int(time.time())}.png'
    driver.save_screenshot(f'screenshots/{screenshot_name}')
    driver.quit()
    upload_to_skype(f'screenshots/{screenshot_name}')
        
    
if __name__ == '__main__':
    take_screenshot('https://google.com')
    
