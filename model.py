from transformers import pipeline
import transformers

import pandas as pd

model_dir = "./summarization_model"

class SummaryModel():
    def __init__(self):
        self.model = pipeline('summarizer', model_dir)
    
    def summarize(self, text):
        summary = self.model(text)

if __name__ == "__main__":
    main()
        
