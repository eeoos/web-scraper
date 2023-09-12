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
#wwr = extract_wwr_jobs(keyword)

#jobs = indeed + wwr

for job in indeed:
    print(job)
    print('////\n////')