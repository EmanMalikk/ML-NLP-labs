import emoji
import regex
text = "We want to extract these emojis"
emojis =regex.findall (r' [^\w\s,. ]', text)
print(emojis)



text ="We want to extract these emojis"

print (text)

def remove_emoji(string):
     emoji_pattern= regex.compile("["
                         u"\U0001F600-\U0001F64F" 
                         u"\U0001F300-\U0001F5FF" 
                         u"\U0001F680-\U0 001F6FF" 
                         u"\U0001F1E0-\U0001F1FF" 
                         u"\U00002702-\0000027B0"
                         u"\U000024C2 \U0001F251"
                         "]+", flags=regex.UNICODE)
     return emoji_pattern.sub(r'', string)
text1 = remove_emoji (text)
print(text1)


text = "We want to extract these emojis"
print (text)

replaced_text= emoji.demojize (text)
print (replaced_text)


