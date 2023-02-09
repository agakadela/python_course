# Today we are going to make a username generator!
# Your tasks are:
#####################################################
# 1. Create and display a greeting message - for example: "Welcome to the username generator"
print("Welcome to the username generator!")
#####################################################
# 2. Ask the user for their name. Assign it to a separate variable
name = input("What's your name?")
#####################################################
# 3. Ask the user for the city that they live in. Assign it to a separate variable
city = input("What's the city you currently live in?")
#####################################################
# 4. Check how many characters the city has and assign it to a separate variable.
# Please convert this number to a string!
city_length = str(len(city))
#####################################################
# 5. Combine the name, the city and the city length number into one string and show it to the user.
# Start with the summary message, for example: "Your username could be:"
print("Your username could be: " + name + city + city_length)
