def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        num_words = word_count(text)
        char_dict = character_count(text)
        char_list= dic_to_list(char_dict)
        char_list.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"There are {num_words} found in this document.")
        for item in char_list:
            char = item["character"]
            count = item["count"]
            print(f"The {char} character was found {count} times")
    print("--- End report---")
            



def word_count(text):
    all_words = text.split()
    return len(all_words)

def character_count(text):
    num_characters = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character in num_characters:
            num_characters[character] += 1
        else:
            num_characters[character]=0
    return num_characters
        
def dic_to_list(dict):
    letter_count=[]
    for char, count in dict.items(): 
        if char.isalpha():
            letter_count.append({"character":char, "count":count})
    return letter_count

def sort_on(dict):
    return dict["count"]
    

main()
