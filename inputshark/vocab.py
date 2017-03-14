from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import string
import pickle


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
