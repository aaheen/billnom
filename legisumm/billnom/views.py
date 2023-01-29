from django.shortcuts import render
from django.urls import path
from django.views.generic import RedirectView
from . import views
import os
import json
from django.conf.urls.i18n import i18n_patterns 
from transformers import pipeline
import transformers
mydir = os.path.dirname(__file__) or "."
import pandas as pd

model_dir = os.path.join(mydir,"model/summarization_model")
with open(os.path.join(mydir,"model/BillData.json"), "r") as read_content:
    billData = json.load(read_content)

with open(os.path.join(mydir,"model/UrlIndex.json"), "r") as read_content:
    urlind = json.load(read_content)


df = pd.read_json(os.path.join(mydir,"model/BillData.json"), orient='index')
placey = df["BILL_TEXT"][3]

class SummaryModel():
    def __init__(self):
        self.model = pipeline('summarization', model_dir)
    
    def summarize(self, text):
        text = f"summarize: {text}"
        summary = self.model(text)
        return summary[0]['summary_text']

def urlIndex(url):
    if url == '':
        return billData["HF366"]["BILL_TEXT"]
    BID = urlind[url]

    return billData[BID]["BILL_TEXT"]

def BillSumm(text=placey):
    print(df.shape)

    model = SummaryModel()
    text = model.summarize(text)

#    import pdb; pdb.set_trace()
    return text



# Create your views here.
def indexbase(request):
    return render(request, 'billnom/index.html',{})

def retsumm(request):
    print(request)
    reqUrl = request.GET.get("E0")
    print(reqUrl)
    return render(request, 'billnom/billTex.html', {"Summary" :BillSumm(urlIndex(reqUrl))})
