import sys
import decimal
sys.path.append("/usr/local/lib/python3.7/site-packages")
import numpy as np
import math
import nltk
from nltk.tokenize import word_tokenize
from random import randint
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation
from matplotlib import cm
from nltk.corpus import stopwords
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def check_string(a_string):
    alphanumeric = ""
    for character in a_string:
        if character.isalnum():
            alphanumeric += character
    return a_string

class my_dictionary(dict):
    
    def __init__(self):
        self = dict()
        
    def add(self, key, value):
        self[key] = value
    
    def checkKey(self,dict, key):
        if key in dict.keys():
            return True
        else:
            return False
    def main_function1(self,str):
        data_input = []
        with open('data/first.csv', 'r',encoding='latin-1') as file:
            reader = csv.reader(file)
            for row in reader:
                if(row[0] == str):
                    data_input.append(row[5])
        kk = 0
        for i in range(len(data_input)):
            x = data_input[i].split(' ')
            for j in range(len(x)):
                if(self.checkKey(self,check_string(x[j]))):
                    self[check_string(x[j])] = self[check_string(x[j])] + 1
                else:
                    self.add(check_string(x[j]),1)
            kk = kk + len(x)
                
        for key in self:
            self[key] = self[key]
        
        return kk

    def main_function1_stop_words(self,str):
        stop_words = set(stopwords.words('english'))
        data_input = []
        with open('data/second.csv', 'r',encoding='latin-1') as file:
            reader = csv.reader(file)
            for row in reader:
                if(row[0] == str):
                    data_input.append(row[5])
        kk = 0
        x = []
        x1 = []
        for i in range(len(data_input)):
            x1 = word_tokenize(data_input[i])
            x = filtered_sentence = [w for w in x1 if not w in stop_words]
            for j in range(len(x)):
                if(self.checkKey(self,check_string(x[j]).lower())):
                    self[check_string(x[j]).lower()] = self[check_string(x[j]).lower()] + 1
                else:
                    self.add(check_string(x[j]).lower(),1)
            kk = kk + len(x)
                
        for key in self:
            self[key] = self[key]
        
        return kk
        
    def main_function_Q_1_E_first(self,):
        stop_words = set(stopwords.words('english'))
        data_input = []
        with open('data/second.csv', 'r',encoding='latin-1') as file:
            reader = csv.reader(file)
            for row in reader:
                if(row[0] == str):
                    data_input.append(row[5])
        kk = 0
        x = []
        x1 = []
        for i in range(len(data_input)):
            x1 = word_tokenize(data_input[i])
            x = filtered_sentence = [w for w in x1 if not w in stop_words]
            for j in range(len(x)):
                if(self.checkKey(self,check_string(x[j]).lower())):
                    self[check_string(x[j]).lower()] = self[check_string(x[j]).lower()] + 1
                else:
                    self.add(check_string(x[j]).lower(),1)
            kk = kk + len(x)
                
        for key in self:
            self[key] = self[key]
        
        return kk
        
def main_function_Q_1_A():
    stop_words = set(stopwords.words('english'))
    data_input = []
    data_output = []
    with open('data/first.csv', 'r',encoding='latin-1') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] != "2"):
                data_input.append(row[5])
                data_output.append(int(row[0]))
    
    dict_obj0 = my_dictionary()
    dict_obj4 = my_dictionary()

    kk_0 = dict_obj0.main_function1('0')
    
    kk_4 = dict_obj4.main_function1('4')
    
#    print(kk_0)
    our_out = []
    
    confusion_matrix = [0,0,0,0]
    
    for i in range(len(data_input)):
        if(data_output[i] != 2):
            strings_in_tweet = data_input[i].split(' ')
#            x1 = word_tokenize(data_input[i])
#            strings_in_tweet = filtered_sentence = [w for w in x1 if not w in stop_words]
#            size_of_vocabulary = len(strings_in_tweet) + size_of_training_set
            probability1 = 0
            probability2 = 0
            for j in range(len(strings_in_tweet)):
                kq1 = 0
                kq2 = 0
                if check_string(strings_in_tweet[j]) in dict_obj4.keys():
                    kq1 = dict_obj4[check_string(strings_in_tweet[j])]
                if check_string(strings_in_tweet[j]) in dict_obj0.keys():
                    kq2 = dict_obj0[check_string(strings_in_tweet[j])]
                #print(kq1,kq2)
                #print(check_string(strings_in_tweet[j]),check_string(strings_in_tweet[j]))
                probability1 = probability1 + math.log((kq1 + 1)/(kk_4 + len(dict_obj0) + len(dict_obj4)))
                #*(len(dict_obj4))/(len(dict_obj0) + len(dict_obj4)))
                probability2 = probability2 + math.log((kq2 + 1)/(kk_0 + len(dict_obj0) + len(dict_obj4)))
                #*(len(dict_obj4))/(len(dict_obj0) + len(dict_obj4)))

            if((probability1)>(probability2)):
                our_out.append(4)
                if(data_output[len(our_out)-1] == 4):
                    confusion_matrix[3] = confusion_matrix[3] + 1
                else:
                    confusion_matrix[2] = confusion_matrix[2] + 1
            else:
                our_out.append(0)
                if(data_output[len(our_out)-1] == 0):
                    confusion_matrix[0] = confusion_matrix[0] + 1
                else:
                    confusion_matrix[1] = confusion_matrix[1] + 1

#            print(probability1)
    
    j = 0
    error = 0
    print(len(data_output),len(our_out))
    for i in range(len(data_output)):
        if(data_output[i] != our_out[i]):
            error = error + 1

    print("Q_1_Part_A")
    print(error,len(data_input))
    
    our_out_part_B = []
    
    for i in range(len(data_output)):
        if randint(1,2) == 1:
            our_out_part_B.append(4)
        else:
            our_out_part_B.append(0)
    
    print("Q_1_Part_B_random")
    error = 0
    print(len(data_output),len(our_out))
    for i in range(len(data_output)):
        if(data_output[i] != our_out_part_B[i]):
            error = error + 1
    
    print(error,len(data_output))
    
    print("Q_1_Part_B_majority")
    error = 0
    print(len(data_output),len(our_out))
    for i in range(len(data_output)):
        if(len(dict_obj0) > len(dict_obj4)):
            if(data_output[i] != 0):
                error = error + 1
        else:
            if(data_output[i] == 0):
                error = error + 1
    
    print(error,len(data_output))
        
    print("Q_1_Part_C_Confusion_matrix")
    
    print(confusion_matrix)

#    print(data_output)
#    print(our_out)
    
    
def main_function_Q_1_A_stopwords():
    stop_words = set(stopwords.words('english'))
    data_input = []
    data_output = []
    with open('data/first.csv', 'r',encoding='latin-1') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[0] != "2"):
                data_input.append(row[5])
                data_output.append(int(row[0]))
    
    dict_obj0 = my_dictionary()
    dict_obj4 = my_dictionary()

    kk_0 = dict_obj0.main_function1_stop_words('0')
    
    kk_4 = dict_obj4.main_function1_stop_words('4')
    
#    print(kk_0)
    our_out = []
    
    confusion_matrix = [0,0,0,0]
    
    for i in range(len(data_input)):
        if(data_output[i] != 2):
#            strings_in_tweet = data_input[i].split(" ")
            x1 = word_tokenize(data_input[i])
            strings_in_tweet = filtered_sentence = [w for w in x1 if not w in stop_words]
            print(strings_in_tweet)
#            size_of_vocabulary = len(strings_in_tweet) + size_of_training_set
            probability1 = 0
            probability2 = 0
            for j in range(len(strings_in_tweet)):
                kq1 = 0
                kq2 = 0
                if check_string(strings_in_tweet[j]).lower() in dict_obj4.keys():
                    kq1 = dict_obj4[check_string(strings_in_tweet[j]).lower()]
                if check_string(strings_in_tweet[j]).lower() in dict_obj0.keys():
                    kq2 = dict_obj0[check_string(strings_in_tweet[j]).lower()]
                #print(kq1,kq2)
                #print(check_string(strings_in_tweet[j]),check_string(strings_in_tweet[j]))
                if (not strings_in_tweet[j].lower() in stop_words):
                    probability1 = probability1 + math.log((kq1 + 1)/(kk_4 + len(dict_obj0) + len(dict_obj4)))
                    #*(len(dict_obj4))/(len(dict_obj0) + len(dict_obj4)))
                    probability2 = probability2 + math.log((kq2 + 1)/(kk_0 + len(dict_obj0) + len(dict_obj4)))
                    #*(len(dict_obj4))/(len(dict_obj0) + len(dict_obj4)))

            if((probability1)>(probability2)):
                our_out.append(4)
                if(data_output[len(our_out)-1] == 4):
                    confusion_matrix[3] = confusion_matrix[3] + 1
                else:
                    confusion_matrix[2] = confusion_matrix[2] + 1
            else:
                our_out.append(0)
                if(data_output[len(our_out)-1] == 0):
                    confusion_matrix[0] = confusion_matrix[0] + 1
                else:
                    confusion_matrix[1] = confusion_matrix[1] + 1

#            print(probability1)
    
    j = 0
    error = 0
    print(len(data_output),len(our_out))
    for i in range(len(data_output)):
        if(data_output[i] != our_out[i]):
            error = error + 1

    print("Q_1_Part_A")
    print(error,len(data_input))
    
    our_out_part_B = []
    
    for i in range(len(data_output)):
        if randint(1,2) == 1:
            our_out_part_B.append(4)
        else:
            our_out_part_B.append(0)
    
    print("Q_1_Part_B_random")
    error = 0
    print(len(data_output),len(our_out))
    for i in range(len(data_output)):
        if(data_output[i] != our_out_part_B[i]):
            error = error + 1
    
    print(error,len(data_output))
    
    print("Q_1_Part_B_majority")
    error = 0
    print(len(data_output),len(our_out))
    for i in range(len(data_output)):
        if(len(dict_obj0) > len(dict_obj4)):
            if(data_output[i] != 0):
                error = error + 1
        else:
            if(data_output[i] == 0):
                error = error + 1
    
    print(error,len(data_output))
        
    print("Q_1_Part_C_Confusion_matrix")
    
    print(confusion_matrix)

#    print(data_output)
#    print(our_out)

main_function_Q_1_A_stopwords()
