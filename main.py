def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_characters(text):
    lower_text = text.lower()
    text_dict = {}
    for char in lower_text:
        if char in text_dict:
            text_dict[char] += 1
        else:
            text_dict[char] = 1
    return text_dict


def dict_to_sorted_list(text_dict):
    sorted_list = []
    for key in text_dict:
        sorted_list.append({"name": key, "num": text_dict[key]})
    sorted_list.sort(reverse=True, key=lambda x: x["num"])
    return sorted_list


def main():
    file_path = "books/frankenstein.txt"
    file_contents = get_book_text(file_path)
    word_count = count_words(file_contents)
    character_count = count_characters(file_contents)
    dict_list = dict_to_sorted_list(character_count)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for item in dict_list:
        if not item["name"].isalpha():
            continue
        char = item["name"]
        num = item["num"]
        print(f"The '{char}' character was found {num} times")

    print("--- End report ---")


main()
