import glob

PATH_POSITIVE = r'C:\Users\Zosia\Documents\Praktyczny Python\M03\data\aclImdb\train\pos\*.txt'
PATH_NEGATIVE = r'C:\Users\Zosia\Documents\Praktyczny Python\M03\data\aclImdb\train\neg\*.txt'

positive_files = glob.glob(PATH_POSITIVE)
negative_files = glob.glob(PATH_NEGATIVE)


# Load and parse positive reviews in order to count word occurencies
positive_words_count = {}
for file in positive_files:
    with open(file, encoding='utf-8') as stream:
        content = stream.read()
        words = content.lower().replace('<br />', ' ').split()
        for word in set(words):
            positive_words_count[word] = positive_words_count.get(word, 0) + 1

# Load and parse negative reviews in order to count word occurencies
negative_words_count = {}
for file in negative_files:
    with open(file, encoding='utf-8') as stream:
        content = stream.read()
        words = content.lower().replace('<br />', ' ').split()
        for word in set(words):
            negative_words_count[word] = negative_words_count.get(word, 0) + 1

# Get sentence
comment = input('Insert your comment: ')
words = comment.lower().replace('<br />', ' ').split()

# Count sentiment for each word and the whole sentence
sentence_sentiment = 0
for word in words:
    positive = positive_words_count.get(word, 0)
    negative = negative_words_count.get(word, 0)
    all_ = positive + negative
    if all_ == 0:
        word_sentiment = 0
    else:
        word_sentiment = (positive - negative) / all_
    print(word, word_sentiment)
    sentence_sentiment += word_sentiment
sentence_sentiment /= len(words)


if sentence_sentiment > 0:
    label = "positive"
elif sentence_sentiment < 0:
    label = "negative"
else:
    label = "neutral"

# Result
print("--")
print("This sentence is", label)
print("Sentiment =", sentence_sentiment)