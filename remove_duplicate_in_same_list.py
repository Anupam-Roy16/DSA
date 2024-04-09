s=[1,2,2,7,7,9,9,10,11,12,13,13,14]
current_index=1
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        s[current_index]=s[i]
        current_index=current_index+1
print(current_index)
print(s[:current_index])