from requests import get # requests package download
from bs4 import BeautifulSoup # BeautifulSoup package download
# bs4는 html tag들을 list, dictiionary와 같은 자료구조로 변환

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("detach", True)


   
count = 0
counting = True
keyword = input("What do you want to search for?")
browser = webdriver.Chrome(options=options) 



while counting != False:
    base_url="https://kr.indeed.com/jobs"
    final_url= f"{base_url}?q={keyword}&start={count*10}"
    browser.get(final_url)
        
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", class_="ecydgvn0")
    pages = pagination.find_all("div", recursive=False)

    if not pages:
        count = 1
        counting = False
    
    for page in pages:

        # 이전 페이지, 다음 페이지에 뒤에 더 갈 곳이 2페이지 이상 있을 때: 7
        # 이전 페이지, 다음 페이지에 뒤에 더 갈 곳이 1페이지 있을 때: 6
        # 첫 페이지이고 다음페이지 버튼 있을 때: 6
        # 마지막 페이지이고 다음 페이지 버튼 없고 이전 페이지만 있을 때: 4 


        page_btn = page.select_one("div button")

        
        
        if page_btn != None:
            page_num = int(page_btn.string)
            current_page = page_num- 1
            #print(f"current_page: {current_page}, count: {count}")
            if current_page != count:
                counting = False
                print(count)
                break
            count += 1


        


        
        
    #     if 
        
    #     last_page = page.select_one("div button")

    #     if last_page != None:

    #         tlast_page = page.select_one("div button")
    #         last_page_num = last_page.string
    #         if last_page_num != '1':
    #             print(last_page_num)
    #             counting = False
    
    # count += 1