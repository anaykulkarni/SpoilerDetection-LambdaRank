import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
import string
import math
from collections import defaultdict
nltk.download('stopwords')
nltk.download('punkt')

sw = stopwords.words('english')
sp = string.punctuation

def getItemSpecificity(reviews):
    reviewsByBookID = defaultdict(list)
    for review in reviews:
        reviewsByBookID[review['book_id']].append(review)
        
    itemwise_word_freq = {}
    corpuswise_word_freq = defaultdict(int)

    total_terms_in_corpus = 0
    for bookid in reviewsByBookID:
        total_terms_in_book = 0
        itemwise_word_freq[bookid] = {}
        for r in reviewsByBookID[bookid]:
            sentences = r['review_sentences']
            words = [word for sent in sentences for word in sent[1].split() if word.lower() not in sw]
            cleaned_words = [''.join([c for c in word if c not in sp]) for word in words if len(word)>1]
            for w in cleaned_words:
                if w in itemwise_word_freq[bookid]:
                    itemwise_word_freq[bookid][w] += 1
                else:
                    itemwise_word_freq[bookid][w] = 1
                corpuswise_word_freq[w] += 1 
            total_terms_in_book += len(cleaned_words)
            total_terms_in_corpus += len(cleaned_words)
        for w in itemwise_word_freq[bookid]:
            itemwise_word_freq[bookid][w] /= total_terms_in_book
    
    for w in corpuswise_word_freq:
        inv_freq = total_terms_in_corpus/corpuswise_word_freq[w]
        corpuswise_word_freq[w] = math.log10(inv_freq)
        
    return itemwise_word_freq, corpuswise_word_freq