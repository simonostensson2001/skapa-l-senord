
import random
import array
#s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#s ={"small" : "abcdefghijklmnopqrstuvwxyz",
#    "big" : "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
#    "num" : "0123456789",
#    "special" : "!@#$%^&*()?"
#    }
#losen = 8
#p = "".join(random.sample(s, losen ))
#f= open("losenordfil.txt","a") 
#f.write(p)
#f.write("\n")


#s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#losen = 8
#p = "".join(random.sample(s, losen ))
#f= open("losenordfil.txt","a") 
#f.write(p)
#f.write("\n")




MAX_LEN = 12

LOCASE_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
UPCASE_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()?"
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
rand_digit = random.choice(DIGITS) 
rand_upper = random.choice(UPCASE_CHARACTERS) 
rand_lower = random.choice(LOCASE_CHARACTERS) 
rand_symbol = random.choice(SYMBOLS)
temp_pass = temp_pass + random.choice(COMBINED_LIST) 


#p = "".join(random.sample(losen ))
f= open("losenordfil.txt","a") 
f.write(p)
f.write("\n")