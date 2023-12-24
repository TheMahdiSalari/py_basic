sentences = input("Please write your sentence :\n")
print("--------------------------------")
special_words = ["can" , "strong" , "positive" , "beautiful"]
positive_words =""
for i in sentences.split(" ") :
    if i in special_words :
        positive_words = [i]
        print("Your positive words :" , positive_words) 