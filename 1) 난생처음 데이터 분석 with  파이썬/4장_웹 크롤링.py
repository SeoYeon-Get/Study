"""# **4장. 웹 크롤링**"""

# 웹 크롤링 자동화 툴 : 그플랜트, 앱피움 등

# 정적인 페이지 : 서버에 저장된 데이터를 그대로 보여줌, 변하지 않음
# 동적인 페이지 : 사용자가 클릭하거나 텍스트를 입력하여 페이지의 상태를 바꿈
#                사용자의 행동에 따라 화면 구성이 달라지도록 설계된 페이지

#get() : 특정 웹페이지에 접속하는 함수
#driver.get([URL])

#fine_element() : 버튼이나 텍스트와 같은 객체를 찾기 위해 사용.
#driver.fine_element('xpath', '[실제 xPath 값']).text
#driver.fine_element('xpath', '[실제 xPath 값']).click()
#driver.fine_element('xpath', '[실제 xPath 값']).send_keys('[텍스트]')

#크롤링(Crawling) : 소프트웨어를 통해 인터넷 웹페이지로부터 정보를 수집하는 일

import sys

!sudo add-apt-repository ppa:saiarcot895/chromium-beta
!sudo apt remove chromium-browser
!sudo snap remove chromium
!sudo apt install chromium-browser

!pip install selenium
!apt-get upgrade
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin

sys.path.insert(0, 'usr/lib/chromium-browser/chromedriver')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 아래와 같이 설정하면 -> 셀레니움 사용 시 가상의 브라우저인 크롬 드라이버에서 동작을 수행하기 때문에,
# 버튼을 클릭하거나 텍스트를 입력해도 진행 상황이 눈에 보이지 않음.
# 도서와 코드 다름 -> 셀레니움 업데이트 때문
from selenium.webdriver.chrome.service import Service
service = Service(executable_path=r'/usr/bin/chromedriver')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

#가상의 웹 브라우저에서 창을 열고 이 객체를 변수에 할당.
driver = webdriver.Chrome(service=service, options=options)

url = 'https://ncov.kdca.go.kr/'
driver.get(url) #해당 웹페이지에 접속

#XPath(XML Path Language) : 웹페이지르 설계할 때 사용한 언어 구조로 위치를 특정하는 방식
topnews = driver.find_element('xpath','//*[@id="content"]/div[2]/div/section/div[2]/ul/li[1]/a')
print(topnews.text)

topnews = driver.find_elements('xpath','//*[@id="content"]/div[2]/div/section/div[2]/ul')

#여러 개의 텍스트를 리스트 topnews에 정리하기
topnews = [topnew.text for topnew in topnews]

print(topnews)

#돋보기 버튼을 찾아 클릭하는 작업 자동화
button = driver.find_element('xpath', '//*[@id="header"]/div/div[2]/a[1]')
print(button.text)
button.click()

#돋보기 버튼을 클릭하고 검색어 입력란을 클릭한 다음 검색어를 입력하고 Enter를 입력하는 과정 자동화
driver.find_element('xpath', '//*[@id="header"]/div/div[2]/a[1]').click()
driver.find_element('xpath', '//*[@id="searchTermMobile123"]').click()
driver.find_element('xpath', '//*[@id="searchTermMobile123"]').send_keys('서울')
driver.find_element('xpath', '//*[@id="searchTermMobile123"]').send_keys(Keys.ENTER)

print(driver.page_source)

#코로나 발생현황 데이터 수집
url = 'https://ncov.kdca.go.kr/'
driver.get(url)

#홈페이지 변경으로 인한 xpath값 변화 -> 도서참고
first_blank = driver.find_element('xpath', '//*[@id="searchTermMobile123"]').text
second_blank = driver.find_element('xpath', '//*[@id="searchTermMobile123"]').text
third_blank = driver.find_element('xpath', '//*[@id="searchTermMobile123"]').text
fourth_blank = driver.find_element('xpath', '//*[@id="searchTermMobile123"]').text

print('기준일자: ', first_blank, '\n일평균 사망자 수: ', second_blank,\
      '\n일평균 재원 위중증 환자 수: ', third_blank,'\n일평균 확진자 수: ', \
      fourth_blank)

