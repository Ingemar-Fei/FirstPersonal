'''
the test script and main script use the file
and in this file will call specific modulest 
'''

def turn_ascii(msg:str)->list[int]:
    # get singe letter's ascii code
    def get_ascii(letter:str)->int:
        return ord(letter)
    # trun a letter string to ascii code string
    return list(map(get_ascii,msg))
    

