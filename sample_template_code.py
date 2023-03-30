import pandas as pd

### Part 1

def get_twiter_news_data():
    real_news = pd.read_csv("data/derived/real_news.csv")
    real_news['created_at'] = pd.to_datetime(real_news['created_at'])

    fake_news = pd.read_csv("data/derived/fake_news.csv")
    fake_news['created_at'] = pd.to_datetime(fake_news['created_at'])

    return real_news, fake_news

def get_follower_favourite_count(df, user):
    user_data = df.loc[df['user_screen_name'] == user]

    # If there are multiple entries for the same user, get the followers and favourite count from the latest post
    latest_update =  # Try to complete  this part
    followers = # Try to complete  this part
    favourites = # Try to complete  this part

    return followers, favourites

def get_user_data(df, users):
    user_data = []
    for user in users:
        followers, favourites = # Try to complete  this line
        user_data.append([user, followers, favourites])

    df = pd.DataFrame(user_data, columns=['user', 'followers', 'favourites'])
    return df

def calculate_statistics(user_data):
    mean = Try to complete  this line
    std = # Try to complete  this line
    kurtosis = # Try to complete  this line
    skew = # Try to complete  this line

    return mean, std, kurtosis, skew

def print_statistics(user_data):
    mean, std, kurtosis, skew = calculate_statistics(user_data)
    data = [['mean', mean['followers'] #.....  # Try to complete  this line
]]
    df = pd.DataFrame(data, columns=['calculus', 'followers', 'favourites'])
    print(df.to_string(index=False))



### Part 2

def AVG_tweet_count_print(tweet_count, length):
    count_values = # Try to complete  this line
    print("AVG n of tweets {} most active users: {}".format(length, count_values.mean()))


real_news_data, fake_news_data = get_twiter_news_data()

real_news_user_tweet_count = real_news_data['user_screen_name'].... # Try to complete  this line
fake_news_user_tweet_count = fake_news_data['user_screen_name']....# Try to complete  this line

print("---------------- Real news users ----------------")
AVG_tweet_count_print(real_news_user_tweet_count, 3)
AVG_tweet_count_print(real_news_user_tweet_count, 5)
AVG_tweet_count_print(real_news_user_tweet_count, 10)
AVG_tweet_count_print(real_news_user_tweet_count, 15)

print("\n\n---------------- Fake news users ----------------")
AVG_tweet_count_print(fake_news_user_tweet_count, 3)
AVG_tweet_count_print(fake_news_user_tweet_count, 5)
AVG_tweet_count_print(fake_news_user_tweet_count, 10)
AVG_tweet_count_print(fake_news_user_tweet_count, 15)

"""
Result will look similar to this, but it willl be different result:
---------------- Real news users ----------------
AVG n of tweets 3 most active users: 332.6666666666667
AVG n of tweets 5 most active users: 257.2
AVG n of tweets 10 most active users: 168.3
AVG n of tweets 15 most active users: 132.66666666666666


---------------- Fake news users ----------------
AVG n of tweets 3 most active users: 33.0
AVG n of tweets 5 most active users: 25.2
AVG n of tweets 10 most active users: 17.1
AVG n of tweets 15 most active users: 13.666666666666666
"""


# Part 3


def get_avg_waiting_time(user_data):
    total_waiting_time = 0
    for idx in range(1, user_data.shape[0]):
        tweet_1_timestamp = user_data.iloc[[idx - 1]]['created_at'].values[0]
        tweet_2_timestamp = user_data.iloc[[idx]]['created_at'].values[0]

        time_days = .... # Try to complete  this line
        total_waiting_time += .... # Try to complete  this line

    avg_waiting_time = .... # Try to complete  this line
    return avg_waiting_time

def avg_waiting_times_print(df, users):
    total_avg_wait_time = 0
    valid_users = 0

    for user in users:
        user_data = df.loc[df['user_screen_name'] == user]
        if user_data.shape[0] > 1:
            valid_users += 1
            user_data = .... # Try to complete  this line
            avg_wait_time = get_avg_waiting_time(user_data)
            print("Average wait time for {}: {} days".format(user, avg_wait_time))
            total_avg_wait_time += .... # Try to complete  this line

    print("Overall average wait time: {} days".format(.... # Try to complete  this line))


real_news_data, fake_news_data = get_twiter_news_data()
distinct_real_news_users = real_news_data['user_screen_name'].unique()
distinct_fake_news_users = fake_news_data['user_screen_name'].unique()

all_news_data = pd.read_excel(open('data/twitter_fakenews_USElections_2016.xlsx', 'rb'), sheet_name='DATA')
all_news_data['created_at'] = pd.to_datetime(all_news_data['created_at'])

print("---------------- Real news users ----------------")
avg_waiting_times_print(all_news_data, distinct_real_news_users)

print("\n\n---------------- Fake news users ----------------")
avg_waiting_times_print(all_news_data, distinct_fake_news_users)

# Result:
# Overall average wait times
# Real news users = 32.46 days
# Fake news users = 22.9 days
