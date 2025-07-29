import math
import base_dicts
# rfc4648 - Base16, Base32, and Base64
# https://www.rfc-editor.org/rfc/rfc4648

#bits with value zero are added (on the right) to form an integral number of n-bit groups.  
#Padding at the end of the data is performed using the padding character latter.
def count_padding(hex_string:str,n:int):
    num_padding = n - (len(hex_string) // n)
    return ( 
        hex_string.zfill(len(hex_string)+num_padding), num_padding,
    )

#split the given string into a list of fix_length substring
#split 0110100001100101011011000110110001101111, eahc 4 bits : 
#['0110', '1000', '0110', '0101', '0110', '1100', '0110', '1100', '0110', '1111']
def split_fixed(s: str, n: int):
    res = [s[i:i+n] for i in range(0, len(s), n)]
    print(f'split {s}, eahc {n} bits : \n{res}({len(res)})')
    return res

# get the hex_string of given string
# the hex_string of hello : 0110100001100101011011000110110001101111 (40)
def str_hexstring(msg:str)->str:
    hex_string =''
    msg_ascii = msg.encode(encoding='ascii',errors='ignore').hex()
    for c in msg_ascii:
        hex_string += bin(int(c,16))[2:].zfill(4)
    print(f'the hex_string of {msg} :',hex_string,f'({len(hex_string)})')
    return hex_string

def lookup_base_dict(hexstr_list,algorithm,num_padding):
    dicts = {
        'base16':base_dicts.base16_dict
    }
    int_list = list(map(lambda t:int(t,2), hexstr_list))
    #print(int_list)
    char_list = list(map(lambda t:dicts[algorithm][t], int_list))
    #print(char_list)
    raw_res = ''.join(char_list)
    print(f'before adding padding: {raw_res}({len(raw_res)})')
    padding = (dicts[algorithm]['padding'] * num_padding) if num_padding>0 else ''
    res = raw_res + padding
    print(f'the finnaly string : {res}')
    return res


# the standard is using ASCII code
def base16(msg:str)->str:
    hex_string,num_padding = count_padding(str_hexstring(msg),4)
    res_list = split_fixed(hex_string,4)
    res = lookup_base_dict(res_list,'base16',num_padding) 
    return res

if __name__=='__main__':
    #str_hexstring('hello')
    print(base16('foobar'))