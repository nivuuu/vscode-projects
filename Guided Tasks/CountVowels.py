# Guided Task 4: Python Programming Basics | DOL4 A2.1 |                    Eryk A Grabowski  13/09/2022
# string containing all vowels
def Check_Vow(string, vowels):
	final = [each for each in string if each in vowels]
	print(len(final))
	print(final)
	
# Driver Code
string = "Test String"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels);

