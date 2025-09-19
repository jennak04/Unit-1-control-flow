age = int(input("Enter Your Age: "))



if age: #validate
    rating = input("Input a movie rating (G, PG, PG-13, R): ")

    if rating == "G":
        print("APPROVED: You can watch this movie")
        
    elif rating == "PG" and age >= 13:
        print("APPROVED: You can watch this movie")
        
    else: 
        print("")
        
    
else: 
    print("ERROR: please enter your age")