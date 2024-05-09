from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from skpy import Skype
import os
from dotenv import load_dotenv

def upload_to_skype(sk, group_id, filename, delete_after=False):
    """
    Uploads a file to a Skype group chat with retry mechanism.

    Args:
        sk (Skype): Instance of the Skype client.
        group_id (str): ID of the Skype group chat.
        filename (str): Path to the file to upload.
        delete_after (bool, optional): Flag to indicate deletion after upload. Defaults to False.

    Returns:
        None
    """
    retries = 3
    while retries > 0:
        try:
            chat = sk.chats[group_id]
            chat.send_file(open(filename, "rb"), filename)
            if os.path.exists(filename) and delete_after:
                os.remove(filename)
                print('File deleted successfully!')
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
                time.sleep(1)

def take_screenshot(url, driver):
    """
    Takes a screenshot of a webpage and saves it with a descriptive name.

    Args:
        url (str): URL of the webpage to capture.
        driver (WebDriver): Instance of the WebDriver used for browsing.

    Returns:
        str: Path to the saved screenshot file.
    """
    driver.get(url)
    screenshot_name = f"screenshot_{driver.title}_{int(time.time())}.png"
    screenshot_path = os.path.join("screenshots", screenshot_name)
    driver.save_screenshot(screenshot_path)
    return screenshot_path

if __name__ == "__main__":
    load_dotenv()
    skype_username = os.getenv("skype_usr")
    skype_password = os.getenv("skype_pwd")
    skype_group_id = os.getenv("skype_group_id")

    # Improved readability with descriptive variable names
    sk = Skype(username=skype_username, password=skype_password)
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    url = "https://google.com"
    screenshot_filepath = take_screenshot(url, driver)
    upload_to_skype(sk, skype_group_id, screenshot_filepath)
    driver.quit()
    
