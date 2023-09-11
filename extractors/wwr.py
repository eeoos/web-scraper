from requests import get # requests package download
from bs4 import BeautifulSoup # BeautifulSoup package download

def extract_wwr_jobs(keyword):
  
  base_url = "https://weworkremotely.com/remote-jobs/search?term="
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Can't request website")
  else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser")
    #BeautifulSoup: 얻은 html 코드를 다룰 수 있는 python entity로 변환
    #response.text: 얻은 웹사이트의 코드를 줌
    
    jobs = soup.find_all('section', class_="jobs")
    #response.text 안의 jobs이라는 클래스명을 가진 section 태그를 불러옴
    for job_section in jobs:
      job_posts = job_section.find_all('li')
      job_posts.pop(-1)
      #job_post가 아닌 마지막에 있는 view-all을 pop(-1)을 통해 제거
      for post in job_posts:
        anchors = post.find_all('a')
        anchor = anchors[1] # 2개의 anchor 중 2번째 것을 얻음
        link = anchor['href']
        company, kind, region = anchor.find_all('span', class_="company") # anchor 내부의 클래스명이 company인 모든 span을 찾음
        # 3개의 span이 순서대로 company, kind, region에 핟당
        title = anchor.find('span', class_='title')
        # anchor 내부의 클래스명이 title인 모든 span을 찾음
        # find_all: 찾은 모든 것들을 list로 줌
        # find: 기준에 맞는 첫번째 하나의 항목만 줌
        job_data = {
          'link': f"https://weworkremotely.com{link}",
          'company' :company.string,
          'region': region.string,
          'position' : title.string
          #.string을 사용하지 않으면 <span class="title">title here</span>과 같이 출력되어짐
          #.string: 태그 안에 있는 텍스트를 줌 title here
        }
        results.append(job_data)
        # new job 데이터를 append 함수로 job_data에 추가 할당
    return results