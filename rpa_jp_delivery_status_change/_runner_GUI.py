import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from ttkthemes import ThemedStyle
import re

# exe파일 출력: pyinstaller --onefile --noconsole _runner_GUI.py

# HTTP 요청에 사용할 헤더
HEADERS = {'tracking-update-key': 'MSS-ty7Q-GJrt-SEzl'}

# 각 환경별 API 엔드포인트
ENVIRONMENTS = {
    'dev': {
        'GET_TRACKING_INFO_API_URL': 'http://dev-dlvr-api-iapi.gncp-dlvr-jp.svc.ad1.io.navercorp.com/qa/trackings/',
        'UPDATE_STATUS_API_URL': 'http://dev-dlvr-gateway.gncp-dlvr-jp.svc.ad1.io.navercorp.com:8080/v2/tracker/goodsflowDeliveryState/'
    },
    'alpha': {
        'GET_TRACKING_INFO_API_URL': 'http://alpha-dlvr-api-iapi.gncp-dlvr-jp.svc.ad1.io.navercorp.com/qa/trackings/',
        'UPDATE_STATUS_API_URL': 'http://alpha-dlvr-gateway.gncp-dlvr-jp.svc.ad1.io.navercorp.com:8080/v2/tracker/goodsflowDeliveryState/'
    },
    'beta': {
        'GET_TRACKING_INFO_API_URL': 'http://beta-dlvr-api-iapi.gncp-dlvr-jp.svc.jr1.io.navercorp.com/qa/trackings/',
        'UPDATE_STATUS_API_URL': 'http://beta-dlvr-gateway.gncp-dlvr-jp.svc.jr1.io.navercorp.com:8080/v2/tracker/goodsflowDeliveryState/'
    },
    'real': {
        'GET_TRACKING_INFO_API_URL': 'http://dlvr-api-iapi.gncp-dlvr-jp.svc.jr1.io.navercorp.com/qa/trackings/',
        'UPDATE_STATUS_API_URL': 'http://dlvr-gateway.gncp-dlvr-jp.svc.jr1.io.navercorp.com:8080/v2/tracker/goodsflowDeliveryState/'
    }
}

# 배송상태 목록
DELIVERY_STATUSES = [
    '집하예정',
    '집하',
    '배송중',
    '배달중',
    '미배달',
    '배달완료',
    '인수확인',
    '반송'
]


def 배송정보_요청(tracking_no, env='alpha'):
    """
    송장번호의 배송 정보를 요청하는 함수
    """
    try:
        url = f'{ENVIRONMENTS[env]["GET_TRACKING_INFO_API_URL"]}{tracking_no}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data:
            delivery_info = data[0]
            delivery_no = delivery_info['deliveryNo']
            delivery_company_type = delivery_info['deliveryCompanyType']
            return delivery_no, delivery_company_type
        else:
            messagebox.showerror("Error", f"처리할 데이터가 없습니다. 송장번호 '{tracking_no}' 를 다시 확인해주세요.")
            return None, None
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"배송 정보를 가져오는 중 오류 발생: {e}")
        return None, None


def 배송상태_업데이트(delivery_company_type, delivery_no, tracking_stat, tracking_no, env='alpha'):
    """
    배송 정보의 상태를 업데이트하는 함수
    """
    try:
        url = f'{ENVIRONMENTS[env]["UPDATE_STATUS_API_URL"]}{delivery_company_type}/{delivery_no}/{tracking_stat}/{tracking_no}'
        response = requests.put(url, headers=HEADERS)
        response.raise_for_status()
        return tracking_no
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"배송 상태를 업데이트하는 중 오류 발생: {e}")
        return None

def submit(tracking_nos_str, tracking_stat, selected_env):
    """
    실행 버튼 클릭
    """
    tracking_nos = split_tracking_numbers(tracking_nos_str)
    if not tracking_stat:
        tracking_stat = "배송완료"
    success_tracking_nos = []  # 성공적으로 업데이트된 송장번호를 저장할 리스트
    for tracking_no in tracking_nos:
        delivery_no, delivery_company_type = 배송정보_요청(tracking_no, selected_env)
        if delivery_no and delivery_company_type:
            success_tracking_no = 배송상태_업데이트(delivery_company_type, delivery_no, tracking_stat, tracking_no, selected_env)
            if success_tracking_no:
                success_tracking_nos.append(success_tracking_no)  # 성공적으로 업데이트된 송장번호를 리스트에 추가

    # 성공적으로 업데이트된 송장번호를 메시지로 출력
    if success_tracking_nos:
        messagebox.showinfo("Success", f"배송상태가 성공적으로 업데이트되었습니다. 성공한 송장번호: {', '.join(success_tracking_nos)}")


def split_tracking_numbers(tracking_numbers_str):
    """
    입력된 송장번호 문자열을 콤마(,)로 분할하여 리스트로 반환
    """
    return re.split(r'\s*,\s*', tracking_numbers_str.strip())


def main():
    root = tk.Tk()
    root.title("배송상태변경")

    style = ThemedStyle(root)
    style.theme_use("clearlooks")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(frame, text="송장번호 입력 (여러개 입력시 콤마(,)로 구분):").grid(row=0, column=0, sticky=tk.W)
    tracking_entry = ttk.Entry(frame, width=50)
    tracking_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

    ttk.Label(frame, text="배송상태 선택:").grid(row=1, column=0, sticky=tk.W)
    selected_status = tk.StringVar()
    status_combobox = ttk.Combobox(frame, width=47, textvariable=selected_status, state="readonly")
    status_combobox.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
    status_combobox['values'] = DELIVERY_STATUSES
    status_combobox.current(5)

    ttk.Label(frame, text="환경 선택:").grid(row=2, column=0, sticky=tk.W)
    selected_env = tk.StringVar()
    env_combobox = ttk.Combobox(frame, width=47, textvariable=selected_env, state="readonly")
    env_combobox.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
    env_combobox['values'] = list(ENVIRONMENTS.keys())
    env_combobox.current(1)

    submit_button = ttk.Button(frame, text="실행", command=lambda: submit(tracking_entry.get(), selected_status.get(), selected_env.get()))
    submit_button.grid(row=3, column=1, padx=5, pady=5, sticky=tk.E)

    root.mainloop()


if __name__ == "__main__":
    main()
