import numpy as np
from statistics import mean
from datetime import datetime
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import os

nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')

unprocessed_datasets = [x for x in os.listdir(r'data_unprocessed') if x.endswith('.csv')]
"""for dataset in unprocessed_datasets:
    print(f'{dataset} is being processed')
    df = pd.read_csv(f'data_unprocessed/{dataset}').set_index('Date').loc['2021-01-05':]
    news_columns = df.columns[3:]

    for col in news_columns:  # here I iterate news columns so col is "news_1", "news_2"...
        sentiment_list = []
        subjectivity_list = []
        print(f'processing {col}...')
        for news in list(df[col]):  # here I iterate news column per singular news
            if str(news) != 'nan':
                doc = nlp(news)
                sentiment_list.append(doc._.blob.polarity)
                subjectivity_list.append(doc._.blob.subjectivity)
            else:
                sentiment_list.append("None")
                subjectivity_list.append("None")
        df[col + '_sentiment'] = sentiment_list
        df[col + '_subjectivity'] = subjectivity_list

    sentiment_columns = [x + '_sentiment' for x in news_columns]
    subjectivity_columns = [x + '_subjectivity' for x in news_columns]

    daily_sentiment_col = []
    daily_subjectivity_col = []
    for i in range(len(df)):
        sentiment_per_row_list = []
        subjectivity_per_row_list = []
        for sent_col, subj_col in zip(sentiment_columns, subjectivity_columns):
            sentiment_per_news = df.iloc[i][sent_col]
            subjectivity_per_news = df.iloc[i][subj_col]
            sentiment_per_row_list.append(sentiment_per_news)
            subjectivity_per_row_list.append(subjectivity_per_news)
        if sentiment_per_row_list[0] != "None":
            daily_sentiment_col.append(mean([x for x in sentiment_per_row_list if x != "None"]))
            daily_subjectivity_col.append(mean([x for x in subjectivity_per_row_list if x != "None"]))
        else:
            daily_sentiment_col.append(np.nan)
            daily_subjectivity_col.append(np.nan)

    df['daily_sentiment'] = daily_sentiment_col
    df['daily_subjectivity'] = daily_subjectivity_col

    for col in df.columns:
        if col.startswith('news'):
            del df[col]

    del df['Volume']

    df.to_csv(f'data_processed/{df["Ticker"].iloc[0]}.csv')
    print('The end of dataset processing!\n\n')"""

"""processed_datasets = [x for x in os.listdir(r'data_processed') if x.endswith('.csv')]

#concatenating datasets
processed_datasets_list = [pd.read_csv(f'data_processed/{name}') for name in processed_datasets]
overall_dataset = pd.concat(processed_datasets_list, ignore_index=True)
overall_dataset['Date'] = [datetime.strptime(date, "%Y-%m-%d").date() if '/' not in date else datetime.strptime(date, "%m/%d/%Y").date() for date in overall_dataset['Date']]
overall_dataset = overall_dataset.sort_values(by=['Date']).rename(columns={"Traiding_result": "Trading_result"})
daily_sentiment_avg = mean(list([value for value in overall_dataset['daily_sentiment'] if str(value)!='nan']))
daily_subjectivity_avg = mean(list([value for value in overall_dataset['daily_subjectivity'] if str(value)!='nan']))
overall_dataset['daily_sentiment'] = overall_dataset['daily_sentiment'].fillna(daily_sentiment_avg)
overall_dataset['daily_subjectivity'] = overall_dataset['daily_subjectivity'].fillna(daily_subjectivity_avg)

overall_dataset.to_csv('data_overall/main_data.csv',index=False)"""
