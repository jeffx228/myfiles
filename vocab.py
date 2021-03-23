# coding=utf-8

import spacy
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher

def get_phrase_matches(str, list):
    m_tool = Matcher(nlp.vocab)
    matches = 0

    vocab = []

    for word in list:
        vocab.append([{"TEXT": word}])

    m_tool.add("MATCH", vocab)

    phrase_matches = m_tool(str)

    for match_id, start, end in phrase_matches:
        matches += 1
        string_id = nlp.vocab.strings[match_id]  
        span = doc[start:end]                   
        print(match_id, string_id, start, end, span.text)

    print("Number of Matches: ")
    print(matches)



# with a precreated vocab list, this code can comb through text,
# count the number of matches with vocab words (without repeats),
# and return the result.
text = "The state was named for the Colorado River, which Spanish travelers named the Río Colorado for the ruddy silt the river carried from the mountains. The Territory of Colorado was organized on February 28, 1861, and on August 1, 1876, U.S. President Ulysses S. Grant signed Proclamation 230 admitting Colorado to the Union as the 38th state. Colorado is nicknamed the Centennial State because it became a state a century after the signing of the United States Declaration of Independence. Colorado is bordered by Wyoming to the north, Nebraska to the northeast, Kansas to the east, Oklahoma to the southeast, New Mexico to the south, Utah to the west, and touches Arizona to the southwest at the Four Corners. Colorado is noted for its vivid landscape of mountains, forests, high plains, mesas, canyons, plateaus, rivers, and desert lands. Colorado is part of the western or southwestern United States, and one of the Mountain States. Denver is the capital and most populous city of Colorado. Residents of the state are known as Coloradans, although the antiquated term Coloradoan is occasionally used."

doc = nlp(text)


print("Writing sample: ")
print(text)


# tok = ld.tokenize(text)

# res = [] 
# for i in tok:
#     i.lower() 
#     if i not in res: 
#         res.append(i) 


patterns = [[{"TEXT": "state"}], [{"TEXT": "ruddy"}], [{"TEXT": "silt"}], [{"TEXT": "aggregate"}]]

vocab = ["state", "ruddy", "silt", "aggregate", "Colorado"]


print("Vocab words: ")
print(vocab)

get_phrase_matches(doc, vocab)


# vocab_counter = 0

# words_used = []

# for i in res:
#     for word in vocab:
#         if (word == i):
#             vocab_counter += 1
#             words_used.append(word)


# print("Number of vocab words used: ")
# print(vocab_counter)

# print("Words used: ")
# print(words_used)