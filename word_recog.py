# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:36:02 2019

@author: breno.zipoli
"""

with open("sample.txt") as file:
    text = file.read()
    
def count_word(text, word_to_find):
    total_words = 1
    i = 0
    j = 0
    count = 0
    word_to_find_list = []
    text_list = []
    word_to_find_list = word_to_find
    
    for char in text:
        text_list += char;
    
    for char in text:
        if text_list[i] == " ":
            total_words += 1
        
        if text_list[i] == word_to_find_list[j]:
            i += 1
            j += 1

            if j == len(word_to_find):
                count += 1
                j = 0
        else:
            i += 1
            j = 0
    print("Searching for the word " + word_to_find + ": " + str(count) + " appearances!")
    print("Total number of words: " + str(total_words))
    print("Percentage: " + str(round(count/total_words*100,2)) + " %" )
    
count_word(text,"to")