with open('ready.rtf', 'w') as f:
    clean = f.writelines('This is what we are talking about as a group')
    print(clean)

with open('ready.rtf','r') as f:
    f_contents = f.read()
    print(f_contents)

