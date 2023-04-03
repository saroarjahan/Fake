# Fake

## Fake News Twitter Analysis

Consider the 2016 US election Viral Twitter dataset collected between election day (Nov 8th) and March
2017. Tweets have been labelled as containing fake news or not by two sets of people, and where fake
news is categorized into one of the five categories: i) Serious fabrication; ii) Large-scale hoaxes; iii) Jokes
taken at face value; iv) Slanted reporting of real facts; v) Stories where the 'truth' is contentious. The
dataset can be downloaded from Fakenews on 2016 US elections viral tweets (November 2016 - March
2017) | Zenodo

### Lab -2: 
1. Write a script for the calculus of the mean, standard deviation, kurtosis and skewness of Number
of follower per user in case of Fake News and Real News dataset. Repeat this process for Favorite
Count as well. Conclude whether one can discriminate the two classes using such statistical data.

3. We want to compare the activity of individual users in Fake News and Real News dataset. Select
the three most active users in terms of number tweets generated and calculate the average
number of tweets generated by the three users. Repeat this process for the five most active users
in each dataset, and for the first 10-users in each dataset, and first 15 users for each dataset.

3. We want to compare the average time a user stays before sending a new message. Write a script
that uses the date information on the dataset for each tweet to calculate the average waiting time
for a random user before sending a new message in case of Fake News and Real News.

### Lab -3: 

4. We would like to study whether the user ids of fake news and real news dataset are genuine or not. For this
purpose, study the program botometer available in https://github.com/IUNetSci/botometer-python. The
program inputs a tweet user id and outputs the probability that the user id is a bot or human. You can use a
threshold 0.5 beyond which a program is bot or not. The purpose is therefore to test the hypothesis whether
Fake News are globally originated from bots or humans and whether Real News are generated by humans or also
by bots. If the computational time is an issue to test the whole data, you can choose a random selection of the
data as well. (N.B: Just Get familirity with theses steps, proably u wont be able to complete this part since its need advance API)

5.Create a social network from the Twitter dataset. For this purpose, consider the
mention reference in Twitter. More specifically, write a small program that allows you to identify
the “mention” in each tweet message (word precedent by “@”). Now, construct a network graph
where the nodes correspond to the user ID while the edge between two nodes, say A and B,
indicates that tweet of user id A contains in its text message a mention of user id B. Construct
social network graph for each dataset (Fake News and Real News). Use appropriate visualization
to draw high level illustration of each graph.

6. Use appropriate functions in NetworkX to  average degree centrality, average closeness centrality and average betweenness centrality for
each dataset


