def get_num_words(text):
    words = text.split()
    return len(words)

# takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string
def count_characters(text) -> dict:
    char_count = {}
    for char in text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

#takes the dictionary of characters and their counts and returns a sorted list of dictionaries
# Each dictionary should have two key-value pairs: one for the character itself and one for that character's count (e.g. {"char": "b", "num": 4868})
def sort_character_counts(char_count: dict) -> list:
    sorted_counts = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return [{"char": char, "num": count} for char, count in sorted_counts]
    