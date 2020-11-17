[comment] v17.11.2020 temp

### protocol

The service, described in [this post by Troy Hunt](https://www.troyhunt.com/ive-just-launched-pwned-passwords-version-2/), relies on the mathematical property called k-anonymity. The first 5 charachters of the SHA-1, of the password we want to check, is sent to the API. E.g. "21BD1" of the SHA-1 "21BD12DC183F740EE76F27B78EB39C8AD972A757" for the password "P@ssword". The service responds with all suffixes ot SHA-1 strings that also match these first 5 characters. For example:

1.  (21BD1)  **0018A45C4D1DEF81644B54AB7F969B88D65:1**  (password "lauragpe")
2.  (21BD1)  **00D4F6E8FA6EECAD2A3AA415EEC418D38EC:2**  (password "alexguo029")
3.  (21BD1)  **011053FD0102E94D6AE2F8B83D76FAF94F6:1**  (password "BDnd9102")
4.  (21BD1)  **012A7CA357541F0AC487871FEEC1891C49C:2**  (password "melobie")
5.  (21BD1)  **0136E006E24E7D152139815FB0FC6A50B15:2**  (password "quvekyny")
6.  ...

So the HIBP service would never be able to conjure the original password we made the SHA-1 of.

#### How can we now check if the password is already pwned?
We simply try to find the suffix of our SHA-1, means the remainder after the first 5 characters, in the result set from the service. If this suffix is found, then password hash is already in their database and therefore pwned.
Details on the API consumation is described here: https://haveibeenpwned.com/API/v2#PwnedPasswords
