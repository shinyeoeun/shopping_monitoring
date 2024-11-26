from selenium import webdriver
from webdriver_manager import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def driver_bootstrap(arguments=[]):
    '''
    크롬을 사용하는 셀레늄 드라이버를 생성합니다.
    크롬 드라이버 바이너리 파일은 webdriver_manager 모듈이 파악하여 자동 다운로드 후 사용합니다.
    인자:
        arguments (문자열 리스트): 크롬 드라이버 옵션들.
    반환:
        driver: 크롬 웹 드라이버.
    '''
    options = webdriver.ChromeOptions()
    for arg in arguments:
        options.add_argument(arg)
        print(arg)
    binaryManager = chrome.ChromeDriverManager().install()
    driver = webdriver.Chrome(options=options)
    return driver


def wait_for_page_load(driver, max_wait_time=10):
    try:
        WebDriverWait(driver, max_wait_time).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*"))
        )
    except TimeoutException as e:
        rp_logger.error(f"페이지 로드 대기 시간 초과: {e}")
        raise
