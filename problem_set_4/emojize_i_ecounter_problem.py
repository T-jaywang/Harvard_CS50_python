import emoji

input_text = input("Input: ")

if "_" in input_text:
    print("Output: ",emoji.emojize(input_text))

else:
    print("Output: ",emoji.emojize(input_text,language="alias"))