import tkinter as tk
from tkinter import ttk, messagebox
from rpa_order_maker.scenarios.scenario import (Scenario, RoundRobinTargetLoader, Targets, ReinitializingFallbackStrategy)
from scenarios import order_scenarioAction
from rpa_order_maker import utils, config

def initialize(test_scenario):
    # 새로운 드라이버 초기화
    driver = utils.driver_bootstrap(config.DRIVER_OPTIONS)
    # 이전 시나리오 종료 및 새로운 드라이버 설정
    test_scenario.driver_quit()
    test_scenario.set_driver(driver)

def run_scenarios(epochs_entry, targets_entries):
    epochs = int(epochs_entry.get())  # 입력된 반복 횟수 가져오기

    # 드라이버 설정
    driver = utils.driver_bootstrap(config.DRIVER_OPTIONS)

    # 로그인 시나리오 설정
    login_scenario = Scenario(driver)
    login_scenario.add_action(order_scenarioAction.LINE로그인(email=config.USER_EMAIL, password=config.USER_PASSWORD))

    # 타겟 상품상세 지정
    targets_list = []
    for entry in targets_entries:
        target_str = entry.get()
        if target_str.strip():
            targets_list.append(target_str)
    targets = Targets(targets_list)
    target_loader = RoundRobinTargetLoader(targets)

    # 주문 시나리오 설정
    auto_order_scenario = Scenario(driver, target_loader=target_loader)
    auto_order_scenario.add_action(order_scenarioAction.상품상세_장바구니추가())
    auto_order_scenario.add_action(order_scenarioAction.장바구니_주문하기())
    auto_order_scenario.add_action(order_scenarioAction.신용카드_TestPG결제())
    auto_order_scenario.set_fallback(ReinitializingFallbackStrategy(3, initialize))

    print('로그인 진행')
    login_scenario.run()

    print('자동 주문 진행')
    for epoch in range(epochs):
        print('ORDER EPOCH {}:'.format(epoch + 1))
        try:
            auto_order_scenario.run()
        except:
            print("Top level reinitialization occurs.")
            initialize(auto_order_scenario)

    auto_order_scenario.driver_quit()

    # 시나리오 실행 완료 후 알럿 노출
    messagebox.showinfo("알림", "시나리오 실행이 완료되었습니다.")

def main():
    root = tk.Tk()
    root.geometry("550x500")  # 너비 500 픽셀, 높이 300 픽셀로 설정
    root.title("RPA 주문 프로그램")

    ttk.Label(root, text="반복 횟수 입력:").pack(pady=10)
    epochs_entry = ttk.Entry(root)
    epochs_entry.pack(pady=5)

    ttk.Label(root, text="상품상세 리스트 입력:").pack(pady=10)
    targets_entries = []
    for i in range(5):  # 최대 5개의 입력란 생성
        label = ttk.Label(root, text=f"상품URL {i + 1}:")
        label.pack(pady=5, anchor="w")  # anchor를 w로 설정하여 왼쪽 정렬
        entry = ttk.Entry(root, width=50)  # 길이를 50으로 설정
        entry.pack(pady=5)
        targets_entries.append((label, entry))  # label과 entry를 함께 저장



    button = ttk.Button(root, text="시나리오 실행", command=lambda: run_scenarios(epochs_entry, targets_entries))
    button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
