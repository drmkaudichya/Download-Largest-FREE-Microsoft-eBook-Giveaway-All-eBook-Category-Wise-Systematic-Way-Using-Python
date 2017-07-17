import urllib.request
import requests
import urllib
from bs4 import BeautifulSoup
import os
import os.path
import urllib.request
import re

#Code By Milind Audichya on 10:55 PM 17-07-2017
#To download all ebooks of Largest FREE Microsoft eBook Giveaway!
# I’m Giving Away code to download MILLIONS of FREE Microsoft eBooks again.
# including: Windows 10, Office 365, Office 2016, Power BI, Azure, Windows 8.1, Office 2013, SharePoint 2016, SharePoint 2013, Dynamics CRM, PowerShell, Exchange Server, System Center, Cloud, SQL Server and more!

# Variables
mainweburl = "https://blogs.msdn.microsoft.com/mssmallbiz/2017/07/11/largest-free-microsoft-ebook-giveaway-im-giving-away-millions-of-free-microsoft-ebooks-again-including-windows-10-office-365-office-2016-power-bi-azure-windows-8-1-office-2013-sharepo/"
rootdirectory = "D:/Microsoft-eBooks"
page = urllib.request.urlopen(mainweburl)
soup = BeautifulSoup(page, "html.parser")
all_tables = soup.find_all('table')
table = soup.find('table')
rows = table.find_all('tr')
Link = {}
cnt = 0


# Method to download file from url to a specific path
def download_file(url, path):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                # f.flush()
    print("Download Complete! @ " + path)
    # return path


# Creating Root Directory
if not os.path.exists(rootdirectory):
    os.makedirs(rootdirectory)

for row in rows:
    data = row.find_all("td")
    # Fetching and creating categories and their directories
    Category = data[0].get_text()
    if not os.path.exists(rootdirectory + "/" + Category):
        os.makedirs(rootdirectory + "/" + Category)

    Title = data[1].get_text()
    Format = data[2].get_text()
    tag = data[2].find_all("a")
    for i in tag:
        try:
            ext = str(i.find("font").get_text())
            if ext == "DOC":
                ext = "docx"
        except:
            ext = ""
        downloadfilename = rootdirectory + "/" + Category + "/" + re.sub('[/:,]', '.', Title) + "." + ext
        cnt += 1
        if not os.path.isfile(downloadfilename):
            download_file(i['href'], downloadfilename)
print("Thank you downloading " + str(cnt) + "+ books using my script DownloadMicosoftGiveAWayeBooks.py")
print("Please show your love by getting connected with me on social platforms : \n https://www.youtube.com/channel/UCu9usLXJYLBAA7ccAdDIVRg \n https://www.facebook.com/MilindKumarAudichya")
print(" https://www.instagram.com/milindaudichya/ \n https://twitter.com/milindaudichya")
