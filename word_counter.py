import random # needed for scrambling text

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
    
    def scramble_text(self, scrambling_level=1):
        """
        A function which takes as input a text file, and creates another text file with the text scrambled.
        Scrambling happens through swapping adjacent characters in a random place in each word, as many times as specified trough scrambling_level (default value is 1).
        """
        # start by reading the file and creating a list of the words in the file. We will use this to perform the scrambling.
        with open(self.filepath, 'r', encoding = 'utf8') as file:
            contents = file.read()
            contents = contents.strip()
            contents = contents.replace('\n', ' ')
            contents = contents.translate({ord(c): None for c in '!:;*,.?—-'})
            contents = contents.lower()
            words = contents.split(' ') # list of words in the file

            output = '' # this will be written into the output text file

            for i in range(len(words)):
                word = words[i]
                scrambled_word = list(word)

                # if the word is one character, it makes no sense to swap, so we just add the word to the output and move on.
                if len(scrambled_word) < 2:
                    output = output + ''.join(scrambled_word) + ' '
                    continue
                # else, we perform swapping
                else:
                    for swap in range(scrambling_level):
                        rand_index = random.randint(0,len(scrambled_word)-2) # take a random index from the word (up to one character from the end, to prevent IndexErrors)
                        # swap the characters
                        temp_char = scrambled_word[rand_index+1]
                        scrambled_word[rand_index+1] = scrambled_word[rand_index]
                        scrambled_word[rand_index] = temp_char

                output = output + ''.join(scrambled_word) + ' ' # add the scrambled word to the output

            # finally, save the scrambled output to a text file
            with open('scrambled_output.txt', 'w', encoding = 'utf8') as outputfile:
                outputfile.write(output)

            return




# A test of the class and its functions. In this repo there is a large text file of a Polish book. 
# We use this as an example of how the methods work.

target_file = 'pantadek.txt'
word_counts = WordCounter(target_file) # create the counter class with the specified file
wordsDict = word_counts.count_words() # store the list of word counts in a variable
print(wordsDict) # print the result of counting
word_counts.list_words_with_occurences_more_than(10) # show the words which occur more than 10 times in the text

word_counts.scramble_text(scrambling_level=12) # scramble the text file, performing 2 swaps in each word. Check the output in the file 'scrambled_output.txt'