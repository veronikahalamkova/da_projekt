#%%
import spacy
from collections import Counter
nlp = spacy.load("en_core_web_sm")

#%%
stock_df = pd.read_csv("temp\dow\dow_final.csv")
# %%
doc = nlp(stock_df['longBusinessSummary'].values[12324])

print([(X.text, X.label_) for X in doc.ents])

# %%
