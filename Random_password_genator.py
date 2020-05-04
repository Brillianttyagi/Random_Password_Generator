#importing shuffle and choice from random module
from random import shuffle,choice
#creating a list of character that we need in our password
lower_alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ['@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','&','#']
uppercase_alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#creating one list by lower_alphabet,num,symbols,uppercase_alphabets
all_char = lower_alphabets + num + symbols + uppercase_alphabets 


#loop contain bool value and used to generate while loop
loop = True
while(loop):  #loop
    #User enter length of password which is greater than 6 as now a days there is no password whose length is shorter than 6
    n = int(input("Enter length of password greater than 6 that you want>> "))

    if n>=6:
        #randomly select atleast one character from each list
        rand_lower_alphabets = choice(lower_alphabets)
        rand_upper_alphabets = choice(uppercase_alphabets)
        rand_symbols = choice(symbols)
        rand_num = choice(num)
        
        #combining all for character which we select above
        temp_password = rand_lower_alphabets + rand_upper_alphabets + rand_symbols + rand_num

        #now generating more character in our password until the length of password is equal to the length which user want
        for i in range(n-4):
            temp_password = temp_password + choice(all_char)
            

        #converting the string of temp_password into a list(which has string's each character as element) 
        temp_password_list = list(temp_password)

        #to avoid starting four character to be fixed(i.e 1st lower alphabets 2nd upper alphabets 3rd symobl amd 4th number)
        #we are shuffling again
        shuffle(temp_password_list)
        #creating password which contain empty string
        password = "" 

        #Now generating our final password
        for x in temp_password_list: 
            password = password + x 
        
        #print password
        print(password)
        #assigning loop = false so that our loop does not run again
        loop = False

    else:
        #if user enter length shorter than six 
        print("<<You entered a length which is smaller than 6\nTry Again??>>")
        #now loop again run