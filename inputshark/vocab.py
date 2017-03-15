from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import pickle


def process_news_pickle(news_file):
    news_data = pickle.load(open('pickles/news/'+news_file))
    ps = PorterStemmer()
    processed_news = {}
    for key in news_data.keys():
        processed_news[key] = []
        for text in news_data[key]:
            if text != None:
                text = text.encode('ascii','ignore')
                #tokenizing
                tokenized_words = word_tokenize(text.translate(None, string.punctuation))
                #removing stop words
                stop_words = set(stopwords.words('english'))
                filtered_sentence = [w for w in tokenized_words if not w in stop_words]
                stemmed_sentence = []
                for w in filtered_sentence:
                    word = ps.stem(w)
                    stemmed_sentence.append(word.encode('ascii','ignore'))
                processed_news[key].append(stemmed_sentence)
    pickle.dump(processed_news,open('pickles/processed_news/'+news_file,'wb'))


def add_vocab(text):
    MAIN_WORD_LIST = pickle.load(open('pickles/vocab_01.pickle'))
    ps = PorterStemmer()
    #tokenizing
    tokenized_words = word_tokenize(text.translate(None, string.punctuation))
    #removing stop words
    stop_words = set(stopwords.words('english'))
    filtered_sentence = [w for w in tokenized_words if not w in stop_words]
    #final word_list
    for w in filtered_sentence:
        word = ps.stem(w)
        if (word not in MAIN_WORD_LIST):
            MAIN_WORD_LIST.append(word)
    pickle.dump(MAIN_WORD_LIST,open('pickles/vocab_01.pickle','wb'))

def vocab_index(process_news_file):
    processed_news_data = pickle.load(open('pickles/processed_news/'+process_news_file))
    firstderiv_news_data = pickle.load(open('pickles/firstderiv/'+process_news_file))
    MAIN_WORD_LIST = pickle.load(open('pickles/vocab_01.pickle'))
    index_list = []
    y_list = []
    for key in processed_news_data.keys():
        if(key!='201312'):
            sentiment = 0
            if firstderiv_news_data[key]<0:
                sentiment = 0
            else:
                sentiment = 1
            for sentence in processed_news_data[key]:
                sent = []
                if sentence != None:
                    for word in sentence:
                        try:
                            index = MAIN_WORD_LIST.index(word)
                            sent.append(index)
                        except:
                            sent.append(0)
                index_list.append(sent)
                y_list.append(sentiment)
    pickle.dump(index_list,open('pickles/news_index/X_train/'+process_news_file,'wb'))
    pickle.dump(y_list,open('pickles/news_index/y_train/'+process_news_file,'wb'))
