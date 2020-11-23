class WordCounter():
    """
    A class which counts words from the specified filepath.
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def count_words(self):
        """
        A function which takes as input a text file, and returns a sorted list of tuples, with the words from the text, and their occurrences.
        """
        with open(self.filepath, 'r', encoding = 'utf8') as file:
            contents = file.read()
            contents = contents.strip()
            contents = contents.replace('\n', ' ')
            contents = contents.translate({ord(c): None for c in '!:;*,.?—-'})
            contents = contents.lower()
            words = contents.split(' ')

            word_counts = dict()

            for word in words:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
            return(sorted(word_counts.items(), key = lambda item: item[1], reverse = True))
    
    def list_words_with_occurences_more_than(self, number):
        """
        Print out the items which occur more than 'number' times in the text.
        """
        for item in self.count_words():
            if (item[1] > 10):
                print(item)



"""
A test of the class and its functions. In this repo there is a large text file of a Polish book. 
We use this as an example of how the methods work.
"""
target_file = 'pantadek.txt'
word_counts = WordCounter(target_file) # create the counter class with the specified file
wordsDict = word_counts.count_words() # store the list of word counts in a variable
print(wordsDict) # print the result of counting
word_counts.list_words_with_occurences_more_than(10) # show the words which occur more than 10 times in the text