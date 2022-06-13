from ipaddress import v4_int_to_packed
import transformers
import torch

from transformers import RobertaTokenizer, RobertaForSequenceClassification

tokenizer = RobertaTokenizer.from_pretrained("pdelobelle/robBERT-dutch-books")
model = RobertaForSequenceClassification.from_pretrained("pdelobelle/robBERT-dutch-books")
v4_int_to_packed
inputfile = "D:\\I&E 2021-2022\\thesis\\Thesis_69_respondenten.csv"
CompList = []

test = "Dit is echt goed"

inputs = tokenizer(test, return_tensors="pt")
print(inputs)
outputs = model(**inputs)
pred_logits = outputs.logits
probs = pred_logits.softmax(dim=-1).detach().cpu().flatten().numpy().tolist()


print(probs)