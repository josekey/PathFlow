import csv
import nltk


def load_specimens_TEST():
    test_spec = []
    with open('specimen_test.csv', newline='') as file:
        r = csv.DictReader(file)
        for row in r:
            test_spec.append({'specimen': row['specimen'] , 'checklist': row['checklist'].split("_")})

    return test_spec


##data fed to function will be raw text
def short_analysis(data):


    ##clean the raw text of stop words
    stopwords = nltk.corpus.stopwords.words("english")
    words: list[str] = nltk.word_tokenize(data)
    #words = [w for w in words if w.lower() not in stopwords]
    ##example concordance
    text = nltk.Text(words)
    concordance_list = text.concordance_list("journey", lines=2)
    ret_str = ""
    for entry in concordance_list:
        ret_str = ret_str + entry.line
    
    return ret_str

##function will do checks for simple key words and return corresponding concordance list
def keyword_concord(text):
    #print( ' text \n %s' % text)
    ##checking for centimeters 
    concordance_list = measurement_check(text)

    ret_str = ""
    for entry in concordance_list:
        ret_str = ret_str + '\n' + entry
    
    print('here is %s' %ret_str)
    return ret_str
    

##helper function returns surrounding text
def measurement_check(text):
    
    str_text = text[:]
    list_of_words = text.split()
    
    ret_str = []
    max_index = len(list_of_words)-1 

    for index, word in enumerate(list_of_words):
        if word == 'cm':
            top_index = index+4 if index+4 < max_index else max_index
            ret_str.append( ' '.join(map(str, list_of_words[index-1: top_index])) )

    
    return ret_str
    
    

