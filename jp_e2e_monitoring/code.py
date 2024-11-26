import asyncio
from playwright.async_api import async_playwright

async def swipe_element(start_x, start_y, end_x, end_y, url):
    async with async_playwright() as p:
        browser = await p.webkit.launch(headless=False)
        page = await browser.new_page()
        before_url = url
        await page.goto(before_url)  # 원하는 웹 페이지로 변경

        print("(함수)현재 진입한 URL: ", page.url)

        # 요소 선택
        element = await page.wait_for_selector('.flicking-camera')

        # 요소가 있는 위치로 스크롤
        await element.scroll_into_view_if_needed()

        # 롱프레스 시작
        await page.mouse.move(start_x, start_y)
        await page.mouse.down()
        await page.wait_for_timeout(1500)  # 롱프레스 시간을 조정할 수 있습니다.

        # 드래그하여 스와이프 동작 수행
        await page.mouse.move(end_x, end_y, steps=10)  # 10단계로 이동
        await page.mouse.up()

        # 페이지가 종료될 때까지 대기 (필요에 따라 변경 가능)
        await page.wait_for_timeout(5000)

        print("(함수)스와이프후 현재 URL: ", page.url)

        await browser.close()

        return page.url

# 비동기 함수를 실행하기 위한 이벤트 루프
asyncio.run(swipe_element(100, 200, 100, 600, "https://qa-view.shoppinglive.naver.com/replays/119052"))  # 시작 지점 (100, 200)에서 끝 지점 (100, 400)으로 스와이프