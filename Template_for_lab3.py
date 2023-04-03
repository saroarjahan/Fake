# -*- coding: utf-8 -*-
"""lab3.ipynb

Automatically generated by Colaboratory.

"""

# part 4

!pip install botometer

import botometer



rapidapi_key = ""
twitter_app_auth = {
    'consumer_key': '',
    'consumer_secret': '',
    'access_token': '',
    'access_token_secret': '',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@clayadavis')


#part 5

import pandas as pd
import re

import networkx as nx
import matplotlib.pyplot as plt

def get_news_data():
    real_news = pd.read_csv("/content/real_news.csv")
    fake_news = pd.read_csv("/content/fake_news.csv")
    return real_news, fake_news

def get_mentions(df):
    all_mentions = []
    for index, row in df.iterrows():
        tweet = row['text']
        user = row['user_screen_name']

        # write rest of code that find mentions and add it to all_mentions like (user, mentions)
        #.....
        #.....

    return all_mentions

def get_nodes(all_mentions):
    nodes = []
    for m in all_mentions:
        # write rest of code  add   (user, mentions) as nodes
        #.....
        #.....

    return list(set(nodes)) # removes duplicate entries

def draw_graph(all_mentions):
    G = nx.Graph()

    nodes = get_nodes(all_mentions)
    # write a line of that add node in G

    # write a for loop that add egdes to the node

    # Calculate the node level
    node_level = nx.algorithms.centrality.degree_centrality(G)
    pos = nx.kamada_kawai_layout(G)
    plt.figure(3, figsize=(20, 20))
    nx.draw_networkx_nodes(G, pos=pos, nodelist=node_level.keys(), node_size=[v*1000 for v in node_level.values()], cmap=plt.cm.Reds)
    nx.draw_networkx_labels(G, pos=pos, font_size=10, font_family="sans-serif")
    nx.draw_networkx_edges(G, pos=pos, alpha=0.5)
    plt.show()

    return G

real_news_data, fake_news_data = get_news_data()


fake_news_mentions = get_mentions(fake_news_data)
graph=draw_graph(fake_news_mentions)


#Closeness centrality

bc = nx.centrality.# complete the line
avg_bc = # complete the line
print(avg_bc)

#Closeness centrality
cc = nx.centrality.# complete the line
avg_cc = # complete the line
print(avg_cc)

#degree centrality
dc = nx.# complete the line
avg_dc1 = # complete the line
print(avg_dc)
