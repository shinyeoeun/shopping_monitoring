# -*- coding: utf-8 -*-
import elements, config, conftest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def 페이지이동(driver, rp_logger, env, target):
    try:
        conftest.wait_for_page_load(driver, rp_logger)
        rp_logger.info(f'{target} 페이지로 이동합니다: {config.URLS[env][target]}')
        driver.get(config.URLS[env][target])
        driver.implicitly_wait(5)
        conftest.wait_for_page_load(driver, rp_logger)
    except Exception as e:
        rp_logger.error(f"{target} 페이지로 이동 중 오류가 발생했습니다: {e}")
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)


def LINE로그인(driver, rp_logger):
    email = config.USER_EMAIL
    password = config.USER_PASSWORD
    try:
        conftest.wait_for_page_load(driver, rp_logger)
        conftest.click_xpath_element_to_be_clickable(driver, elements.XPATHS['로그인']['LINE로그인'])
        rp_logger.info(f'MY 로그인을 시도합니다: {email} / {password}')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "tid")))  # 로그인 페이지가 로드될 때까지 대기
        driver.find_element(By.NAME, "tid").send_keys(email)
        driver.find_element(By.NAME, "tpasswd").send_keys(password)
        driver.find_element(By.CLASS_NAME, "MdBtn01").click()
        time.sleep(1)
    except Exception as e:
        rp_logger.error("로그인하는 도중 오류가 발생했습니다: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)

def 비즈니스로그인(driver, rp_logger):
    email = config.SELLER_ID
    password = config.SELLER_PASSWORD
    try:
        conftest.wait_for_page_load(driver, rp_logger)
        conftest.click_xpath_element_to_be_clickable(driver, elements.XPATHS['로그인']['센터로그인'])
        rp_logger.info(f'센터 로그인을 시도합니다: {email} / {password}')
        driver.find_element(By.XPATH, elements.XPATHS['로그인']['비즈니스계정으로로그인']).click()
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element((By.XPATH, elements.XPATHS['로그인']['biz로그인버튼']))
        time.sleep(1)
    except Exception as e:
        rp_logger.error("로그인하는 도중 오류가 발생했습니다: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)


def 상품상세_장바구니추가(driver, rp_logger):
    try:
        rp_logger.info('[장바구니 추가] 버튼을 클릭합니다.')
        for _ in range(2):
            conftest.click_xpath_element_to_be_clickable(driver, elements.XPATHS['상품상세']['장바구니추가'])
        driver.implicitly_wait(5)
        conftest.click_xpath_element_to_be_clickable(driver, elements.XPATHS['상품상세']['장바구니이동'])
        time.sleep(1)
    except Exception as e:
        rp_logger.error("상품을 장바구니에 추가하는 도중 오류가 발생했습니다: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)

def 장바구니_주문하기(driver, rp_logger):
    try:
        rp_logger.info('[주문하기] 버튼을 클릭합니다.')
        conftest.click_xpath_element_to_be_clickable(driver, elements.XPATHS['장바구니']['주문하기'])
        driver.implicitly_wait(5)
    except Exception as e:
        rp_logger.error("장바구니에서 주문하기 버튼을 클릭하는 도중 오류가 발생했습니다: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)


def 주문서_결제(driver, rp_logger, platform, payment):
    try:
        rp_logger.info('[결제방법-수정] 버튼을 클릭합니다.')
        scroll_location = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            scroll_height = driver.execute_script("return document.body.scrollHeight")
            if scroll_location == scroll_height:
                break
            else:
                scroll_location = driver.execute_script("return document.body.scrollHeight")
        conftest.click_xpath_element_to_be_clickable(driver, elements.XPATHS['주문서']['결제방법_수정'])

        driver.implicitly_wait(5)
        while True:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            scroll_height = driver.execute_script("return document.body.scrollHeight")
            if scroll_location == scroll_height:
                break
            else:
                scroll_location = driver.execute_script("return document.body.scrollHeight")

        rp_logger.info(f'결제방법을 선택합니다:  {payment}')
        driver.find_element(By.XPATH, elements.XPATHS['주문서'][payment]).click()

        rp_logger.info('[주문내용확인] 버튼을 클릭합니다.')
        conftest.click_xpath_element_to_be_clickable(driver, elements.XPATHS['주문서']['주문내용확인'])
        time.sleep(1)

        rp_logger.info('[주문확정하기] 버튼을 클릭합니다.')
        conftest.click_xpath_element_to_be_clickable(driver, elements.XPATHS['주문서']['주문확정하기'])
        time.sleep(1)

        main_page = driver.current_window_handle

        if platform == 'pc':
            WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)
            popup_page = next(handle for handle in driver.window_handles if handle != main_page)
            driver.switch_to.window(popup_page)
            time.sleep(1)

            driver.switch_to.window(popup_page)
            try:
                pg_element = driver.find_element(By.XPATH, elements.XPATHS['주문서']['TestPG_결제확정'])
                pg_element.click()
                driver.implicitly_wait(10)
            except NoSuchElementException:
                pass

            driver.switch_to.window(driver.window_handles[0])
            driver.switch_to.window(main_page)

        elif platform == 'mo':
            try:
                pg_element = driver.find_element(By.XPATH, elements.XPATHS['주문서']['TestPG_결제확정'])
                pg_element.click()
                driver.implicitly_wait(10)
            except NoSuchElementException:
                pass

    except Exception as e:
        rp_logger.error("주문서에서 결제를 진행하는 도중 오류가 발생했습니다: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)

def 주문성공(driver, rp_logger):
    try:
        order_no_element = driver.find_element(By.XPATH, elements.XPATHS['주문서']['주문번호'])
        order_no = order_no_element.text
        rp_logger.info(f"주문번호: {order_no}")
        return True
    except Exception as e:
        rp_logger.error("주문실패: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)
        return False

def 상품관리_페이지진입성공(driver, rp_logger):
    try:
        conftest.wait_for_page_load(driver, rp_logger)
        WebDriverWait(driver, 10).until(EC.url_contains("https://smartstorecenter.jp/#/products/origin-list"))
        return True
    except Exception as e:
        rp_logger.error("진입식패: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)
        return False

