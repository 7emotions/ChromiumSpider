import subprocess
import os.path
import shutil

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver

from webdriver_manager.microsoft import EdgeChromiumDriverManager


def find(browser: WebDriver, xpath: str) -> WebElement:
    """
    Find an element by xpath.
    :param browser: 
    :param xpath:
    :return:
    """
    return browser.find_element(by=By.XPATH, value=xpath)


def determine_drive_version(app_path=r'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe') -> str:
    """
    Check the version of the chromium driver.
    :param app_path: Edge application path.
    :return: WebDriver path
    """
    print('[*] Checking Chromium Driver version...')
    folder_path = os.path.join(os.getcwd(), 'driver')
    file_name = 'msedgedriver.exe'
    file_path = os.path.join(folder_path, file_name)

    if os.path.exists(file_path):
        result = subprocess.run([file_path, '--version'], capture_output=True, text=True)
        driver_version = '.'.join(result.stdout.strip().split(' ')[3].split('.')[:-1])

        command = f'wmic datafile where name="{app_path}" get Version /value'
        result_a = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = result_a.stdout.strip()
        version = '.'.join(output.split('=')[1].split('.')[0:3])

        if driver_version != version:
            print('[*] Updating Chromium Driver...')
            download_driver_path = EdgeChromiumDriverManager().install()
            shutil.copy(download_driver_path, folder_path)
            print('[+] Chromium Driver is updated.')
        else:
            print("[+] Chromium Driver is up to date.")

    else:
        print('[+] ChromeDriver is not installed. Installing Chromium Driver...')
        download_driver_path = EdgeChromiumDriverManager().install()
        shutil.copy(download_driver_path, folder_path)

    return file_path


def get_spider(headless=True) -> WebDriver:
    """
    Get Chromium Driver
    :param headless:headless mode
    :return: WebDriver
    """
    options = webdriver.EdgeOptions()
    options.add_experimental_option('detach', True)
    options.add_argument('window-size=1920x3000')
    options.add_argument('--disable-gpu')
    options.add_argument('--hide-scrollbars')
    options.add_argument('blink-settings=imagesEnabled=false')
    if headless:
        options.add_argument('--headless')
    options.add_argument('no-sandbox')
    options.add_argument('--disable-extensions')
    options.add_argument(r'User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                         r'like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0')

    file_path = determine_drive_version()
    service = Service(file_path)
    browser = webdriver.Edge(options=options, service=service)

    return browser
