from requests import get
from bs4 import BeautifulSoup


BASE_URL = "https://www.warframe.com"
URL = f"{BASE_URL}/uk/game/warframes"
HEADERS = {
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
FILE_NAME = "lab1.txt"
with open(FILE_NAME, "w", encoding="utf-8") as file:
   page = get(URL, headers=HEADERS)
   soup = BeautifulSoup(page.content,  "html.parser")
   wf_list1 = soup.find(name="div", class_="row").find_all(class_="wf")
   wf_list = wf_list1 + (soup.find(name="div", class_="row").find_all(class_="primewf"))
   n = 1

   for wf in wf_list:
       wf_name = wf.find(name="div", class_="innerWfTitle").find(string=True, recursive=False).strip()
       wf_url = BASE_URL + wf.get("href")

       print(f"{n}: {wf_name}")
       print(f"URL: {wf_url}")

       file.write(f"{n}: {wf_name}")
       file.write(f"URL: {wf_url}")

       n += 1

