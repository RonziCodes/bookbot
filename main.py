def main():
    with open("books/frankenstien.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        lower_words = file_contents.lower()

        char_count = {}
        for char in lower_words:
            if char.isalpha():
                if char not in char_count:
                    char_count[char] = 0
                char_count[char] += 1

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")

    char_list = [{"char": char, "num": count} for char, count in char_count.items()]

    def sort_on(char_dict):
        return char_dict["num"]

    char_list.sort(reverse=True, key=sort_on)

    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

main()
