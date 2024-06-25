import spacy
import PyPDF2
from spacy import displacy

nlp=spacy.load("en_core_web_sm")
"""
doc=nlp(u"Tesla is looking at buying U.S. startup for $6 million")
for token in doc:
    print(token.text,token.pos_,token.dep_)

print(nlp.pipe_names)

doc2=nlp(u"tesla isn't looking into startup anymore.Eray so handsome")
print("\n\n\n")

for token2 in doc2.sents:
    print(token2)

print(doc2[8].is_sent_start)
print("\n\n\n")
print("\n\n\n")
for token2 in doc2.ents:
    print(token2)
    print(token2.label_)
    print(str(spacy.explain(token2.label_)))

doc3=nlp(u"Autonomous cars shift insurance liability toward manufacturers.")
print("\n\n\n")
for token3 in doc3.noun_chunks: #noun_chunks isimler icin ents ise ozel isimler icin
    print(token3)

doc4=nlp(u"This is a sentence.")
displacy.serve(doc,style="dep",port=5001)
"""

