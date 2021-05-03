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
