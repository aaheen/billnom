# Bill Nom
> Legislation summarization tool for the Minnesota State Legislature

## Structure
NLP model is using the T5 model from Google, imported from [Huggingface](https://huggingface.co/), fine-tuned on legislative language from documents obtained from the [MN Revisor's Office](https://www.revisor.mn.gov/). Front-end built using [Dash by Plotly](https://dash.plotly.com/). API is in Python.

## Authors
- [Andrew Amakye Ansah (aikenfell)](https://github.com/aikenfell) - Data mining & web scraping
- [Erik Heen (eaheen)](https://heen.dev/) - API, front end
- [Ling Long (tardism)](https://github.com/tardism) - API, front end, Android app
- [Aaron Mead (ronofays)](https://github.com/ronofays) - NLP, API

## References

### Applications
- https://huggingface.co/
- https://beautiful-soup-4.readthedocs.io/en/latest/
- https://dash.plotly.com/

### Research
- https://huggingface.co/
- https://github.com/karpathy/nanoGPT
- https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html
- https://arxiv.org/pdf/1706.03762.pdf

### Data Sources
- https://www.revisor.mn.gov/
- https://www.leg.mn.gov/leg/legis
