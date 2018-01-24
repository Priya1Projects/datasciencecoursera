import sys, string, re
import matplotlib.pyplot as plt

# command line arguments
file = sys.argv[1]
#target = sys.argv[2]
#window = int(sys.argv[3])

#a= open(file) #uncomment when calling from command line
a = open('C:\\temp\\GalvanizeProjectSubmission\\count.txt')
text = a.read().lower() 
a.close()

tokens = text.replace('.','')
tokens = tokens.replace(',','')
tokens=tokens.split() # split on whitespace
print(tokens)
print('total words:', len(tokens))
unique_words = set(tokens)
print('Unique word count', len(unique_words))
sentence_count = len(re.findall(r'\.', text))
print('Number of sentences', sentence_count)

sentences= text.split('.')
wordspersen = 0

for sen in sentences:   
    wordspersen += len(sen.split())
    print(wordspersen)
avg_words = wordspersen / len(sentences)  
print('Average length of sentence',avg_words)

# Word frequency using dict   
def map_book(tokens):
    hash_map = {}

    if tokens is not None:
        for element in tokens:
            # Remove Punctuation
            word = element.replace(",","")
            word = word.replace(".","")

            # Word Exist?
            if word in hash_map:
                hash_map[word] = hash_map[word] + 1
            else:
                hash_map[word] = 1

        return hash_map
    else:
        return None


# Create a Hash Map (Dictionary)
map = map_book(tokens)
    
for k, v in sorted(map.items(), key=lambda x: x[1],reverse=True):
    print ("%s: %s" % (k, v))