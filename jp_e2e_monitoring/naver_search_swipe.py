import pytest
from selenium import webdriver
import pyautogui
import time

DRIVER_OPTIONS = ['disable-gpu', '--start-maximized', '--log-level=3']

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    for arg in DRIVER_OPTIONS:
        options.add_argument(arg)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def swipe_by_coordinates(start_x, start_y, end_x, end_y, duration=1):
    """
    지정된 좌표에서 좌표로 마우스 스와이프 동작을 수행.

    Args:
        start_x (int): 스와이프 시작 X 좌표.
        start_y (int): 스와이프 시작 Y 좌표.
        end_x (int): 스와이프 종료 X 좌표.
        end_y (int): 스와이프 종료 Y 좌표.
        duration (float): 스와이프 동작에 걸리는 시간 (초).
    """
    pyautogui.moveTo(start_x, start_y)
    pyautogui.mouseDown()
    pyautogui.moveTo(end_x, end_y, duration=duration)
    pyautogui.mouseUp()

def test_좌표로_스와이프(driver):
    driver.get('https://mini-search.shopping.naver.com/ns/search?query=%EA%B0%80%EB%94%94%EA%B1%B4')
    time.sleep(3)

    # 브라우저 위치와 크기 가져오기
    browser_position = driver.get_window_rect()  # {'x': 100, 'y': 100, 'width': 1920, 'height': 1080}
    browser_x = browser_position['x']
    browser_y = browser_position['y']

    # 스와이프 시작 좌표와 끝 좌표 설정 (브라우저 기준)
    start_x = browser_x + 1096
    start_y = browser_y + 400
    swipe_length = 400  # 오른쪽에서 왼쪽으로 스와이프할 길이
    end_x = start_x - swipe_length
    end_y = start_y

    # 스와이프 동작 수행
    swipe_by_coordinates(start_x, start_y, end_x, end_y)

    # 스와이프 결과를 확인하기 위한 대기 시간
    time.sleep(3)
