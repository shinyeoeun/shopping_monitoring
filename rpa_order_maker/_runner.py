from rpa_order_maker.scenarios.scenario import (Scenario, RoundRobinTargetLoader, Targets, ReinitializingFallbackStrategy)
from scenarios import order_scenarioAction
from rpa_order_maker import utils, config


def initialize(test_scenario):
    # 새로운 드라이버 초기화
    driver = utils.driver_bootstrap(config.DRIVER_OPTIONS)
    # 이전 시나리오 종료 및 새로운 드라이버 설정
    test_scenario.driver_quit()
    test_scenario.set_driver(driver)

def main():
    # 드라이버 설정
    driver = utils.driver_bootstrap(config.DRIVER_OPTIONS)

    # 로그인 시나리오 설정
    login_scenario = Scenario(driver)
    login_scenario.add_action(order_scenarioAction.LINE로그인(email=config.USER_EMAIL, password=config.USER_PASSWORD))

    # 타겟 상품상세 지정
    targets = Targets(config.URLS['real']['MY_상품상세_리스트'])
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
    while config.EPOCHS > auto_order_scenario.scenario_runs:
        print('ORDER EPOCH {}:'.format(auto_order_scenario.scenario_runs))
        try:
            auto_order_scenario.run()
        except:
            print("Top level reinitialization occurs.")
            initialize(auto_order_scenario)

    auto_order_scenario.driver_quit()

if __name__ == "__main__":
    main()
