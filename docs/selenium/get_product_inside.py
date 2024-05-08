def get_data(large_category_name,small_category_name,url):
    # 웹 크롤링 동작
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    import time

    from selenium.webdriver.common.keys import Keys
    from datetime import datetime
    from bs4 import BeautifulSoup
    import re

    webdriver_manager_directory = ChromeDriverManager().install()
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
    # ChromeDriver 실행
    from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException    # Element : 웹요소 찾지 못할 때 / Window : 창이 없거나 찾을 수 없을 때
    # Chrome WebDriver의 capabilities 속성 사용
    capabilities = browser.capabilities
    from selenium.webdriver.common.by import By
    # - 정보 획득
    # from selenium.webdriver.support.ui import Select      # Select : dropdown 메뉴 다루는 클래스
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    # 몽고db 저장
    from pymongo import MongoClient
    # mongodb에 접속
    mongoClient = MongoClient("mongodb://localhost:27017")
    # database 연결
    database = mongoClient["dibidibi"]
    # collection 작업
    dibidibi = database['product']
    
    
    # - 주소 입력
    browser.get(url)

    time.sleep(1)

    # 스크롤 끝까지 내리기
    element_body = browser.find_element(by=By.CSS_SELECTOR,value='body')
    previous_scrollHeight = 0
    while True:
        element_body.send_keys(Keys.END)
        current_scrollHeight = browser.execute_script('return document.body.scrollHeight')
        if previous_scrollHeight >= current_scrollHeight:
            break
        else:
            previous_scrollHeight = current_scrollHeight
        time.sleep(1)

    # 초기 상위 아이템 목록
    product_list_value = '#dealResultFirst > div > #DealListUL > li'
    product_list = browser.find_elements(by=By.CSS_SELECTOR, value=product_list_value)

    for product in product_list:
        
        # 찜 갯수
        try:
            zzim = product.find_element(by=By.CSS_SELECTOR, value='div > a > div.info > div > div.stats > span:nth-child(1) > span').text
            zzim = re.sub(r'\D', '', zzim)
            zzim = int(zzim)
        except:
            zzim = ''

        # 상품 이름
        try:
            product_name = product.find_element(by=By.CSS_SELECTOR, value='div > a > div.info > div > div.gpnm').text
        except:
            product_name = ''

        # 상품 가격
        try:
            product_price = product.find_element(by=By.CSS_SELECTOR, value='div > a > div.info > div > div.bid > div > div.price.bidprice').text
            product_price = re.sub(r'\D', '', product_price)
            product_price = int(product_price)
        except:
            product_price = ''

        # 행사 가격
        try:
            product_event_price = product.find_element(by=By.CSS_SELECTOR, value='div > a > div.info > div > div.bid > div > div.price.txt').text
            product_event_price = re.sub(r'\D', '', product_event_price)
            product_event_price = int(product_event_price)
        except:
            product_event_price = ''

        # 판매자
        try:
            seller_name = product.find_element(by=By.CSS_SELECTOR, value='div > div > div > span.storenm.scab2').text
        except:
            seller_name = ''
        
        # 데이터 저장
        data={
        'large_category_name' : large_category_name,
        'small_category_name' : small_category_name,
        'zzim' : zzim,
        'product_name' : product_name,
        'product_price' : product_price,
        'product_event_price' : product_event_price,
        'seller_name' : seller_name,
        }
        dibidibi.insert_one(data)

    # 하위 아이템 목록
    product_list_value = '#dealResult > div > #DealListUL > li'
    product_list = browser.find_elements(by=By.CSS_SELECTOR, value=product_list_value)

    for product in product_list:
        # 찜 갯수
        try:
            zzim = product.find_element(by=By.CSS_SELECTOR, value='div > a > div.info > div > div.stats > span:nth-child(1) > span').text
            zzim = re.sub(r'\D', '', zzim)
            zzim = int(zzim)
        except:
            zzim = ''

        # 상품 이름
        try:
            product_name = product.find_element(by=By.CSS_SELECTOR, value='div > a > div.info > div > div.gpnm').text
        except:
            product_name = ''

        # 상품 가격
        try:
            product_price = product.find_element(by=By.CSS_SELECTOR, value='div > a > div.info > div > div.bid > div > div.price.bidprice').text
            product_price = re.sub(r'\D', '', product_price)
            product_price = int(product_price)
        except:
            product_price = ''

        # 행사 가격
        try:
            product_event_price = product.find_element(by=By.CSS_SELECTOR, value='div > a > div.info > div > div.bid > div > div.price.txt').text
            product_event_price = re.sub(r'\D', '', product_event_price)
            product_event_price = int(product_event_price)
        except:
            product_event_price = ''

        # 판매자
        try:
            seller_name = product.find_element(by=By.CSS_SELECTOR, value='div > div > div > span.storenm.scab2').text
        except:
            seller_name = ''
        
        # 데이터 저장
        data={
        'large_category_name' : large_category_name,
        'small_category_name' : small_category_name,
        'zzim' : zzim,
        'product_name' : product_name,
        'product_price' : product_price,
        'product_event_price' : product_event_price,
        'seller_name' : seller_name,
        }
        dibidibi.insert_one(data)

    browser.close()

