from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_page_count(keyword):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=options)

    base_url = "https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword="
    browser.get(f"{base_url}{keyword}")

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("div", class_="pagination")
    pages = pagination.find_all("a", recursive=False)
    if not pages:
        return 1
    count = len(pages)
    if count >= 10:
        return 10
    else:
        return count




def extract_saramin_jobs(keyword):

    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("detach", True)

    browser = webdriver.Chrome(options=options)
    pages = get_page_count(keyword)

    print("Found", pages, "pages (saramin)")
    results = []

    for page in range(pages):


        base_url = "https://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=search&searchword="
        
        url = f"{base_url}{keyword}&recruitPage={page+1}"
        browser.get(url)
        print("Requesting", url)
        
        soup = BeautifulSoup(browser.page_source, "html.parser")

        job_list = soup.find("div", class_="content")
        jobs = job_list.find_all('div', recursive=False)

        for job in jobs:
            area_job = job.find("div", class_="area_job")
            anchor = area_job.select_one("h2 a")
            link = anchor['href']
            title = anchor['title']

            job_condition = job.find("div", class_="job_condition")
            spans = job_condition.find_all("span")
            location = spans[0].get_text()
            
            corp_name = job.find("strong", class_="corp_name")
            company = corp_name.find("a")

            job_data = {
                            'link':f"https://www.saramin.co.kr{link}",
                            'company':company.string.replace(" ", "").replace("\n", ""),
                            'location':location.replace(",", " "),
                            'position':title.replace(",", " "),
                        }

            results.append(job_data)
            
    return results

