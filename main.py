# from requests import get # requests package download
# from bs4 import BeautifulSoup # BeautifulSoup package download
# # bs4는 html tag들을 list, dictiionary와 같은 자료구조로 변환
# from extractors.wwr import extract_wwr_jobs
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.incruit import extract_incruit_jobs
from extractors.saramin import extract_saramin_jobs

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
incruit = extract_incruit_jobs(keyword)
saramin = extract_saramin_jobs(keyword)

jobs = indeed + wwr + incruit + saramin

file = open(f"{keyword}.csv", "w", encoding="utf-8-sig") # CSV: comma-separated-value
file.write("Position,Company,Location,URL\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()

# challenge
# part 1. 다른 구직 사이트로 가서 자신만의 추출기 만들어보기
# part 1. incruit 완료 - 매우 미흡
# 태그를 불러올 때 클래스명을 활용하지 않고 태그 순서로 불러와 예외인 경우가 발생하여 오류 발생
# 밑의 링크를 통해 클래스명을 활용하여 추출하는 방법 터득. + get_text()
# https://replit.com/@rorodeuni/Scrapper#extractors/MyChallenge.py 참고해서 공부하기

# part 2. indeed에서 10개의 페이지를 스크랩 할 수 있는지 확인하고 시도

# Flask는 Python을 이용해서 웹사이트를 구축할 수 있는 초소형 micro framework


