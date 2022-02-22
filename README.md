# password-checker

usage:
'''sh
python  checkpass.py [password1_to_check] [password2_to_check]
'''

Example:
'''sh
python checkpass.py password123 hello123 '$tRoNG_P@s$w0rD!'
'''

Output:
'''sh
[+] -> [password123] was found 248071 times ... you should change your password
[+] -> [hello123] was found 271016 times ... you should change your password
[+] -> [$tRoNG_P@s$w0rD!] was not found. 
done!
'''
