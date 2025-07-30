import math
import base_dicts
# rfc4648 - Base16, Base32, and Base64
# https://www.rfc-editor.org/rfc/rfc4648

base_info = {
    'base16':{
        'diction':base_dicts.base16_dict,
        'digit':4,
        },
    'base32':{
        'diction':base_dicts.base32_dict,
        'digit':5,
        },
    'base32hex':{
        'diction':base_dicts.base32hex_dict,
        'digit':5,
        },
    'base64':{
        'diction':base_dicts.base64_dict,
        'digit':6,
        },
    'base64urlsafe':{
        'diction':base_dicts.base64urlsafe_dict,
        'digit':6,
        },
}
#bits with value zero are added (on the right) to form an integral number of n-bit groups.  
#Padding at the end of the data is performed using the padding character latter.
def count_padding(hex_string:str,n:int):
    '''
    cut msg into gorups that can transform wholy,like the 5 and 8 has the least common multiple number 40, 
    which means every 5bytes can change into 8bytes base32 result and so as base64, every 3bytes input get 4bytes result.
    the pad character here make sure reult length is as a norlmal result length.
    i.g., in Base32, 1 byte input get 2 byte output, so it need 6 pads to get 8bytes.
    '''
    quantum = math.lcm(8, n)
    num_padding = int(quantum/n) - math.ceil((len(hex_string) % quantum)/n) if (len(hex_string) % quantum)>0 else 0
    res = hex_string + '0'* (( n - len(hex_string)%n) if  len(hex_string)%n>0 else 0) 
    print(f" count pad: {num_padding}, \n fill result : {res}")
    return ( 
        res , num_padding,
    )

# get the hex_string of given string
# the hex_string of hello : 0110100001100101011011000110110001101111 (40)
def str_hexstring(msg)->str:
    if type(msg)==bytes:
        msg_ascii = msg.hex()
    else:
        msg_ascii = msg.encode(encoding='utf-8',errors='ignore').hex()
    hex_string =''
    for c in msg_ascii:
        hex_string += bin(int(c,16))[2:].zfill(4)
    print(f'the hex_string of {msg} :',hex_string,f'({len(hex_string)})')
    return hex_string

#split the given string into a list of fix_length substring
#split 0110100001100101011011000110110001101111, eahc 4 bits : 
#['0110', '1000', '0110', '0101', '0110', '1100', '0110', '1100', '0110', '1111']
def split_fixed(s: str, n: int):
    res = [s[i:i+n] for i in range(0, len(s), n)]
    print(f'split {s}, eahc {n} bits : \n{res}({len(res)})')
    return res

def lookup_base_dict(hexstr_list,algorithm,num_padding):
    algo_dict = base_info[algorithm]['diction']
    int_list = list(map(lambda t:int(t,2), hexstr_list))
    #print(int_list)
    char_list = list(map(lambda t:algo_dict[t], int_list))
    #print(char_list)
    raw_res = ''.join(char_list)
    print(f'before adding pad: {raw_res}({len(raw_res)})')
    padding = (algo_dict['pad'] * num_padding) if num_padding>0 else ''
    res = raw_res + padding
    print(f'--- the finnaly string : {res} \n')
    return res


# the standard is using ASCII code
def base_family(msg:str,algorithm:str)->str:
    hex_string,num_padding = count_padding(str_hexstring(msg),base_info[algorithm]['digit'])
    res_list = split_fixed(hex_string,base_info[algorithm]['digit'])
    res = lookup_base_dict(res_list,algorithm,num_padding) 
    return res

def base16(msg:str)->str:
    return base_family(msg,'base16')
def base32(msg:str)->str:
    return base_family(msg,'base32')
def base32hex(msg:str)->str:
    return base_family(msg,'base32hex')
def base64(msg:str)->str:
    return base_family(msg,'base64')
def base64urlsafe(msg:str)->str:
    return base_family(msg,'base64urlsafe')

if __name__=='__main__':
    #str_hexstring('hello')
    print(base16(b'foobar'))
    print(base32('foobar'))
    print(base32hex('foobar'))
    print(base64('foobar'))
    print(base64urlsafe('foobar'))