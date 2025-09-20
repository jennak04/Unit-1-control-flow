age = int(input("Enter Your Age: "))



if age: #validate
    rating = input("Input a movie rating (G, PG, PG-13, R): ")
    if rating == "G":
        print("APPROVED: You can watch this movie")
         
    elif rating == "PG":
        if age >= 6:
            print("APPROVED: You can watch this movie")
            
        else: 
            print("WARNING: Not recomended for your age")

        
    elif rating == "PG-13":
        if age >= 13:
            print("APPROVED: You can watch this movie")
            
        else: 
            print("WARNING: Not recomended for your age")
        
    elif rating == "R":
        if age > 17:
            print("APPROVED: You can watch this movie")
        
        else:
            print("DENIED: must be 17+ for R-rated movies")
    
else: 
    print("ERROR: please enter your age")