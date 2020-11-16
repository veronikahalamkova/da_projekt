# %%
import pandas as pd
from datetime import datetime, date, timedelta
import os
import glob
from difflib import get_close_matches
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 

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

#news_company_dict=[]

for article in df_news["text"]:
    for company in sp500_names["unofficial_name"]:
        if company in article:
            print(article)
        else:
            pass

#print(news_company_dict)

# %%

#using get_close_matches
for word in df_news["text"].split():
    match = get_close_matches(word, company_name, n=1, cutoff=.4)
    print(match)

# %%
# Sentiment Analysis
analyzer = SentimentIntensityAnalyzer()

scores = df_news["text"].apply(analyzer.polarity_scores).tolist()

df_scores = pd.DataFrame(scores)
df_news = df_news.join(df_scores, rsuffix='_right')


# %%

df_news.head(20)

# %%
