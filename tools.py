import basefamily

def b16_encode(msg:str)->str:
    return basefamily.base_encode(msg,'base16')

def b32_encode(msg:str)->str:
    return basefamily.base_encode(msg,'base32')

def b32hex_encode(msg:str)->str:
    return basefamily.base_encode(msg,'base32hex')

def b64_encode(msg:str)->str:
    return basefamily.base_encode(msg,'base64')

def b64urlsafe_encode(msg:str)->str:
    return basefamily.base_encode(msg,'base64urlsafe')



if __name__=='__main__':
    #str_hexstring('hello')
    print(b16_encode(b'foobar'))
    print(b32_encode('foobar'))
    print(b32hex_encode('foobar'))
    print(b64_encode('foobar'))
    print(b64urlsafe_encode('foobar'))