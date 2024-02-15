# DeizToolz

 🧐 Helpful Tools &amp; Scripts 🧐

This Repo contains many assorted utilities that I have created for various projects. 
Hope that this may help others in the same way, or at least as a starting point for similar projects. 

Primarily Python & Javascript files related to security 🤫, authentication, JSON, data transformation, etc. 

includes :
JWT-Edit-Tool.py : Simple utility for Json Web Tokens to split, decode, and edit the json values.

Usage:                   (Great for simple editing of JWT values.)

Paste JWT into file : Line 6 : JWT = 'PASTE JWT HERE'.
Run file : python JWT-Edit-Tool.py
JWT header & payload will be displayed in original & decoded json format.
If you want to change the value of a field in the header, or create a new key : Value pair, 
enter existing / new key name at first prompt. 
If no changes desired, leave blank & press enter.

Repeat process for the header key on next line. 
Type existing / new key or press enter to leave as is. 
Third prompt will take a new key for the "PAYLOAD" portion, or press Enter for no change. 
Fourth prompt will take new value for the key input above, or press Enter for no change.

NOTE: Thi wil not provide an acccurate signature, if values change. 
Signature will be ignored, Copy original signature to the end of new JWT on output if 3 part format is required.

example:
JWT = "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6NzEsInVzZXJuYW1lIjoiTkVXVVNFUk5BTUUiLCJleHBpcmF0aW9uIjoyMDIzNjA3OTkyNjkwfQ.yMurNH4Mqw1-bWqMsneAqYnkTvXMHtA5P7ydTgxMnLA"

python JWT-Edit-Tool.py
-- OUTPUT --
Target Json Web Token
Source JWT Header =  eyJhbGciOiJIUzI1NiJ9
Decoded, json format: =   {'alg': 'HS256'}

Source JWT Body =  eyJpZCI6NzEsInVzZXJuYW1lIjoiTkVXVVNFUk5BTUUiLCJleHBpcmF0aW9uIjoyMDIzNjA3OTkyNjkwfQ==
Decoded, json format: =  {'id': 71, 'username': 'NEWUSERNAME', 'expiration': 2023607992690}

Header : Enter key for json value to edit (enter for no change)...... alg
Header : Enter Value for chosen key (enter for no change)......none 
Payload : Enter key for json value to edit (enter for no change)...... username
Payload : Enter Value for chosen key (enter for no change)......admin

Modified Header =  eyJhbGciOiAibm9uZSJ9
Decoded, json format: =  {'alg': 'none'}

Modified Payload =  eyJpZCI6IDcxLCAidXNlcm5hbWUiOiAiYWRtaW4iLCAiZXhwaXJhdGlvbiI6IDIwMjM2MDc5OTI2OTB9
Decoded, json format: =  {'id': 71, 'username': 'admin', 'expiration': 2023607992690}

New JWT = eyJhbGciOiAibm9uZSJ9.eyJpZCI6IDcxLCAidXNlcm5hbWUiOiAiYWRtaW4iLCAiZXhwaXJhdGlvbiI6IDIwMjM2MDc5OTI2OTB9
