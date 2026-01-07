from wordfreq import zipf_frequency
import spacy
from letter_freq import letter_freq
import math

def load_words_set(filename="words.txt"):
    with open(filename, "r") as f:
        return set(line.strip().lower() for line in f if line.strip())
    
words_set = load_words_set()
nlp = spacy.load("en_core_web_lg")

def letter_points(placed_letters: str) -> float:
    placed_letters = placed_letters.lower()
    sum = 0
    for letter in placed_letters:
        sum += 210000 / float(letter_freq[letter])
    return sum

def rarity_points(word: str):
    def lemmatize_word(word: str) -> str:
        doc = nlp(word)
        return doc[0].lemma_
    def activation_function(num: float) -> float:
        return round(8 - num, 1)
    return activation_function(zipf_frequency(lemmatize_word(word), "en"))

def total_points(word: str) -> str:
    word = word.lower()
    if not word.isalpha():
        print('Word must be comprised of letters only!')
        return
    if not word in words_set:
        print('Not a valid word!')
        return

    return round(
        rarity_points(word) +
        letter_points(word)
    )

if __name__ == "__main__":
    #for word in ["The", "Puddle", "Exquisite", "Achoo", "Fuchsia", "Elixir", "Snort", "Whoops"]:
    #    print(f"{word}:\n    Letter Points: {round(letter_points(word))}\n    Rarity Points: {round(rarity_points(word))}\nTotal Points: {total_points(word)}\n")
    print(f'The: {rarity_points("The")}')
    print(f'A: {rarity_points("A")}')
    print(f'Hello: {rarity_points("Hello")}')
    print(f'Elixir: {rarity_points("Elixir")}')
    print(f'Achoo: {rarity_points("Achoo")}')
    print(f'Thaw: {rarity_points("Thaw")}')
    print(f'Psst: {rarity_points("Psst")}')
    print(f'Oops: {rarity_points("Oops")}')
    print(f'Zoom: {rarity_points("Zoom")}')
# next, make a dictionary of all words and their points!
