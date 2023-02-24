from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

<<<<<<< HEAD
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

=======
keyword = input("What do you want to search for? ")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr
>>>>>>> 7cb4498a28aa2b527ae210e54bf17113b8970c83

file = open(f"{keyword}.csv", "w")
file.write("Position,Company,Location,URL\n")

for job in jobs:
  file.write(f"{job['position']},{job['company']},{job['location']},{job['link']}\n")


file.close()
