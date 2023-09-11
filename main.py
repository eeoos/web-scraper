from requests import get # requests package download
from bs4 import BeautifulSoup # BeautifulSoup package download
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#options.add_argument("--no-sandbox")
#options.add_argument("--disable-dev-shm-usage")


# request로 접속하면 indeed가 차단
# Selenium 사용 방법"""
"""
Files 옆 점 세개 클릭 -> Show hidden files 클릭 -> Config files가 보임 -> replit.nix 클릭 -> deps 안의 python38 아래에 pkgs.chromium 타이핑 -> enter 후 pkgs.chromedrive 타이핑
(chromium: 크롬 브라우저의 기반이 되는 브라우저)
(Replit에서 브라우저를 사용하기 위한 준비 끝)

"""
# 구글 크롬 브라우저를 생성
browser = webdriver.Chrome()

browser.get("https://kr.indeed.com/jobs?q=python&limit=50")

soup = BeautifulSoup(browser.page_source, "html.parser")

job_list = soup.find("ul", class_="css-zu9cdh")
jobs = job_list.find_all('li', recursive=False) # recursive-False를 통해 ul 바로 밑에 있는 li만 추출
print(len(jobs))
for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        print("job li")
    else:
        print("mosaic li")

















while True: # 크롬 자동 종료 방지 코드
    pass