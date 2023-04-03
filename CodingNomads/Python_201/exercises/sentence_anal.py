import re

string = "This is a lovely little I don't know how long sentence I'm going to break down into lower-case, upper-case letters plus non-alphanumerics."

def sentenceAnalysis(string):
    unspaced = string.replace(' ', '')
    alpha_only = re.sub('[^\w]','', unspaced)

    dict_out = {
        "Upper case":   len(re.sub('[^A-Z]', '', alpha_only)),
        "Lower case":   len(re.sub('[A-Z]', '', alpha_only)),
        "Punctuations": len(re.sub('[\w]','', unspaced)),
        "Total chars":  len(unspaced)
    }

    [print(f"{x[0]}: {x[1]}") for x in dict_out.items()]

    return dict_out

chk = sentenceAnalysis(string)


