# Q1/Write a method that will remove any given character from a String?
def remove_char(char, text):
 
 return text.replace(char,'')

# test remove_char() method
print("Q1 remove_char() method tests :\n")
print(remove_char(" ", "I love AI"))
print("-"*30) 
print(remove_char("_", "I_Love_Pyton"))

print("#" * 50)

# --------------------------------------------- #

# Q2/Write a program to find all prime numbers up to a given range of numbers?
print("Q2 find prime numbers program test :\n")

lower = 1
upper = 10

for n in range(lower, upper + 1):
   
   if n > 1:
       
       for i in range(2, n):
           
           if (n % i) == 0:
               
               break
       else:
           
           print(n)
           
print("#" * 50)

# --------------------------------------------- #

# Q3/write a function that count how many the given character repeated in a given string?
def repeated_count(char, text):
	
	return text.count(char)
	
# test repeated_count() method
print("Q3 repeated_count() method tests :\n")
print(repeated_count("l","Hello world"))
print("-"*30)
print(repeated_count("O","AI DOJO"))
