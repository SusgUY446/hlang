
user_input = input()

words = user_input.split()

if words[0] == "say":
    if len(words) >= 2:
        temp_storage = words[1]
        print(f"{temp_storage}")
    else:
        print("")
else:
  if words[0] == "stop":
    pass
