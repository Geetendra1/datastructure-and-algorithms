test_number = 966969
 
# using str() + string slicing
# for checking a number is palindrome
res = str(test_number) == str(test_number)[::-1]
 
# printing result
print ("Is the number palindrome ? : " + str(res))