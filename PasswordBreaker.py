import os
import math
#Entire Character List is on next line. Currently included list is a-z, A-Z, 0-9
#['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','~','`','_','-','+','=','[',']','{','}',':',';','"',"'",'<',',','>','.','?','/','|','\\']

checkedCharactersList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
checkedCharactersCounterList = []
password = str('Ca7')

def main():
    for charlength in range(3):#Change to len of password variable. Determine the length of the password (Number of characters) we are testing for
        flag = False
        print("Current Password Testing Length: " + str(charlength + 1))
        checkedCharactersCounterList = []

        for i in range(charlength + 1): #Creating a counter for each character position
            checkedCharactersCounterList.append(0)

        for currentTestNumber in range(int(math.pow(len(checkedCharactersList), charlength + 1))): #Create every single character combination for the current password character length, and test it
            
            print("Current password being tested (In Numbers) is: " + str(checkedCharactersCounterList))
            testPassword = "" #Set the testPassword to nothing, so appending the password characters doesn't add characters from the previous tests.

            for x in checkedCharactersCounterList: #Turning the current values of each count position into characters for the password
                testPassword += checkedCharactersList[x]
            
            print("Current password being tested (In Letters) is: " + testPassword)

            if testPassword == password: #Test to see if the test password is the same as the password we are searching for. 
                print("Password Found")
                flag = True
                break

            for charPos in range(len(checkedCharactersCounterList)): #Adds 1 to the first number (leftmost) in checkedCharactersCounterList. Once this reaches the max amount of characters (scanned through all possible characters to check for) (len(checkedCharactersList) - 1), then it resets to the first character, and makes the next position to the right increase by one. If that is at max, it sets to zero. This repeats until all characters are tested in all slots, or password is found.
                if checkedCharactersCounterList[charPos] == (len(checkedCharactersList) - 1):
                    checkedCharactersCounterList[charPos] = 0
                elif checkedCharactersCounterList[charPos] < (len(checkedCharactersList) - 1):
                    checkedCharactersCounterList[charPos] += 1
                    break
                elif checkedCharactersCounterList[charPos] > (len(checkedCharactersList) - 1):
                    checkedCharactersCounterList[charPos] = 0
                    print("Error: Counting above checkedCharactersList's number of characters" + str(charPos) + checkedCharactersCounterList[charPos])
               
        if flag: #If password is found, exit the loop
            break
main()
