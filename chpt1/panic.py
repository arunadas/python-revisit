phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)


# letters_to_remove = ['D',"'"," ",'i','c','!']
# for i in letters_to_remove:
#     plist.remove(i)
    
# plist.insert(2,' ')
# plist.insert(4,'a')

# for i in range(2):
#     plist.pop()

for i in range(4):
    plist.pop()
plist.pop(0) 
plist.remove("'")
plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))   

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)