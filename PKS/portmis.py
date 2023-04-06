from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Chrome 드라이버 위치 설정
driver_path = 'D:\chromedriver_win32\chromedriver'

# Chrome 드라이버 옵션 설정
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')  # 화면 크기 설정

# Chrome 드라이버 실행
driver = webdriver.Chrome(driver_path, options=options)

# 웹사이트 접속
url = 'https://new.portmis.go.kr/portmis/websquare/websquare.jsp?w2xPath=/portmis/w2/main/index.xml&page=/portmis/w2/cm/sys/UI-PM-MT-001-021.xml&menuId=0045&menuCd=M4735&menuNm=%ED%86%B5%ED%95%A9%ED%99%94%EB%AC%BC%EC%A0%95%EB%B3%B4'
driver.get(url)

# 로그인 버튼 클릭
login_button_locator = (
    By.XPATH, '//*[@id="mf_tacMain_contents_M4735_body_btn_goLogin"]')  # 버튼의 XPath 설정
wait = WebDriverWait(driver, 10)  # 10초간 대기
button = wait.until(EC.element_to_be_clickable(
    login_button_locator))  # 버튼이 클릭 가능할 때까지 대기
button.click()

# ID 입력
id_input = driver.find_element_by_xpath('//*[@id="mf_frameLogin1_login1_id"]')
id_input.send_keys('sinokor01')
# Password 입력
password_input = driver.find_element_by_xpath(
    '//*[@id="mf_frameLogin1_login1_pw"]')
password_input.send_keys('sinokor012!')
# Enter 키 입력
password_input.send_keys(Keys.RETURN)
# 2초 대기
time.sleep(2)
# 웹사이트 재접속
driver.get(url)

# 통합화물정보 버튼을 찾아 클릭
try:
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mf_tacMain_contents_M4735_body_genMenuLevel1_2_genMenuLevel2_3_genMenuLevel3_1_btnMenuLevel3"]'))
    )
    button.click()
    print('통합화물정보 버튼 클릭 완료')
except:
    print('통합화물정보 버튼을 찾을 수 없습니다.')

# 텍스트 입력란 찾기
chungcode_input = driver.find_element_by_id('mf_tacMain_contents_M9033_body_udc_prtAgCd_cmmCd')
hoculbuho_input = driver.find_element_by_id('mf_tacMain_contents_M9033_body_udc_clsgn_cmmCd')
iphangnyeundo_input = driver.find_element_by_id('mf_tacMain_contents_M9033_body_udc_etrypt_cmmCd')
iphanghoetsu_input = driver.find_element_by_id('mf_tacMain_contents_M9033_body_udc_etrypt_cmmCdNm')
upchecode_input = driver.find_element_by_id('mf_tacMain_contents_M9033_body_udc_entrpsCd_cmmCd')

