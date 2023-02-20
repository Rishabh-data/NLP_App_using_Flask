import paralleldots
paralleldots.set_api_key('NBwUdfcFuhQ8p01lgsWCa3hcXRlVJBCNPxV1ZMouI5s')
def ner(text):
    ner = paralleldots.ner(text)
    return ner

