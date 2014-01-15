# strings.py
# CS 1 class examples to show some string functions.

string_list = ["lions", "tigers", "bears"]
sentence = "and".join(string_list)
print sentence

sentence = " and ".join(string_list)
print sentence


from re import findall

## Suppose we have a text with many email addresses
text = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here findall returns a list of all the found email strings
## ['alice@google.com', 'bob@abc.com']
emails = findall(r'[\w\.-]+@[\w\.-]+', text) 

for email in emails:
    # do something with each found email string
    print email