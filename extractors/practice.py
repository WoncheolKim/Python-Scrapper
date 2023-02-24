from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options = options)

#페이지가 있는지 없는지 확인하는 함수를 만든것. 단지 selenium을 써서 컴퓨터가 사람이 한것처럼 만든것
#그리하여 명령어가 달라짐. 참고할것!
def get_page_count(keyword):
  base_url = "https://kr.indeed.com/jobs?q="
  browser.get(f"{base_url}{keyword}")
  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find('nav', class_="css-jbuxu0 ecydgvn0")
  if pagination == None:
    return 1
  pages = pagination.find_all('div', recursive = False)
  count = len(pages)
  if count >= 10:
    return 10
  else:
    return count

# print(get_page_count("python"))
# print(get_page_count("next.js"))
# print(get_page_count("django"))
# print(get_page_count("nest"))
#위의 print를 하면 web 을 검사하여 몇개의 page가 있는지 확인하여 숫자로 출력한다.!


# print(browser.page_source)
def extract_indeed_jobs(keyword):
  pages = get_page_count(keyword)

results = []


for page in range(10): #위의 페이지는 list가 아니기에 range로 list를 만들어준다!
  base_url = "https://kr.indeed.com/jobs"
  final_url = f"{base_url}?q={keyword}&start={page*10}"
  print(f"page:{page}")
  print("Found", page, "pages")
  print("Requesting", final_url)

browser.get(final_url)
response = browser.page_source

soup = BeautifulSoup(browser.page_source, "html.parser")

job_list = soup.find('ul', class_= "jobsearch-ResultsList")
jobs = job_list.find_all('li', recursive = False)
#ul 바로밑 li만을 찾아낼 것이다
for job in jobs:
  zone = job.find("div", class_="mosaic-zone")
#find는 찾은 element를 주거나 None을 준다
if zone == None:#job li에서 job을 추출한다
  anchor = job.select_one("h2 a")
  title = anchor['aria-label']
  link = anchor['href']
  company = job.find("span",class_="companyName")
  location = job.find("div",class_="companyLocation")
  job_data = {
  'link' : f"https://kr.indeed.com{link}",
  'company' : company.string.replace(","," "),
  'location' : location.string.replace(","," "), #가끔 ,를 출력물이 가지고 있으면 겹치기때문에 replace 사용하여 없애준다.
  'position' : title.replace(","," "),
  }
  results.append(job_data)
return results