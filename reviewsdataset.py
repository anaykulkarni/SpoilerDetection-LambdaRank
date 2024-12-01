import gzip
import json
import random

def getReviews():
    reviews = []
    for l in gzip.open("goodreads_reviews_spoiler.json.gz"):
        obj = json.loads(l.decode('utf-8'))
        if obj['has_spoiler'] and obj['book_id'] in metadata:
            reviews.append(obj)
        if len(reviews) >= 10000:
            break
    return reviews

def getBookMetadata():
    metadata = {}
    for l in gzip.open('goodreads_book_works.json.gz'):
        obj = json.loads(l.decode('utf-8'))
        if obj['original_title'].strip():
            metadata[obj['best_book_id']] = obj['original_title']
    return metadata

def loadBatch(review):
    batch = []
    spoilers = []
    nonspoilers = []
    for position, sent in enumerate(review['review_sentences']):
        if sent[0] == 0:
            nonspoilers.append((sent[1], position))
        else: 
            spoilers.append((sent[1], position))
    if len(nonspoilers) == 0:
        return []
    for sent in spoilers:
        batch.append((sent[0], metadata[review['book_id']], 1, sent[1]))
        negative_sample = random.sample(nonspoilers, k=1)[0]
        batch.append((negative_sample[0], metadata[review['book_id']], 0, negative_sample[1]))
    return batch

def loadBatchListwise(review, i):
    batch = {'sentences': [], 'contexts': [], 'labels': [], 'positions': [], 'reviewid': [], 'bookid': []}
    sentences = review['review_sentences']
    # prev = 0
    # nxt = 0
    for position, sent in enumerate(sentences):
        # nxt = sentences[position+1][0] if position+1 < len(sentences) else 0 # check if next sentence is a spoiler
        # prev = sentences[position-1][0] if position>0 else 0 # check if prev sentence is a spoiler
        batch['sentences'].append(sent[1])
        batch['contexts'].append(metadata[review['book_id']])
        batch['labels'].append(sent[0])
        batch['positions'].append(position)
        batch['reviewid'].append(i)
        batch['bookid'].append(review['book_id'])
        # batch['neighbours'].append(prev+nxt)
    return batch

def loadDataset():
    dataset = []
    for r in reviews:
        batch = loadBatch(r)
        if len(batch) > 1:
            dataset.extend(batch)
    return dataset

metadata = getBookMetadata()
reviews = getReviews()