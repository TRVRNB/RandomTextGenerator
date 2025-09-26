import json, random, sys

EMOJIS = "🗿😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏🚀"

PARTS = (
"noun",
"pronoun",
"article",
"preposition",
"conjunction",
"proper_noun",
"verb",
"adjective",
"adverb",
)

STARTING_PARTS = (
    "noun",
    "noun",
    "pronoun",
    "proper_noun",
    "conjunction",
    "preposition",
    "article",
)

VALID_PARTS = {
	"noun": ("verb", "verb", "preposition"),
	"pronoun": ("verb", "verb", "adjective", "adverb"),
	"article": ("adjective", "adjective", "noun", "noun", "proper_noun"),
	"adjective": ("noun", "adjective", "adverb"),
	"verb": ("noun", "pronoun", "adverb", "preposition", "conjunction"),
	"adverb": ("verb", "adjective", "adverb"),
	"preposition": ("article", "article", "noun", "proper_noun", "pronoun"),
	"conjunction": ("noun", "pronoun", "article", "adjective", "verb"),
	"proper_noun": ("verb", "verb", "preposition"),
}



# open words.json and convert to dict
file = open("words.json", "r") # this is a 100 kb file!
WORD_LIST = file.read()
WORD_LIST = json.loads(WORD_LIST) # this should overwrite the original in memory?
print("• Successfully loaded and parsed words.json")

text = ""
paragraph_count = int(input("How many paragraphs?: "))
print("\n" + "-" * 100 + "\n")
for _ in range(paragraph_count):
    tense = random.choice(("past", "present", "neutral"))
    for _ in range(random.randint(1, 15)):
        sentence = ""
        next_part = random.choice(STARTING_PARTS)
        for i in range(9999): # extreme upper bound
            # choose a part
            part = next_part
            next_part = random.choice(VALID_PARTS[part])
            # verbs need tense to be specified
            if part == "verb":
                part += "_" + tense
            # choose a word
            weights = WORD_LIST[part].values()
            words = WORD_LIST[part].keys()
            word = random.choices(list(words), weights=list(weights), k=1)[0]
            # check for capitalization req.
            if part == "proper_noun" or word in ("i", "i'd", "i'm", "i've", "i'll"):
                word = word.capitalize()
            if "noun" in part and random.randint(1, 10) == 1:
                word += " " + random.choice(EMOJIS)
            # check for sentence end
            if part in ("noun", "proper_noun", "adverb", "adjective", "verb_neutral", "verb_past", "verb_present") and i > 0 and random.randint(1, 3) == 1:
                sentence += word
                if bool(random.getrandbits(1)): # period or just another clause?
                    sentence += "."
                    next_part = random.choice(STARTING_PARTS)
                    break
                else:
                    sentence += random.choice((",", ",", ",", ";")) + " " # easier than doing weights
                    next_part = "preposition"
            else:
                # add a space to the sentence, and a comma if there are 2 adjectives
                if part == "adjective" and next_part == "adjective" or part == "adverb" and next_part == "adverb":
                    sentence += word + ", "
                else:
                    sentence += word + " "

        text += sentence[0].upper() + sentence[1:] + " "
    text += "\n\n" # 2 lines

print(text.strip())
sys.stdout = open("output.txt", "w") # this makes all future print statements print directly to output.txt
print(text.strip())
input()
