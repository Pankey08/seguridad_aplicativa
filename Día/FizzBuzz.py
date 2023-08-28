#programa de fizz buzz 

for contador in range (100):
    
    contador +=1
    
    if contador % 15 == 0:
        print("fizz buzz", contador)
        
    if contador % 3 == 0:
        print("fizz", contador)
        
    if contador % 5 == 0:
        print("buzz", contador)
