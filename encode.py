#!/usr/bin/env python3
import sys
sys.path.append('.')
import tools

valid_base = (
    'base16',   'base32',   'base32hex',    'base64',   'base64urlsafe',
    )
# encode.py base64 xxx
algorithm = sys.argv[1]
input = sys.argv[2:]
msg = ' '.join(input)

print(f'---{algorithm}:{msg}---')
if algorithm not in valid_base:
    raise(Exception(f"valid base : {' '.join(valid_base)}")) 
match algorithm:
    case 'base16':
        tools.b16_encode(msg)
    case 'base32':
        tools.b32_encode(msg)
    case 'base32hex':
        tools.b32hex_encode(msg)
    case 'base64':
        tools.b64_encode(msg)
    case 'base64urlsafe':
        tools.b64urlsafe_encode(msg)


