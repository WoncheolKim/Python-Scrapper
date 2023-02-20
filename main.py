from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

base_url = "https//ca.indeed.com/jobs?q="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
  print("Cant request page")
else:
  soup = BeautifulSoup(response.text, "thml.parser")
  job_list = soup.find("ul", class_="jobsearch-ResultsList")
  jobs = job_list.find_all('li', recursive=False)
  print(len(jobs))
  for job in jobs:
    print(job)
    print("//////////")