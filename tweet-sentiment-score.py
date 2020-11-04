#!/usr/bin/python3

# this is a sample project from the University of Michigan Python programming certificate program
# this script reads a csv file containing tweets, along with the number of retweets and replies
# the script counts the positive and negative words within each tweet, then calculates a net score
# the result is written to a new csv file

def strip_punctuation(x):
    for char in punctuation_chars:
        if char in x:
            x = x.replace(char, "")
    return x


def get_pos(y):
    y = y.lower()
    lst = y.split()
    count = 0
    for word in lst:
        word = strip_punctuation(word)
        if word in positive_words:
            count = count +1
    return count


def get_neg(z):
    z = z.lower()
    lst = z.split()
    count = 0
    for word in lst:
        word = strip_punctuation(word)
        if word in negative_words:
            count = count +1
    return count

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

outfile = open("resulting_data.csv", "w")
# output the header row
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
fileconnection = open("project_twitter_data.csv", 'r')
lines = fileconnection.readlines()
header = lines[0]
field_names = header.strip().split(',')

for row in lines[1:]:
    vals = row.strip().split(',')
    tweet = vals[0]
    retweet_count = vals[1]
    reply_count = vals[2]
    pos_score = get_pos(tweet)
    neg_score = get_neg(tweet)
    net_score = pos_score - neg_score
    row_string = '{}, {}, {}, {}, {}'.format(retweet_count, reply_count, pos_score, neg_score, net_score)
    outfile.write(row_string)
    outfile.write('\n')

outfile.close()

