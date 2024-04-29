import numpy as np
import pandas as pd
import json

with open('./Notebooks/random_forest.ipynb') as json_file:
    data = json.load(json_file)

wordCount = 0
for each in data['cells']:
    cellType = each['cell_type']
    if cellType == "markdown":
        content = each['source']
        for line in content:
            temp = [word for word in line.split() if
                    "#" not in word]  # we might need to filter for more markdown keywords here
            wordCount = wordCount + len(temp)

print(wordCount)