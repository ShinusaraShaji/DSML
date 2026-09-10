import requests
from bs4 import BeautifulSoup
URL="https://realpython.github.i0/fake-jobs/"
page=requests.get(URL)
print(page.text)
soup=BeautifulSoup(page.content,"html.parser")
results=soup.find(id="ResultsContainer")
job_elements=results.find_all("div",class_="card-copntent")
for job_elents in job_elements:
    title_element=job_elements.find("h2",class_="title")
    company_element=job_elements.find("h3",class_="company")
    location_element=job_elements.find("p",class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print()