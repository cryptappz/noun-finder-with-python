from textblob import TextBlob

txt = """Natural language processing (NLP) is a field of computer science, artificial intelligence, and computational linguistics concerned with the interactions between computers and human (natural) languages."""
blob = TextBlob(txt)
print(blob.noun_phrases)
