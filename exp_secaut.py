#!/usr/bin/env python3

# pwntools module for easy communication with service
# install on your machine via pip3 install --user pwntools
# or even look into setting up a python virtualenv if you want
# Documentation can be found at http://docs.pwntools.com/en/stable/
# You will probably need the Tubes section for communication
# http://docs.pwntools.com/en/stable/tubes.html 
# if you call this script using "python3 ./exp_skeleton.py DEBUG"
# you can see a lot more debug information like the network traffic
import pwn 

def guess_key(text):
    return "recovered_key"
    
def main():
    r = pwn.remote("vigenere.chals.fuzzy.land", 5200) # connect to the service
    r.recvuntil("============\n") # receive (and discard) all of the intro text including the ====
    text = r.recvuntil("============\n") # receive and save the ciphertext
    text = text.decode("utf-8") # we received raw bytes, interpret it as utf-8 text
    text = text.strip("\n"+"="*80+"\n") # strip the === from the ciphertext

    # recover the key
    recovered_key = guess_key(text)
    pwn.log.info("Keyguess = " + recovered_key)

    r.recvuntil("text:\n") # receive the rest of the prompt (one could also use r.recvline() multiple times)
    r.sendline(recovered_key) # send our recovered key

    response = r.recvall().decode("utf-8") # get all of the remaining response (this reads until server shuts down)
    pwn.log.info("Server response: " + response) # log the response on the console

if __name__ == "__main__":
    main()
