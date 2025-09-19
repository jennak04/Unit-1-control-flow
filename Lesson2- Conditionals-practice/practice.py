age = int(input("Enter Your Age: "))



if age: #validate
    rating = input("Input a movie rating (G, PG, PG-13, R): ")

    if rating == "G":
        print("APPROVED: You can watch this movie")
        
    elif rating == "PG" and age >= 6:
        print("APPROVED: You can watch this movie")
        
    elif rating == "PG-13" and age >= 13:
        print(f"APPROVED: You can watch a {rating} movie")
        
    else: 
        print("WARNING: Not recomended for your age")
        
    if rating == "R" and age > 17:
        print("APPROVED: You can watch this movie")
        
    else:
        print("DENIED: must be 17+ for R-rated movies")
        

        
    
else: 
    print("ERROR: please enter your age")