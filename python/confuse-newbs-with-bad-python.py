print(("Take an umbrella.", "Have a nice day!")[bool(__import__('re').match(r"^y$", input("Is it raining? "), __import__("re").IGNORECASE))])
