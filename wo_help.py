"""
author: nic
title: wordhelper
"""

import streamlit as st
from copy import deepcopy
import pandas as pd

def check_word(word_,letterlist):
    not_in = False
    for letter in word_:
        try:
            letterlist.remove(letter)
        except ValueError:
            not_in = True
            break
        
    if not_in == True:
        return False
    else:
        return True
    
def find_words(wordlen,avail_letters):
    with open('wortliste.txt','r') as f:
        wordlist_raw = f.readlines()
        
    for idx,word in enumerate(wordlist_raw):
        wordlist_raw[idx] = word.strip('\n').lower()

    wordlist = wordlist_raw

    len_fittings = []
    for word in wordlist:
        if len(word) == wordlen:
            len_fittings.append(word)
            
    contain_letters = list(avail_letters)
    all_results = []
    for word in len_fittings:
        if check_word(word,deepcopy(contain_letters)):
            all_results.append(word)
            
    return all_results


st.title('Ihre 4Bilder1Wort Hilfe!')
st.text(""" In das Feld die Buchstaben eingeben und dann den slider anpassen""")
st.text(""" Alles ausfüllen mit Buchstaben an einem Stück, dann >>Suchen<< drücken """)
lets = st.text_input('Alle Buchstaben')
w_len = st.slider(
    'Wortlänge', min_value=2, max_value=12, value=4, step=1,
    help='Hier Länge einstellen :)')
if st.button('Suchen',help='klick mich zum suchen :)'):
    res_list = find_words(w_len,lets)
    for idx,word in enumerate(res_list):
        res_list[idx] = word.upper()
    res_df = pd.DataFrame(res_list,columns=('Wörter',))
    st.dataframe(res_df)


