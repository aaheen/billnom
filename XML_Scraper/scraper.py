import requests
import xml
import lxml
import json
from bs4 import BeautifulSoup
import time

retDict = {}

i = 0
x = 1
for num in range(1150,1500):
    print(num)

    session = "0932023"
    session = "0932023"
    reqString = "https://www.revisor.mn.gov/bills/status_result.php?"
    reqString += "body=House&"
    reqString += "search=basic&"
    reqString += "session="+"&"
    reqString += "location=House&"
    reqString += "bill=&"
    reqString += "bill_type=bill&"
    reqString += "rev_number=&"
    reqString += "keyword_type=all&"
    reqString += "keyword=&"
    reqString += "keyword_field_text=1&"
    reqString += "author1%5B%5D=&"
    reqString += "author%5B%5D=&"
    reqString += "topic%5B%5D="+str(num)+"&"

    reqString += "submit_topic=GO&"
    reqString += "committee%5B%5D=&"
    reqString += "action%5B%5D=&"
    reqString += "titleword=&"
    reqString += "format=xml"


    XMLresponse = requests.get(reqString)

    # with open("Stage1.xml", "w") as f:
    #     f.write(XMLresponse.text) 

    # with open('Stage1.xml', 'r') as f:
    #     XMLresponse = f.read()
    Stage2 = BeautifulSoup(XMLresponse.text, 'xml')

    i+=1
    for tag in Stage2.find_all('BILL_RESULT'):
        BID = tag.find('FILE_TYPE').text+tag.find('FILE_NUMBER').text

        tempDict = {}
        # tempDict.update({"FILE_TYPE" : })
        tempDict.update({"DESCRIPTION" : tag.find('DESCRIPTION').text})
        tempDict.update({"BILL_URL" : tag.find('LATEST_TEXT_HTML_URI').text})

        HTMLresponse = requests.get("https://"+tag.find('LATEST_TEXT_HTML_URI').text)
        Stage4 = BeautifulSoup(HTMLresponse.text, 'lxml')
        BillTex = ""
        for tag in Stage4.find_all('ins'):
            BillTex += tag.text+"\n"

        tempDict.update({"BILL_TEXT" : BillTex})

        retDict.update({BID : tempDict})

    time.sleep(1)
    if i >= 50:
        with open("BillData"+str(i*x)+".json", "w") as outfile:
            json.dump(retDict, outfile, indent=4)
            retDict = {}
            i = 0
            x += 1


    # with open('Stage3.html', 'w') as f:
    #     f.write(HTMLresponse.text) 

    # with open('Stage3.html', 'r') as f:
    #     htmlresponse = f.read()


with open("BillData.json", "w") as outfile:
    json.dump(retDict, outfile, indent=4)
