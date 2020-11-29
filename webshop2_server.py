#!/usr/bin/env python3

# Fix Python 2.x.
from __future__ import print_function
try: input = raw_input
except NameError: pass

import string, itertools, struct, random, base64, logging
#pip install gmpy2
from gmpy2 import powmod, gcd, invert

def print_flag():
    with open("./flag.txt", "r") as f:
        print(f.read())

class ElGamal():
    def __init__(self):
        """
        Initialize the parameters of the signature scheme
        """

        self.p = 26739716003959091706329826666827035087565335226699556698113932874616833767742741088982988953373585124757718534793111548922460518065117481332992168194995333444749347632145719971740258057888379516911991885908919887292279898987036050983559865286778100334222678601271996099712962547932267107780824312995388478263679638960032991772183901327443579296772974409322824649449372701994609834681484041361463741673587196144441502533820459072576111605463731784216269657735507697556147628171352499610534812102165891611117844482261390704160809945563448323948336055206321103025073060021966233533128545756065496894021269259244786473283
        self.g = 23312301520278371702503945778324996984449069913609515662774053679129969592722333640884694089391142680617698359553482492172938004265967411650179620180149559311984871859190771762454158039824722576140196322470125363944713142021363246002721465785110968122046379639525147005195137068184834823373805728469731175586698254364898485406109522826466969899796456811140875089036432730296989472382198625246234766759916058573378885318761007645223809357540283721271009575370095732666965349225931625120652881775311730702695312977148302308123790935542734216766047390665767488016604702310510955530609669800643127628994746363422416017065

        # we dont wanna leave our private key just out in the open...
        from secret import private_key
        self.x = private_key
        self.y = 2376273319883441079494463863888593579633723425450627354617300364421975116250401438849792327564277770213673496709228200505418495129400132023350681598576407447407517472656974365709823117878410332278341710626289124673999686484141746066820680775900265127908150487399967517546089605525812007621720595734533496921947268121187336667085324895818501645301605171002730253685034398908734763228538675175178454850015002567068010578398327221749510029789192675544008050801366314079030290750552850846856458804350539619011895370863866451143165472616316477321550435103292332587460010123459118268186793871579905864252066777311284942182
        assert self.y == powmod(self.g, self.x, self.p) # make sure we have the correct public key for the secret key
        print(self.y)
        self.rand = random.SystemRandom()

    def sign(self, m):
        """
        Signs the message m using the private key.
        Makes sure to generate a good randomness k, we don't want to be Sony...
        """
        assert(1 <= m <= self.p - 1)

        k = self.rand.randint(2, self.p - 2)
        while gcd(k, self.p - 1) != 1:
            k = self.rand.randint(2, self.p - 2)

        r = powmod(self.g, k, self.p)
        k_inv = invert(k, self.p-1)
        s = ((m - self.x * r) * k_inv ) % (self.p - 1)

        return (r,s)

    def verify(self, sig, m):
        """
        Verify a signature in the form (r,s) for a message m.
        Returns True if the signature sig verifies for the message m,
                False otherwise,
        """
        try:
            (r,s) = sig
            if not 1 < r < self.p:
                return False

            left = powmod(self.g, m, self.p)
            right = (powmod(self.y, r, self.p) * powmod(r, s, self.p)) % self.p
            return left == right
        except Exception as e:
            # print(e)
            return False

signature_scheme = ElGamal()

def generate_gift_voucher(amount):
    """
    Generate a gift voucher of the form amount:r:s,
    where (r,s) is an Elgamal signature for amount
    """
    (r,s) = signature_scheme.sign(amount)
    return str(amount)+":"+str(r)+":"+str(s)

def redeem_gift_voucher(voucher):
    voucher_parts =  voucher.split(":")
    m = int(voucher_parts[0])
    r = int(voucher_parts[1])
    s = int(voucher_parts[2])

    if signature_scheme.verify((r,s), m):
        return m
    else:
        raise ValueError("Invalid Voucher detected!")


def item_menu(state):
    while True:
        print("")
        print("Current Balance: {} ShopCoins".format(state["balance"]))
        print("1. Even Shinier Flag *New* - 99999 ShopCoins")
        print("2. Cat Picture       *New* - 1 ShopCoin")
        print("3. Dog Picture       *New* - 1 ShopCoin")
        print("4. Squirrel Picture  *New* - 2 ShopCoin")
        print("5. Fish Picture      *New* - 2 ShopCoin")
        print("6. Exit")
        choice = input("> ")
        try:
            choice = int(choice.strip())
        except Exception as e:
            continue

        if choice == 1:
            if state["balance"] >= 99999:
                state["balance"] -= 99999
                print_flag()
            else:
                print("Not enough money")
            continue

        if choice == 2:
            if state["balance"] >= 1:
                state["balance"] -= 1
                print("https://tinyurl.com/cat2-pic-webshop")
            else:
                print("Not enough money")
            continue
        if choice == 3:
            if state["balance"] >= 1:
                state["balance"] -= 1
                print("https://tinyurl.com/dog2-pic-webshop")
            else:
                print("Not enough money")
            continue
        if choice == 4:
            if state["balance"] >= 2:
                state["balance"] -= 2
                print("https://tinyurl.com/squirrel-pic-webshop")
            else:
                print("Not enough money")
            continue
        if choice == 5:
            if state["balance"] >= 2:
                state["balance"] -= 2
                print("https://tinyurl.com/fish-pic-webshop")
            else:
                print("Not enough money")
            continue

        if choice == 6:
            return

def menu():
    state = None
    while True:
        print("")
        if state == None:
            print("Welcome to WebShop 2.0, with improved security. Please register:")
            name = input("Name: ")
            state = { "name" : name, "balance" : 0, "redeemed_voucher" : False }
            print("Happy to welcome you as a customer {}".format(name))
            print("As a token of our gratitude, here is a secure voucher for one ShopCoin")
            print("="*80)
            print(generate_gift_voucher(1))
            print("="*80)
            print("Happy Shopping!\n")

        print("Welcome {}. Current Balance: {} ShopCoins".format(state["name"], state["balance"]))
        print("1. Buy Items")
        print("2. Buy more ShopCoins")
        print("3. Redeem Voucher")
        print("4. Exit")

        choice = input("> ")
        try:
            choice = int(choice.strip())
        except Exception as e:
            continue

        if choice == 1:
            item_menu(state)
            continue

        if choice == 2:
            print("Online payment system coming soon...")
            continue

        if choice == 3:
            if state["redeemed_voucher"]:
                print("You already redeemed a voucher, only one voucher allowed per person")
                continue

            voucher = input("Please enter your gift voucher: ").strip()
            try:
                amount = redeem_gift_voucher(voucher)
            except Exception as e:
                # print(e)
                print("Failed to process voucher")
                continue
            state["balance"] += amount
            state["redeemed_voucher"] = True
            print("successfully redeemed voucher")
            continue

        if choice == 4:
            print("Until next time")
            return


if __name__ == "__main__":
    menu()
