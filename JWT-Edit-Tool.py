# NOTE: Copy JWT value below ( JWT = 'ENTER HERE' ) will show decoded jwt, and allow for edit of json values in header, & body (payload).
# NOTE: Signature will not change. Can copy & paste original signature, or leave off altogether. (i.e. alg: 'none')
   
import base64
import json

JWT = "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6NzEsInVzZXJuYW1lIjoiTkVXVVNFUk5BTUUiLCJleHBpcmF0aW9uIjoyMDIzNjA3OTkyNjkwfQ.yMurNH4Mqw1-bWqMsneAqYnkTvXMHtA5P7ydTgxMnLA"

jwtsplit = JWT.split(".")      
jwtsplit1 = (jwtsplit[0])
jwtsplit2 = (jwtsplit[1])
jwtsplit3 = (jwtsplit[2])
split1len = (len(jwtsplit1))
split2len = (len(jwtsplit2))

remndr1 = (split1len % 4) #NOTE: Check Remainder for Modulus of 4, add = padding
if remndr1 == 0:
    pass
elif remndr1 == 1:    
    jwtsplit1 = (jwtsplit1 + "===")
elif remndr1 == 2:
    jwtsplit1 = (jwtsplit1 + "==")
elif remndr1 == 3:
    jwtsplit1 = (jwtsplit1 + "=")
       

remndr2 = (split2len % 4) #NOTE: Check Remainder for Modulus of 4, add = padding
if remndr2 == 0:
    pass
elif remndr2 == 1:    
    jwtsplit2 = (jwtsplit2 + "===")
elif remndr2 == 2:
    jwtsplit2 = (jwtsplit2 + "==")
elif remndr2 == 3:
    jwtsplit2 = (jwtsplit2 + "=") 

print("")
print("Target Json Web Token")
#print("Header: ", jwtsplit1)
#print("Body: ", jwtsplit2)
#print('')
#print("Signature: ", jwtsplit3)
#print('')
#print('Base64 Decoded JWT - Header and Body')
split1d = base64.b64decode(jwtsplit1)
split2d = base64.b64decode(jwtsplit2)
#print(split1d)
#print(split2d)

json1d = json.loads(split1d) # Json Output for decoded HEADER
print(f'Source JWT Header = ', jwtsplit1)
print('Decoded, json format: =  ', json1d)
print("")
json2d = json.loads(split2d) # Json Output for decoded HEADER
print('Source JWT Body = ', jwtsplit2)
print('Decoded, json format: = ', json2d)
print("")

# Decode the first part (header) and load it as a JSON
header = base64.urlsafe_b64decode(jwtsplit1 + "==")
header_json = json.loads(header) # Load header into json format

edit_header_key = input('Header : Enter key for json value to edit (enter for no change)...... ') # Provide key string only
edit_header_value = input('Header : Enter Value for chosen key (enter for no change)......') # Provide json value string only 
header_json[edit_header_key] = (edit_header_value)  # NOTE: Change value of desired json key in header
modified_header = base64.urlsafe_b64encode(json.dumps(header_json).encode()).decode().rstrip("=")

# Adding code for body key value edit 
payload = base64.urlsafe_b64decode(jwtsplit2 + "==")
payload_json = json.loads(payload) # Load header into json format

edit_payload_key = input('Payload : Enter key for json value to edit (enter for no change)...... ') # Provide key string only
edit_payload_value = input('Payload : Enter Value for chosen key (enter for no change)......') # Provide json value string only 
payload_json[edit_payload_key] = (edit_payload_value)  # NOTE: Change value of desired json key in header
modified_payload = base64.urlsafe_b64encode(json.dumps(payload_json).encode()).decode().rstrip("=")



print("")
print("Modified Header = ", modified_header)
print("Decoded, json format: = ", (header_json))
print("")
print ("Modified Payload = ", modified_payload)
print("Decoded, json format: = ", (payload_json))
print("")
print(f'New JWT = {modified_header}.{modified_payload}')