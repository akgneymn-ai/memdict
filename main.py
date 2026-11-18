meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "BRO": "Kardeşim, dostum",
    "OMG": "Şaşkınlık ifade eder",
    "GG": "İyi oyun",
    "EGO": "Kendini beğenmişlik",
    "SLAY": "Harika olmak",
    "NPC": "Kendi düşüncesi olmayan kişi"
}

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Bu kelime sözlükte bulunmuyor.")
