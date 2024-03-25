def main():
    print_book_report("books/frankenstein.md")


def print_book_report(file):
    with open(file) as f:
        file_contents = f.read()
        print(f"---Begin report of {file} ---")
        words = count_words(file_contents)
        print(f"{words} words found in the document\n")
        letters = count_letters(file_contents)
        for letter, count in sort_by_count(letters):
            print(f"The '{letter}' character was found {count} times")
        print("--- End report ---")


def count_words(content):
    return len(content.split())


def sort_by_count(letters):
    list = []
    for letter in letters:
        list.append((letter, letters[letter]))

    list.sort(reverse=True, key=lambda tup: tup[1])

    return list





def count_letters(content):
    dict = {}
    for char in content.lower():
        if not char.isalpha():
            continue
        if char not in dict:
            dict[char] = 0
        dict[char] += 1

    return dict


main()
