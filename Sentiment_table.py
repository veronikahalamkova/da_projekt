# %%
import pandas as pd
from datetime import datetime, date, timedelta
import os
import glob
from difflib import get_close_matches
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from scipy.sparse import csr_matrix
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sparse_dot_topn.sparse_dot_topn as ct

# %%

## creating a dataframe with name variations for SP500 stocks

stock_industries_file = os.path.join("output\sp500\industries", "sp500_industries.csv")
df_industries = pd.read_csv(stock_industries_file)
#df_industries.head(20)
sp500_names=df_industries.loc[:,["ticker", "longName"]]

# %%

unofficial_name=[]

for name in sp500_names["longName"]:
    x=name.rstrip("Inc.").rstrip("plc").rstrip("Incorporated").rstrip("Corporatio").strip().rstrip(",")
    unofficial_name.append(x)

sp500_names["unofficial_name"]= unofficial_name

#%%

sp500_names.head(20)

# %%

### specifying the date range for the sentiment analysis

sdate = date(2020, 3, 1)   # start date
edate = date(2020, 10, 1)   # end date

delta = edate - sdate       # as timedelta


date_list= []
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    date_list.append(day)
    #print(day)

#print(date_list)

len(date_list)

# %%

### merging all file names in the above-specified date range into one list

all_files = []
for date in date_list:
    path = f"results\{date}"
    all_files.append(glob.glob(path + "\*.txt"))

print(all_files)

# %%

### merging all text into one list

text=[]

for file_block in all_files:
    for filename in file_block:
        df = open(filename)
        rows = [row for row in df]
        df.close()
        text.append(rows)
        
print(text)

# %%

### merging all article headlines into one list

names=[]

for file_block in all_files:
    for filename in file_block:
        name=filename.split("\\")[2].rstrip(".txt")
        names.append(name)
        
#print(names)

# %%

### merging all articles dates into one list

dates=[]

for file_block in all_files:
    for filename in file_block:
        date=filename.split("\\")[1]
        dates.append(date)
        
print(dates)

# %%

### creating a dictionary with the article headline, date and article text

dict=[]
for n, d, t in zip(names, dates, text):
    dict_x={"name":n, "date":d, "text":t}
    dict.append(dict_x)

print(dict)


# %%

### converting the dictionary into a dataframe

df_news=pd.DataFrame(dict, columns=["name", "date", "text"])

# %%

df_news.head(30)

# %%
# Sentiment Analysis
analyzer = SentimentIntensityAnalyzer()

scores = df_news["text"].apply(analyzer.polarity_scores).tolist()

df_scores = pd.DataFrame(scores)
df_news = df_news.join(df_scores, rsuffix='_right')


# %%

df_news.head(20)

# %%

#creating a matrix of company vs article

company_columns = sp500_names["ticker"]

for col in company_columns:
    df_news[col] = 0

# %%

df_news.head(20)

# %%%

def ngrams(string, n=3):
    string = re.sub(r'[,-./]|\sBD',r'', string)
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]

ngrams("Apple")

# %%

company_names = sp500_names["unofficial_name"]
article_headlines=df_news["name"]
vectorizer = TfidfVectorizer(min_df=1, analyzer=ngrams)
tf_idf_matrix = vectorizer.fit_transform(article_headlines)
query_vec=vectorizer.transform(company_names)

# %%

print(tf_idf_matrix[0])

# %%

results = cosine_similarity(tf_idf_matrix,query_vec)
print(results)

# %%

def cossim_top_similarity(A, B, ntop, lower_bound=0):
    # force A and B as a CSR matrix.
    # If they have already been CSR, there is no overhead
    A = A.tocsr()
    B = B.tocsr()
    M, _ = A.shape
    _, N = B.shape
 
    idx_dtype = np.int32
 
    nnz_max = M*ntop
 
    indptr = np.zeros(M+1, dtype=idx_dtype)
    indices = np.zeros(nnz_max, dtype=idx_dtype)
    data = np.zeros(nnz_max, dtype=A.dtype)

    ct.sparse_dot_topn(
        M, N, np.asarray(A.indptr, dtype=idx_dtype),
        np.asarray(A.indices, dtype=idx_dtype),
        A.data,
        np.asarray(B.indptr, dtype=idx_dtype),
        np.asarray(B.indices, dtype=idx_dtype),
        B.data,
        ntop,
        lower_bound,
        indptr, indices, data)

    return csr_matrix((data,indices,indptr),shape=(M,N))

# %%

t1 = time.time()
matches = cossim_top_similarity(tf_idf_matrix, query_vec, 10, 0.8)
t = time.time()-t1

# %%

print("SELFTIMED:", t)

# %%
def get_matches_df(sparse_matrix, name_vector, top=100):
    non_zeros = sparse_matrix.nonzero()
    
    sparserows = non_zeros[0]
    sparsecols = non_zeros[1]
    
    if top:
        nr_matches = top
    else:
        nr_matches = sparsecols.size
    
    left_side = np.empty([nr_matches], dtype=object)
    right_side = np.empty([nr_matches], dtype=object)
    similairity = np.zeros(nr_matches)
    
    for index in range(0, nr_matches):
        left_side[index] = name_vector[sparserows[index]]
        right_side[index] = name_vector[sparsecols[index]]
        similairity[index] = sparse_matrix.data[index]
    
    return pd.DataFrame({'left_side': left_side,
                          'right_side': right_side,
                           'similairity': similairity})
        

# %%

matches_df = get_matches_df(matches, company_names, top=100000)
matches_df = matches_df[matches_df['similairity'] < 0.99999] # Remove all exact matches
matches_df.sample(20)

# %%

# %%
