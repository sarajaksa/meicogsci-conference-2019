import os
import nltk


def get_topics_for_abstract(folder, filename, model, lem):
    with open(os.path.join(folder, filename)) as f:
        data = f.readlines()
        title = data[0].replace("... title: ", "").replace("\n", " ")
        data = " ".join(data).replace("... title: ", "").replace("\n", " ")
    data = data.lower()
    data_tok = nltk.tokenize.word_tokenize(data)
    data_tok = [lem.lemmatize(w) for w in data_tok]
    doc_topics, _, _ = model.get_document_topics(
        model.id2word.doc2bow(data_tok), per_word_topics=True
    )
    doc_topics = dict(doc_topics)
    new_row = []
    for i in range(21):
        if i in doc_topics:
            new_row.append(doc_topics[i])
        else:
            new_row.append(0)
    new_row.append(filename)
    new_row.append(title)
    return new_row
