from bs4 import BeautifulSoup
from requests import get
from selenium import webdriver

def wanted_find(keyword):
    base_url = f"https://www.wanted.co.kr/search?query={keyword}"
    response = get(base_url)
    driver = webdriver.Chrome()
    driver.get(base_url)
    results=[]
    if response.status_code != 200:
        print("Can't respond")
    else : 
        soup = BeautifulSoup(driver.page_source, "html.parser")
        job_lists = soup.find_all("div", class_="List_List_container__JnQMS")
        for job_list in job_lists:
            li_lists = job_list.find_all("li")
        for li_list in li_lists:
            anchors = li_list.select_one("div a")
            link = f"https://www.wanted.co.kr{anchors['href']}"
            job_position = li_list.find("div", class_="job-card-position")
            company = li_list.find("div", class_="job-card-company-name")
            location = li_list.find("div", class_="job-card-company-location")
            all_done ={
                "company": company.string,
                "position": job_position.string,
                "location": location.text,
                "link": link
            }
            results.append(all_done)
    return results

print(wanted_find("python"))