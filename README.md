### Fine-Grained Spoiler Detection in Book Reviews: An Ensemble Approach Combining Classification and Listwise Ranking
---

#### Steps to run the code:

1. You can find the Goodreads dataset here - https://mengtingwan.github.io/data/goodreads.html.
In order to work with the code you need to download two datasets from the link above:
    - `goodreads_book_works.json.gz`
    - `goodreads_reviews_spoiler.json.gz`

2. Run `EDA.ipynb` for Exploratory data analysis

3. Run `prepare-csv.ipynb` first to generate the csv files before running the models.
 
4. The models are contained in their own .ipynb files:
    - `Baseline-Classifier.ipynb`: Contains baseline and improved baseline models. The baseline is a simple logistic classifier. Improved baseline makes use of engineered features.
    - `ListwiseRanking-Base.ipynb`: Contains LightGBM's LambdaRank Model trained on basic features
    - `ListwiseRanking-Improved.ipynb`: Contains LightGBM's LambdaRank Model trained on engineered features
    - `Ensemble.ipynb`: Contains an ensemble model combining classifier, LambdaRank, BERT embeddings, TF-IDF, engineered features.

#### Note: 
Helper classes are located in:
1. `reviewsdataset.py`: methods to subsamples a small representative dataset from the larger Goodreads review corpora
2. `reviewplot.py`: Visualization functions
3. `itemspecificity.py`: methods to compute item-specific features.