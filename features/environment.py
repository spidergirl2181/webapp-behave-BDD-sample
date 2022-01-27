from multiprocessing import context
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

from features.pages.page import Page

def before_scenario(context, scenario):
    context.base_url = "https://openweathermap.org/"
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    # start of headless mode config
    option.add_argument("--headless")
    option.add_argument("--disable-gpu")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--no-sandbox")
    option.add_argument("--window-size=1920,1080")
    option.add_argument("--no-first-run")
    option.add_argument("--no-default-browser-check")
    option.add_argument("--ignore-certificate-errors")
    # end of headless mode config

    # Relative filepath on Windows
    context.browser = webdriver.Chrome(r'C:features\browserdriver\chromedriver.exe', chrome_options=option) 

    # Use WebDriver-Manager (see more at: https://pypi.org/project/webdriver-manager/)
    #context.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    context.browser.get(context.base_url)

    # construct base page
    context.page = Page(context.browser, context.base_url)

def after_scenario(context, scenario):
	context.browser.quit()
