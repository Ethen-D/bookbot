def main():
    path = "books/frankenstein.txt"
    contents = get_contents(path)
    count = get_count(contents)
    char_count = get_char_count(contents)
    print_report(char_count)
    #print(contents)
    #print(count)
    #print(char_count)

def get_contents(path):
    with open(path) as f:
        return f.read()

def get_count(contents):
    words = contents.split()
    return len(words)

def get_char_count(contents):
    lower_cases = contents.lower()
    count_dict = {}
    for char in lower_cases:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict

def print_report(dict1):
    for char in dict1:
        if char.isalpha():
            print(f"The '{char}' character was found {dict1[char]} times")
    print(f"--- End report ---")

main()