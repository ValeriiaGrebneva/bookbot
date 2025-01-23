def number_of_words(text):
    words = text.split()
    return(len(words))
def count_char(text):
    text_lower = text.lower()
    dict_counts = {}
    for ch in text_lower:
        if ch in dict_counts:
            dict_counts[ch] += 1
        else:
            dict_counts[ch] = 1
    return dict_counts
def report(dict_counts):
    for ch in dict_counts:
        if ch.isalpha():
            print(f"The '{ch}' character was found {dict_counts[ch]} times")
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words(file_contents)} words found in the document")
    print("")
    report(count_char(file_contents))
    print("--- End report ---")
main()