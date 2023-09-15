from requests import get # requests package download
from bs4 import BeautifulSoup # BeautifulSoup package download
# bs4는 html tag들을 list, dictiionary와 같은 자료구조로 변환

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


indeed는 request를 사용하면 403을 반환하기 때문에 브라우저를 생성해서 들어가는 방법을 사용
여기서는 chrome을 생성하여 indeed에 접근 (봇으로 잡히지 않음)

"""

def get_page_count(keyword):

    
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=options) 

    base_url="https://kr.indeed.com/jobs?q="
    browser.get(f"{base_url}{keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", class_="ecydgvn0")
    pages = pagination.find_all("div", recursive=False) # recursice=False: 바로 밑에 있는 것만 추출
    if not pages: # 페이지 수가 0이라면 함수 종료
        return 1
    
    count = len(pages) # 페이지 수
    if count >= 5:
        return 5
    else:
        return count

def extract_indeed_jobs(keyword):

    
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=options)
    
    pages = get_page_count(keyword)
    

    print("Found", pages, "pages (indeed)")
    results = []

    for page in range(pages):    
  
        base_url="https://kr.indeed.com/jobs"
        final_url= f"{base_url}?q={keyword}&start={page*10}"
        browser.get(final_url)
        print("Requesting", final_url)
        
        soup = BeautifulSoup(browser.page_source, "html.parser")

        

        job_list = soup.find("ul", class_="css-zu9cdh")
        jobs = job_list.find_all('li', recursive=False) # recursive-False를 통해 ul 바로 밑에 있는 li만 추출

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                #h2 = job.find("h2", class_="jobTitle")
                #a = h2.find("a",) find 함수 대신 select 함수 사용
                anchor = job.select_one("h2 a") # select 함수에서는 CSS s   elector 사용 가능, h2 내부의 a를 추출
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    'link':f"https://kr.indeed.com{link}",
                    'company':company.string.replace(",", " "),
                    'location':location.string.replace(",", " "),
                    'position':title.replace(",", " "),
                }

                results.append(job_data)
    return results  

    while True:
        pass




        #while True: # 크롬 자동 종료 방지 코드
        #    pass
