import sys

path_to_file = "./books/frankenstein.txt"

def read_book(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(input_string):
    words = input_string.split()
    return len(words)

def count_letters_d(input_string):
    word_d = {}
    for l in input_string.lower():
        word_d[l] = word_d.get(l, 0) + 1
    return word_d

def sort_letters_d(words_d):
    return {k: v for k, v in sorted(words_d.items(), key=lambda item: item[1], reverse=True) if k.isalpha()}

def display_report(total_words, letters_sorted):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document\n")
    
    for k, v in letters_sorted.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

def main():
    try:
        book1 = read_book(path_to_file)
        words_d = count_letters_d(book1)
        letters_d = sort_letters_d(words_d)
        words_count = count_words(book1)
        display_report(words_count, letters_d)
        #print(words_d)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    sys.exit(main())