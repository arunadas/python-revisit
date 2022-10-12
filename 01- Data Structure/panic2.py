phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# print(plist[1:3])
# print(plist[5:3:-1])
# print(plist[7:5:-1])
  
new_phrase = ''.join(plist[1:3] + plist[5:3:-1] + plist[7:5:-1])

print(plist)
print(new_phrase)