from transformers import pipeline
import transformers

import pandas as pd

model_dir = "./summarization_model"

class SummaryModel():
    def __init__(self):
        self.model = pipeline('summarization', model_dir)
    
    def summarize(self, text):
        text = f"summarize: {text}"
        summary = self.model(text)
        return summary[0]['summary_text']

def main():
    df = pd.read_json("./BillData.json", orient='index')
    text = df["BILL_TEXT"][3]
    print(df.shape)

    model = SummaryModel()
    text = model.summarize(text)

#    import pdb; pdb.set_trace()
    print(text)

if __name__ == "__main__":
    main()
