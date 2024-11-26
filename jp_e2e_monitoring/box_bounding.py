import asyncio
from playwright.async_api import async_playwright

async def swipe_element(url, num_swipes):
    async with async_playwright() as p:
        browser = await p.webkit.launch(headless=False)
        page = await browser.new_page()
        before_url = url
        await page.goto(before_url)  # 원하는 웹 페이지로 이동

        print("(함수)현재 진입한 URL: ", page.url)

        # 요소 선택
        element = await page.wait_for_selector(
            "//div[contains(@class, 'DoubleTapScreen_content_8siO2') and contains(@class, 'DoubleTapScreen_animation_show_content_9a5+s')]"
        )

        # 요소의 bounding box를 통해 위치와 크기 확인
        box = await element.bounding_box()
        if not box:
            print("요소를 찾을 수 없습니다.")
            await browser.close()
            return None

        # 요소의 정중앙 좌표 계산
        start_x = box['x'] + box['width'] / 2
        start_y = box['y'] + box['height'] / 2

        # end_x는 고정, end_y는 start_y + 400
        end_y = start_y + 400

        # 요소가 있는 위치로 스크롤
        await element.scroll_into_view_if_needed()

        for i in range(num_swipes):  # 스와이프 동작을 num_swipes 만큼 반복
            # 롱프레스 시작
            await page.mouse.move(start_x, start_y)
            await page.mouse.down()
            await page.wait_for_timeout(1500)  # 롱프레스 시간을 조정할 수 있습니다.

            # 드래그하여 스와이프 동작 수행
            await page.mouse.move(start_x, end_y, steps=10)  # 10단계로 이동
            await page.mouse.up()

            print(f"(함수)스와이프 {i+1}번 수행")

            # 스와이프 후 약간의 대기 시간 추가 (필요에 따라 조정 가능)
            await page.wait_for_timeout(1000)

            # 모든 요소가 visible 상태가 될 때까지 대기
            await page.wait_for_load_state('networkidle')  # 페이지의 네트워크 활동이 idle 상태가 될 때까지 대기
            await page.wait_for_selector('*:visible')  # 페이지 내 모든 요소가 visible 상태가 될 때까지 대기

        print("(함수)최종 스와이프 후 현재 URL: ", page.url)

        await browser.close()

        return page.url

# 비동기 함수를 실행하기 위한 이벤트 루프
# 원하는 스와이프 횟수를 num_swipes 인자로 전달
asyncio.run(swipe_element("https://qa-view.shoppinglive.naver.com/replays/119052", num_swipes=5))
