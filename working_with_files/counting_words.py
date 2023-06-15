# Define a function that counts the number of time every word appears in a string
def count_word_frequency(sample_text):
    word_frequency = {}
    sample_text = sample_text.lower().replace(".","")
    text_list = sample_text.split()
    for word in text_list:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    return word_frequency

# This is the text the function is being applied on
sample_text = "This is a sample text. This text is used for counting. This script I am making will count how many " \
              "times a word appears in this string."

# This is the filled dictionary
word_frequency_dict = count_word_frequency(sample_text)