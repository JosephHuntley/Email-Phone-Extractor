import re
import pyperclip


phone_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                #Area code
(-|\s|\.)?                      #separator
(\d{3})                           #first 3 digits
(-|\s|\.)                       #separator
(\d{4})                           #last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?   #exstention
)''', re.VERBOSE)

email_regex = re.compile(r'''(
[0-9a-zA-Z_.%+-]*
@
[0-9a-zA-Z_.%+-]*
(\.com|\.edu|\.gov|\.org)
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3],groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('no phone numbers or email adresses found.')
