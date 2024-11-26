import random

class Scenario:
    """
    시나리오 클래스
    """
    def __init__(self, driver, target_loader=None):
        self.actions = []
        self.set_driver(driver)
        self.target_loader = target_loader
        self.fallback = RecursiveRetryFallbackStrategy(max_retries=5)
        self.scenario_runs = 0

    def driver_quit(self):
        """
        드라이버 종료
        """
        self.driver.close()
        self.driver.quit()

    def run(self):
        """
        시나리오 실행
        """
        try:
            if self.target_loader is None:
                self._run(target=None)
            else:
                self._run(self.target_loader.next())
        except FallbackStrategy.FallbackGiveUp as fbgu:
            self.driver_quit()
            raise fbgu
        except Exception as e:
            self.fallback.handle(e, self)

    def _run(self, target):
        """
        내부 시나리오 실행
        """
        print(f"[Scenario] Run {self.scenario_runs} with target {target}.")
        for a in self.actions:
            print(f"Action: {a.__class__.__name__}")
            if a.require_target():
                a.run(target)
            else:
                a.run()
        self.scenario_runs += 1

    def add_action(self, action):
        """
        액션 추가
        """
        action.set_driver(self.driver)
        self.actions.append(action)

    def set_driver(self, driver):
        """
        드라이버 설정
        """
        self.driver = driver
        for a in self.actions:
            a.set_driver(self.driver)

    def set_target(self, target_loader):
        """
        타겟 설정
        """
        self.target_loader = None

    def set_fallback(self, fallback_strategy):
        """
        폴백 설정
        """
        self.fallback = fallback_strategy


class FallbackStrategy:
    """
    폴백 전략 클래스
    """
    def handle(self, error, state):
        """
        예외 처리
        """
        raise NotImplementedError

    class FallbackGiveUp(Exception):
        """
        폴백 포기 예외 클래스
        """
        pass


class RecursiveRetryFallbackStrategy(FallbackStrategy):
    """
    재귀 재시도 폴백 전략 클래스
    """
    def __init__(self, max_retries):
        self.max_retries = max_retries
        self.retries = 0

    def handle(self, error, scenario):
        """
        예외 처리
        """
        print("[Fallback] fallback retry {} with error: {}".format(self.retries, error))
        if self.retries + 1 <= self.max_retries:
            print('[Fallback] proceed.')
            self.retries += 1
            scenario.run()
        else:
            print('[Fallback] give up.')
            raise FallbackStrategy.FallbackGiveUp


class ReinitializingFallbackStrategy(FallbackStrategy):
    """
    재초기화 폴백 전략 클래스
    """
    def __init__(self, threshold, reinitializer):
        self.delegate_under_threshold = RecursiveRetryFallbackStrategy(max_retries=threshold)
        self.threshold = threshold
        self.reinitializer = reinitializer

    def handle(self, error, scenario):
        """
        예외 처리
        """
        try:
            self.delegate_under_threshold.handle(error, scenario)
        except FallbackStrategy.FallbackGiveUp as fbgu:
            print("[Fallback] Fallback level reinitialization occurs.")
            try:
                self.reinitializer(scenario)
                self.delegate_under_threshold = RecursiveRetryFallbackStrategy(max_retries=self.threshold)
            except:
                raise FallbackStrategy.FallbackGiveUp
        except Exception:
            raise FallbackStrategy.FallbackGiveUp


class ScenarioAction:
    """
    시나리오 액션 클래스
    """
    def __init__(self):
        self.driver = None

    def set_driver(self, driver):
        """
        드라이버 설정
        """
        self.driver = driver

    def run(self, target=None):
        """
        실행
        """
        raise NotImplementedError

    def require_target(self):
        """
        타겟 필요 여부 반환
        """
        return False


class Targets:
    """
    타겟 클래스
    """
    def __init__(self, target_urls):
        self.targets = target_urls
        self.subscribers = []

    def add_target(self, target_url):
        """
        타겟 추가
        """
        self.targets.append(target_url)
        for s in self.subscribers:
            s.handle_noti(1 if target_url is str else len(target_url))

    def get(self, i):
        """
        인덱스에 해당하는 타겟 반환
        """
        return self.targets[i]

    def subscribe(self, obj):
        """
        구독 추가
        """
        self.subscribers.append(obj)

    def length(self):
        """
        길이 반환
        """
        return len(self.targets)


class TargetLoader:
    """
    타겟 로더 클래스
    """
    def __init__(self, targets: Targets):
        targets.subscribe(self)
        self.targets = targets
        self.current_index = None

    def next(self):
        """
        다음 타겟 반환
        """
        raise NotImplementedError

    def current(self):
        """
        현재 타겟 반환
        """
        return self.targets.get(self.current_index)

    def handle_noti(self, hint):
        """
        알림 처리
        """
        pass


class RoundRobinTargetLoader(TargetLoader):
    """
    라운드로빈 타겟 로더 클래스
    """
    def __init__(self, targets: Targets):
        super().__init__(targets)
        self.current_index = -1

    def next(self):
        """
        다음 타겟 반환
        """
        self.current_index += 1
        if self.current_index >= self.targets.length():
            self.current_index = 0
        return self.current()

    def handle_noti(self, hint):
        """
        알림 처리
        """
        change_amount = hint
        if change_amount > 0:
            pass
        elif self.current_index >= self.targets.length():
            self.current_index = 0


class RandomTargetLoader(TargetLoader):
    """
    랜덤 타겟 로더 클래스
    """
    def __init__(self, targets: Targets):
        super().__init__(targets)
        self.current_index = None

    def next(self):
        self.current_index = self.random_index()
        return self.current()

    def random_index(self):
        return random.randrange(0, self.targets.length())
            