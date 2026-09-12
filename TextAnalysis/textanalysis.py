"""
TEXT ANALYSIS
Step1: Count all characters using string length function
Step2: Create function to clean all symbols and numbers from string and count number of words.
Step3: Create function to split sentences through "." and count the number of sentences.
Step4: Create function to get unique words.
     --> use map to get all the words list in lowercase
     --> use set to get unqiue values
Step5: Get the frequency of each word. Loop through the set returned by previous function.
     --> for each word use count function to count the words in the string
     --> Add it to a new dictionary
Step6: Create function to sort the dictionary based on frequency(high to low)
Step7: Get the most common word from the word_frequency.
     --> Make a list of the counts from the word_frequency.items(). Get Max value of the list
     --> Print all the words that has frequency == Max
Step8: Create a function to filter by length> Get Min & Max length user input
     --> Use filter function to filter by Min <= length <= Max
Step9: Iterate through the sorted frequency dictionary and get the top 5 most common words

"""
import re

string = input("Enter a phrase: \n")

def character_count(string):
   characters = len(string)
   return characters

def word_count(string):
   #Clean anything that that is not a word or not a whitespace. Replace with ""
   clean_string = re.sub(r'[^\w\s]', '', string)
   words = clean_string.split()
   return words, len(words)

def sentence_count(string):
   sentences = string.split(".")
   frequency = len(sentences) - 1
   return sentences, frequency

def unique(words):
   words_list = list(map(lambda word: word.lower(), words))
   unique_words = set(words_list)
   unique_words_count = len(unique_words)
   return unique_words_count, unique_words, words_list

def frequency(words):
   word_frequency = {}
   for word in words:
      if word in word_frequency:
         word_frequency[word] += 1
      else:
         word_frequency[word] = 1
   return word_frequency

def sort_frequency(word_frequency):
   sorted_freq = dict(sorted(word_frequency.items(), key = lambda x: x[1], reverse = True))
   return sorted_freq

def most_common_word(word_frequency):
   count_list = [count for word, count in word_frequency.items()]
   highest = max(count_list)
   for word, count in word_frequency.items():
      if count == highest:
         print(f"{word}: {count}")

def filter_by_length(unique_words):
   min_ = int(input("Enter Min length: "))
   max_ = int(input("Enter Max length: "))
   filtered = list(filter(lambda x: min_ <= len(x) <= max_, unique_words))
   return filtered

def top_5(sort_freq):
   i = 0
   for word, freq in sort_freq.items():
      if i<5:
         print(f"{word}: {freq}")
         i += 1


def main():
   characters = character_count(string)
   print(f"\nTotal Characters: {characters}")

   words, total_words = word_count(string)
   print(f"\nTotal Words: {total_words}")

   sentences, total_sentences = sentence_count(string)
   print(f"\nTotal Sentences: {total_sentences}")

   unique_words_count, unique_words, words_list = unique(words)
   print(f"\nUnique Words: {unique_words_count}")

   word_frequency = frequency(words)
   sort_freq = sort_frequency(word_frequency)
   print("\nSorted Word Counts:\n")
   for word, count in sort_freq.items(): print(f"{word}: {count}")

   print("\nMost common word in the passage: ")
   most_common_word(word_frequency)

   print("\nTop 5 most common words: ")
   top_5(sort_freq)

   print("\nFilter words by length")
   filtered = filter_by_length(unique_words)
   print("Filtered words: ")
   for word in filtered: print(word, end= "   ")

main()