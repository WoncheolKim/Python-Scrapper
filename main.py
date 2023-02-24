from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

def get_page_count(keyword):
  base_url = "https://ca.indeed.com/jobs?q="
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Can't request page")
  else:
    soup = BeautifulSoup(response.text, "html.parser")
    pagination = soup.find("ul", class_="pagination-list")
    if pagination == None:
      return 1
    pages = pagination.find_all("li", recursive=False)
    count = len(pages)
    if count >= 5:
      return 5
    else:
      return count


def extract_indeed_jobs(keyword):
  base_url = "https//ca.indeed.com/jobs?q="
  response = get(f"{base_url}{keyword}")
  if response.status_code != 200:
    print("Cant request page")
  else:
    results = []
    soup = BeautifulSoup(response.text, "thml.parser")
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all('li', recursive=False)
    print(len(jobs))
    for job in jobs:
      zone = job.find("div", class_="mosaic-zone")
      if zone == None:
        anchor = job.select_one("h2 a")
        title = anchor['aria-label']
        link = anchor['href']
        company = job.find("span", class_="companyName")
        location = job.find("div", class_="companyLocation")
        job_data = {
          'link': f"https://ca.indeed.com{link}",
          'company': company.string,
          'location': location.string,
          'position': title
        }
        results.append(job_data)
    for result in results:
      print(result, "\n//////\n")