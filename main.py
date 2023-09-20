from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from extractors.incruit import extract_incruit_jobs
from extractors.saramin import extract_saramin_jobs
#from extractors.wanted import extract_wanted_jobs

from file import save_to_file


keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
incruit = extract_incruit_jobs(keyword)
saramin = extract_saramin_jobs(keyword)

jobs = indeed + wwr + incruit + saramin

save_to_file(keyword, jobs)



"""
wanted = extract_wanted_jobs(keyword)
wanted 왜 jobs이 8개밖에 안뜨는지 모르겠음



challengevb
part 1. 다른 구직 사이트로 가서 자신만의 추출기 만들어보기
part 1. incruit (requests 사용) 완료 - 매우 미흡
태그를 불러올 때 클래스명을 활용하지 않고 태그 순서로 불러와 예외인 경우가 발생하여 오류 발생
밑의 링크를 통해 클래스명을 활용하여 추출하는 방법 터득. + get_text()
https://replit.com/@rorodeuni/Scrapper#extractors/MyChallenge.py 참고해서 공부하기
part 1. saramin (selenium 사용) 완료 
part 1. wanted (selenium 사용) 무한 스크롤 적용하기: jobs가 8개밖에 안뜸 모르겠음

part 2. indeed에서 10개의 페이지를 스크랩 할 수 있는지 확인하고 시도
part 2. indeed 맨 끝까지 스크랩 할 수 있는 코드 구현
마지막 페이지에서 더 갈 수 있다면 오류 발생
Flask는 Python을 이용해서 웹사이트를 구축할 수 있는 초소형 micro framework
"""

