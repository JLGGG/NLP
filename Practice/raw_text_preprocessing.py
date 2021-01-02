import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from autocorrect import Speller
from nltk.wsd import lesk
from nltk.tokenize import sent_tokenize
import string

sentence = "In this book authored by Sohom Ghosh and Dwight Gunning, we shall learnning how to pracess Natueral Language and extract insights from it. The first four chapter will introduce you to the basics of NLP. Later chapters will describe how to deal with complex NLP prajects. If you want to get early access of it, you should book your order now."
words = word_tokenize(sentence)
spell = Speller()

# Spelling correction
corrected_sentence = ""
corrected_word_list = []
for wd in words:
    if wd not in string.punctuation:
        wd_c = spell(wd)
        if wd_c != wd:
            print(wd+" has been corrected to: "+wd_c)
            corrected_sentence = corrected_sentence+" "+wd_c
            corrected_word_list.append(wd_c)
        else:
            corrected_sentence = corrected_sentence+" "+wd
            corrected_word_list.append(wd)
    else:
        corrected_sentence = corrected_sentence + wd
        corrected_word_list.append(wd)

print(sentence)
print(corrected_sentence)
print(nltk.pos_tag(corrected_word_list)) # Add PoS tag

# Remove stopwords
stop_words = stopwords.words('English')
corrected_word_list_without_stopwords = []
for wd in corrected_word_list:
    if wd not in stop_words:
        corrected_word_list_without_stopwords.append(wd)
print(corrected_word_list_without_stopwords[:20])

# Stem extraction
stemmer = nltk.stem.PorterStemmer()
corrected_word_list_without_stopwords_stemmed = []
for wd in corrected_word_list_without_stopwords:
    corrected_word_list_without_stopwords_stemmed.append(stemmer.stem(wd))
print(corrected_word_list_without_stopwords_stemmed[:20])


lemmatizer = WordNetLemmatizer()
corrected_word_list_without_stopwords_lemmatized = []
for wd in corrected_word_list_without_stopwords:
    corrected_word_list_without_stopwords_lemmatized.append(lemmatizer.lemmatize(wd))
print(corrected_word_list_without_stopwords_lemmatized[:20])