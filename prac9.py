name = ("sasan" , "reza" , "neda" , "omid" , "reza" , "ali" , "zahra" ,
        "mahan" , "ashkan" , "reza")
convert_name = list(name)
count_name = convert_name.count("reza")
for i in range(count_name) :
    convert_name.remove("reza")
name = tuple(convert_name)
print("The new tuple of name =" , name)
