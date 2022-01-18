
import glob

PATH_POSITIVE = r'C:\Users\Zosia\Documents\Praktyczny Python\M03\data\aclImdb\train\pos\*.txt'
PATH_NEGATIVE = r'C:\Users\Zosia\Documents\Praktyczny Python\M03\data\aclImdb\train\neg\*.txt'
PUNCTUATION = '.,;:?!"%()-'

files_positive = glob.glob(PATH_POSITIVE)
files_negative = glob.glob(PATH_NEGATIVE)

# Load training reviews
all_positive_reviews = []
for file in files_positive:
    with open(file, encoding='utf-8') as stream:
        file = stream.read()
        all_positive_reviews.append(file)

all_negative_reviews = []
for file in files_negative:
    with open(file, encoding='utf-8') as stream:
        file = stream.read()
        all_negative_reviews.append(file)

# Define functions to parse the texts
def text_cleaner(text):
    text = text.lower()
    for char in PUNCTUATION:
        text = text.replace(char, ' ')
    text = text.replace('<br />', ' ')
    words_list = text.split()
    return words_list

def clean_str_or_list(niewiadomoco):
    if type(niewiadomoco) == str:
        words_list = text_cleaner(niewiadomoco)    
    elif type(niewiadomoco) == list:
        words_list = []
        for comment in niewiadomoco:
            for word in comment:
                words_list.append(text_cleaner(word))
    return words_list

# Parse the reviews
clear_positive_reviews = []
for review in all_positive_reviews:
    clear_positive_reviews.append(clean_str_or_list(review))

clear_negative_reviews = []
for review in all_negative_reviews:
    clear_negative_reviews.append(clean_str_or_list(review))

# Get user comment and parse it
comment = input('Insert your comment: ')
clear_comment = clean_str_or_list(comment)

# Compute sentiment for each word
words_and_sentiments = []
for word in clear_comment:

    positive_counter = 0
    for review in clear_positive_reviews:
        if word in review:
            positive_counter += 1

    negative_counter = 0
    for review in clear_negative_reviews:
        if word in review:
            negative_counter += 1

    if positive_counter != 0 or negative_counter != 0:
        sentiment = (positive_counter - negative_counter) / (positive_counter + negative_counter)
    else:
        sentiment = 0
    word_sentiment = [word, sentiment]
    words_and_sentiments.append(word_sentiment)


# Compute sentiment for the whole comment
sentiments_sum = 0
for word, sentiment in words_and_sentiments:
    sentiments_sum += sentiment

comment_sentiment_value = sentiments_sum / len(clear_comment)

if comment_sentiment_value > 0:
    comment_sentiment = "positive"
elif comment_sentiment_value < 0:
    comment_sentiment = "negative"
else:
    comment_sentiment = "neutral"

# Report
for word, sentiment in words_and_sentiments:
    print(word, sentiment)
print("--")
print("This sentence is", comment_sentiment)
print("Sentiment =", comment_sentiment_value)
