import pandas as pd
import re

df = pd.read_csv('malicious_phish.csv')
from collections import Counter

vocabulary = {
  'benign':     Counter(),
  'phishing':   Counter(),
  'defacement': Counter(),
  'malware':    Counter()
}

for row in df.iterrows():
  url      = row[1]['url']
  category = row[1]['type']
  vocab    = vocabulary[category]
  words    = re.findall(r'[a-z]+', url)
 
  for word in words:
    vocab[word] += 1
   
print(vocabulary['malware'].most_common(10))
print(vocabulary['phishing'].most_common(10))
print(vocabulary['defacement'].most_common(10))
print(vocabulary['benign'].most_common(10))

most_common = {
  'benign':     float(vocabulary['benign'].most_common(1)[0][1]),
  'phishing':   float(vocabulary['phishing'].most_common(1)[0][1]),
  'defacement': float(vocabulary['defacement'].most_common(1)[0][1]),
  'malware':    float(vocabulary['benign'].most_common(1)[0][1])
}

word_factors = {
  'benign':     Counter(),
  'phishing':   Counter(),
  'defacement': Counter(),
  'malware':    Counter()
}

factors   = word_factors['benign']
max_count = most_common['benign']
for word, count in vocabulary['benign'].items():
  factors[word] = count / max_count
 
benign_factor     = word_factors['benign']
benign_min_factor = 1.0 / most_common['benign']
for category in ['phishing', 'defacement', 'malware']:
  factors   = word_factors[category]
  max_count = most_common[category]
   
  for word, count in vocabulary[category].items():
    if word in benign_factor:
      factors[word] = (count / max_count) / benign_factor[word]
    else:
      factors[word] = (count / max_count) / benign_min_factor
   
print(word_factors['malware'].most_common(10))
print()
print(word_factors['phishing'].most_common(10))
print()
print(word_factors['defacement'].most_common(10)) 