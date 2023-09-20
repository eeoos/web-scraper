from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

def extract_wanted_jobs(keyword):

    options = Options()
    options.add_argument("-no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    #options.add_argument('--start-maximized')

    options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=options)

    results = []

    base_url = "https://www.wanted.co.kr"
    
    url = f"{base_url}/search?query={keyword}&tab=position"

    
    scrollPage(browser, url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
            
    job_list = soup.find("div", class_="JobList_container__Z19Mc")  
    jobs= job_list.find_all('div', class_="JobCard_container__FqChn")

    for job in jobs:

        anchor = job.find("a")
        link = anchor['href']
 
        area_job = job.find("div", class_="JobCard_content__5mZPT")
        
        position = area_job.find("strong", class_="JobCard_title__ddkwM")



        company_content = job.find("span", class_="JobCard_companyContent__zUT91")
        company = job.find("span", class_="JobCard_companyName__vZMqJ")
        location = job.find("span", class_="JobCard_location__2EOr5")

        
        job_data = {
                    'link':f"https://www.wanted.co.kr{link}",
                    'company':company.string.replace(",", " "),
                    'location':location.string.replace(",", " "),
                    'position':position.string.replace(",", " "),
                    }
        results.append(job_data)
    return results

def scrollPage(browser, url):
    
    browser.get(url)
    #스크롤 내리기 이동 전 위치
    scroll_location = browser.execute_script("return document.body.scrollHeight")

    while True:
        #현재 스크롤의 가장 아래로 내림
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        
        #전체 스크롤이 늘어날 때까지 대기
        time.sleep(2)
        
        #늘어난 스크롤 높이
        scroll_height = browser.execute_script("return document.body.scrollHeight")

        #늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
        if scroll_location == scroll_height:
            break
            
        #같지 않으면 스크롤 위치 값을 수정하여 같아질 때까지 반복
        else:
            #스크롤 위치값을 수정
            scroll_location = browser.execute_script("return document.body.scrollHeight")

        #같지 않으면 스크롤 위치 값을 수정하여 같아질 때까지 반복
        # else:
        #     #스크롤 위치값을 수정
        #     scroll_location = browser.execute_script("return document.body.scrollHeight")


keyword = input("What do you want to search for?")

wanted = extract_wanted_jobs(keyword)
# wwr = extract_wwr_jobs(keyword)
# incruit = extract_incruit_jobs(keyword)
# saramin = extract_saramin_jobs(keyword)

#jobs = indeed + wwr + incruit + saramin

# wanted = extract_wanted_jobs(keyword)
# wanted 왜 jobs이 8개밖에 안뜨는지 모르겠음

file = open(f"{keyword}.csv", "w", encoding="utf-8-sig") # CSV: comma-separated-value
file.write("Position,Company,Location,URL\n")

for job in wanted:
    file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")

file.close()
# 포기 개빡치네
