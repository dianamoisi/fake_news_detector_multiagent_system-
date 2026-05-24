import re

def clean_text(text):
    # 1. Transformare în lowercase (litere mici)
    text = str(text).lower()
    
    # 2. Eliminare link-uri / URL-uri
    text = re.sub(r"http\S+|www\S+", "", text)
    
    # 3. Eliminare caractere speciale și numere (păstrăm doar litere și spații)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    
    # 4. Eliminare spații multiple și spații de la începutul/finalul textului
    text = re.sub(r"\s+", " ", text).strip()
    
    return text