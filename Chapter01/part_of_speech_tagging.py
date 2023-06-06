import spacy

nlp = spacy.load("en_core_web_sm")


def pos_tagging(text):
    doc = nlp(text)
    for token in doc:
        print(f"Token: {token.text}, Coarse-grained POS-Tag: {token.pos_}")
        print(f"Token: {token.text}, Fine-grained POS-Tag: {token.tag_}")
        print("--")


if __name__ == "__main__":

    text = "Alexander Bell who was a Scottish scientist is credited with inventing the first practical telephone"
    pos_tagging(text)