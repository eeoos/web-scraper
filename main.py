# from requests import get # requests package download
# from bs4 import BeautifulSoup # BeautifulSoup package download
# # bs4는 html tag들을 list, dictiionary와 같은 자료구조로 변환
# from extractors.wwr import extract_wwr_jobs
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr

file = open(f"{keyword}.csv", "w", encoding="utf-8") # CSV: comma-separated-value
file.write("Position,Company,Location,URL\n")

for job in jobs:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()





