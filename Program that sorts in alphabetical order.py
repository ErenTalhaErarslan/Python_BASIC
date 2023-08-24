#Program that sorts in alphabetical order

my_str = str(input("Lütfen Kelime Giriniz : "))

words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are:")
for word in words:
  print(word)
