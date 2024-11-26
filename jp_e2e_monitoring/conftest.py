from selenium import webdriver
import config
import pytest
from reportportal_client import RPLogger
import logging
import inspect
import os
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from PIL import Image


@pytest.fixture(scope="session")
def rp_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logging.setLoggerClass(RPLogger)
    return logger


@pytest.fixture(scope="session", autouse=True)
def init_image(request):
    directory = 'jp_e2e_monitoring/images'
    if not os.path.exists(directory):
        os.makedirs(directory)
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"파일을 삭제하는 도중 오류가 발생했습니다: {e}")


def save_numbered_screenshot(driver, directory='jp_e2e_monitoring/images', filename='screenshot'):
    if not os.path.exists(directory):
        os.makedirs(directory)

    caller_function = inspect.stack()[1].function

    count = 1
    while os.path.exists(f"{directory}/{filename}_{caller_function}_{count}.png"):
        count += 1

    png_filepath = f"{directory}/{filename}_{caller_function}_{count}.png"
    webp_filepath = f"{directory}/{filename}_{caller_function}_{count}.webp"

    driver.save_screenshot(png_filepath)

    with Image.open(png_filepath) as img:
        img.save(webp_filepath, 'webp')
    os.remove(png_filepath)

    return webp_filepath


def log_screenshot(rp_logger, screenshot_file_path):
    if screenshot_file_path:
        with open(screenshot_file_path, "rb") as image_file:
            file_data = image_file.read()
            rp_logger.info(
                "에러 스크린샷",
                attachment={"name": "dummy.png",
                            "data": file_data,
                            "mime": "image/png"}
            )


def log_exception(rp_logger):
    exception_info = traceback.format_exc()
    rp_logger.error("Exception occurred:\n%s", exception_info)


def wait_for_page_load(driver, rp_logger, max_wait_time=10):
    try:
        WebDriverWait(driver, max_wait_time).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*"))
        )
    except TimeoutException as e:
        rp_logger.error(f"페이지 로드 대기 시간 초과: {e}")
        raise


def click_xpath_element_to_be_clickable(driver, xpath):
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()
