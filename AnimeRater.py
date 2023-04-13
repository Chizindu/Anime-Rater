

class show_list:
    

    def __init__(self, Anime):
        pass

    def search(Anime):   #adding a search function. (This is not complete)
        names = ("what anime are you looking into? ")
        print = ("The boys have rated ", names, "a ", Anime[names], "out of 10!")


    def rating(Anime): #function that takes the dictionary as an argument and finds the average
       
        #first we take the user input for what anime they are looking to rate
        names = input("what anime are you looking into?: ")
       
       #if the name is not already in the dictionary of anime's already present it will be added and asigned a value of 0 
        if names not in Anime:
            Anime[names] = 0
       
        #new_ave variable will be the number that will contribute to the average inputed by the user
        new_ave = int(input("Out of 10 what would you rate this anime?: "))
        
        # Misleading name will fix. This just adds the old average to the number provided in new_ave
        average = int(Anime[names] + new_ave)
       
        #This is to ensure that the first number added does not get divided by 2 so that the first number provided is the new average.
        #If the number is more than 0 the average of the 2 numbers will replace the old average
        if Anime[names]!= 0:
            Anime[names] = average/2
        elif Anime[names] == 0:
            Anime[names] = average
       
       #prints out the new average for the anime provided 
        print(Anime[names])

        #prints out the updated dictionary
        print(Anime)

    def run(): #function to keep the program going to add multiple ratings at once
       
        Anime = {} #initialized the dicttionary
        loop = True
        while loop:
            show_list.rating(Anime)
            stop = input("Would you like to stop yes or no?: ")
            print(Anime)
            
            if stop == 'yes':
                loop = False
            elif stop =='no':
                continue

    
show_list.run()