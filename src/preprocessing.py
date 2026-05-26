import re

def clean_text(text):
    # 1. Transformare în lowercase (litere mici)
    text = str(text).lower()
    
    # 2. Eliminare link-uri / URL-uri
    text = re.sub(r"http\S+|www\S+", "", text)
    
    # 3. Eliminare caractere speciale si numere (pastram doar litere si spatii)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    
    # 4. Eliminare spatii multiple si spatii de la începutul/finalul textului
    text = re.sub(r"\s+", " ", text).strip()
    
    return text