#program for code decode
message="danger"
i=0
while i<len(message):
    letter=message[i]
    print(chr(ord(letter)+2),end=" ")
    i=i+1