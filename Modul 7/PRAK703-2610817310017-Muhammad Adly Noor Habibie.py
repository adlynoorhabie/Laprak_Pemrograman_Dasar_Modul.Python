sentence = input("kalimat: ").strip().lower().replace(" ", "")

print("jumlah vokal: ", sentence.count("a") + sentence.count("i") + 
    sentence.count("u") + sentence.count("e") + sentence.count("o"))

print("jumlah konsonan: ", len(sentence) - (sentence.count("a") + sentence.count("i") + 
    sentence.count("u") + sentence.count("e") + sentence.count("o")))