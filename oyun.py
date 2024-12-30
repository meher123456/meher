print("Hos geldiniz")
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap","CREEPY":"korkunc birsey"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
if word in meme_dict.keys():
    print(word,)
    
else:
    print("Boyle bir soz yok!")
