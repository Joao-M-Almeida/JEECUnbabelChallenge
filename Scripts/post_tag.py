import nltk
from nltk.tag import StanfordPOSTagger
from nltk.tokenize import TweetTokenizer
from nltk.util import ngrams
from collections import Counter

import itertools
import string


s0 = "AQ AO RG DD DP DT DE DI DA NC NP VM VS VA PP PD PX PI PT PR PE CC CS I SP F Z 0"
words = s0.lower().split()
fdist = itertools.permutations(words, 2)
dic = {}
for i,k in enumerate(fdist):
    dic[k]=i
tagers=[]
st = StanfordPOSTagger('../../stanford-postagger-full-2015-12-09/models/spanish.tagger',
                       '../../stanford-postagger-full-2015-12-09/stanford-postagger.jar')


def postag(txt,Dictio=dic,tagger=st,n=2):
    vect = [0] * len(dic)
    #txt = ''.join([c for c in txt if c not in string.punctuation])
    txt_lst = txt.split()
    #print txt_lst
    tag_lst = st.tag(txt_lst)
    tag_lst = [clean_tag(tag[1]) for tag in tag_lst]
    grams = ngrams(tag_lst,n)
    for gram in grams:
        try:
            vect[Dictio[gram]] +=1 
        except KeyError:
            pass
    return vect

def clean_tag(tag,possible_tags = words):
    possible_tags = set(possible_tags)
    if tag[0] in possible_tags:
        return tag[0]
    elif tag[0:2] in possible_tags:
        return tag[0:2]
    return '0'
    

