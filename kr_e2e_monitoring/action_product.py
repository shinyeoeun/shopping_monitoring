# -*- coding: utf-8 -*-
import elements, config, conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC


def 네이버로그인(driver, rp_logger):
    email = config.USER_EMAIL
    password = config.USER_PASSWORD
    try:
        conftest.wait_for_page_load(driver, rp_logger)
        rp_logger.info('로그인 페이지로 이동합니다.')
        driver.get(config.URLS['real']['네이버로그인'])
        rp_logger.info(f'로그인을 시도합니다: {email} / {password}')
        driver.find_element(By.NAME, "id").send_keys(email)
        driver.find_element(By.NAME, "pw").send_keys(password)
        driver.find_element(By.ID, "log.login").click()
    except Exception as e:
        rp_logger.error("로그인하는 도중 오류가 발생했습니다: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)

def 네이버로그인_팝업(driver, rp_logger, platform):
    email = config.USER_EMAIL
    password = config.USER_PASSWORD
    try:
        rp_logger.info('로그인 팝업으로 이동합니다.')
        main_page = driver.current_window_handle

        if platform == 'pc':
            WebDriverWait(driver, 10).until(lambda driver: len(driver.window_handles) > 1)
            popup_page = next(handle for handle in driver.window_handles if handle != main_page)
            driver.switch_to.window(popup_page)
            time.sleep(1)

            rp_logger.info(f'로그인을 시도합니다: {email} / {password}')
            driver.find_element(By.NAME, "id").send_keys(email)
            driver.find_element(By.NAME, "pw").send_keys(password)
            driver.find_element(By.ID, "log.login").click()
            time.sleep(1)

            driver.switch_to.window(main_page)

        elif platform == 'mo':
            rp_logger.info(f'로그인을 시도합니다: {email} / {password}')
            driver.find_element(By.NAME, "id").send_keys(email)
            driver.find_element(By.NAME, "pw").send_keys(password)
            driver.find_element(By.ID, "upper_login_btn").click()
            time.sleep(1)

    except Exception as e:
        rp_logger.error("로그인하는 도중 오류가 발생했습니다: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)


def 페이지이동(driver, rp_logger, channel, target):
    try:
        conftest.wait_for_page_load(driver, rp_logger)
        rp_logger.info(f'{channel} {target} 페이지로 이동합니다: {config.URLS["real"][f"{channel}_{target}"]}')
        driver.get(config.URLS['real'][f'{channel}_{target}'])
    except Exception as e:
        rp_logger.error(f"{target} 페이지로 이동 중 오류가 발생했습니다: {e}")
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)

def 상품상세_클릭(driver, rp_logger, platform, target):
    try:
        conftest.wait_for_page_load(driver, rp_logger)
        rp_logger.info(f'상품상세 [{target}] 버튼을 클릭합니다')

        if platform == 'pc':
            locator = (By.CLASS_NAME, elements.CLASS['상품상세'][target])
        elif platform == 'mo':
            locator = (By.XPATH, elements.XPATHS_MO['상품상세'][target])

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator))
        driver.find_element(*locator).click()
    except Exception as e:
        rp_logger.error(f"{target} 클릭 중 오류가 발생했습니다: {e}")
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)



def alert_확인(driver, rp_logger):
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        rp_logger.info("Alert 확인 버튼 클릭")
    except Exception as e:
        rp_logger.error("Alert 확인 중 오류가 발생했습니다: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)

def 장바구니_클릭(driver, rp_logger, target):
    try:
        conftest.wait_for_page_load(driver, rp_logger)
        rp_logger.info(f'장바구니 [{target}] 버튼을 클릭합니다')

        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, elements.CLASS['장바구니'][target]))
        )
        element.click()
    except Exception as e:
        rp_logger.error("장바구니 주문하는 도중 오류가 발생했습니다: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)

def 배송시간선택_확인(driver, rp_logger):
    return True

def 주문서_이동확인(driver, rp_logger):
    try:
        conftest.wait_for_page_load(driver, rp_logger)
        WebDriverWait(driver, 10).until(EC.url_contains("orders.pay.naver.com"))
        rp_logger.info("주문서 진입 성공")
        return True
    except Exception as e:
        rp_logger.error("주문서 진입 실패: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)


def 상품상세_이동확인(driver, rp_logger):
    try:
        conftest.wait_for_page_load(driver, rp_logger)
        WebDriverWait(driver, 10).until(EC.url_contains("smartstore.naver.com"))
        rp_logger.info("상품상세 진입 성공")
        return True
    except Exception as e:
        rp_logger.error("주문서 진입 실패: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)



def MY찜한상품_확인(driver, rp_logger):
    try:
        conftest.wait_for_page_load(driver)
        rp_logger.info(f'MY찜한상품 페이지로 이동합니다: {config.URLS["alpha"]["MY찜한상품"]}')
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, elements.XPATHS['MY찜한상품']['최근상품']))
        )
        product_name = element.text
        rp_logger.info(f'찜 성공한 상품명: {product_name}')
        return True
    except Exception as e:
        rp_logger.error("찜한상품 미노출: %s", e)
        conftest.log_exception(rp_logger)
        screenshot_file_path = conftest.save_numbered_screenshot(driver)
        conftest.log_screenshot(rp_logger, screenshot_file_path)
        return False


def MY찜한상품_상품삭제(driver, rp_logger):
    pass


def 장바구니초기화(driver, rp_logger, cart_type):
    페이지이동(driver, rp_logger, '장바구니', cart_type)
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, elements.CLASS['장바구니']['선택삭제']))
    )
    time.sleep(0.5)
    element.click()
    alert_확인(driver, rp_logger)
    time.sleep(0.5)
