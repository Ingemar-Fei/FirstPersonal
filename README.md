# FirstPersonal
FirstPersonalProject on boot.dev course

# What this doing?
After done some Python and C progamming courses, I'm trying to do shits combining the Python and C language.
In this project , I'm trying to using C to write some libs like 'BASE family'(RFC4648)， and using python to do the test.

# Complie and test
This project is intend to run on Linux, using gcc-13-x86-64-linux-gnu and Python 3.12.3.
There will be a shell script to make .so lib and run a python unnit test script to test the C code.

# Project Plan
First it will be build in Python, run with CLI.
Then C will take some core work, at that time, add specif argument to run with C lib.
Finnally the C lib can be edited like a plug-in to make the whole program more possible functions.

# the path of this project
the base family algorithm:
    input (bytes) -> count_quantums -> each_quantum_transformation -> output(printable bytes)
i.g., 
    base64: 
    the quantum is LCM 8 and log2(base_digit) -> 8=4x2,6=3x2,LCM(6x8)=4x3x2=12 , which means
    each 24 bits ( 3 input bytes ) divde into groups of 6 bits and transform to 4 base64 bytes
    not all the time the last quantum of input is 3bytes, so add one pad for each missing bytes
    of 4 base64 bytes.
    'fooo' -> ( f o o ) (o - - ) -> ( 4 base64 bytes) ( 2 base64 bytes) -> add 2 pads

python:
    string/bytes (input) -> count_pads -> align_length -> lookup_dictionary -> add_pads -> output
