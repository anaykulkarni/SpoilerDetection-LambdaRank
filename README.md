### Fine-Grained Spoiler Detection in Book Reviews: An Ensemble Approach Combining Classification and Listwise Ranking
---

You can find the Goodreads dataset here - https://mengtingwan.github.io/data/goodreads.html

Run EDA.ipynb for Exploratory data analysis

Run prepare-csv.ipynb first to generate the csv files before running the models.
 
The models are contained in their own .ipynb files:
1. Baseline-Classifier.ipynb
2. ListwiseRanking-Base.ipynb
3. ListwiseRanking-Improved.ipynb
4. Ensemble.ipynb

Helper classes are located in:
1. reviewsdataset.py
2. reviewplot.py
3. itemspecificity.py