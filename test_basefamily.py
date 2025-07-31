import unittest
import basefamily

class TestBaseFamily(unittest.TestCase):
    testset = {
        'base16':[
            ("f","66"),
            ("fo","666F"),
            ("foo","666F6F"),
            ("foob","666F6F62"),
            ("fooba","666F6F6261"),
            ("foobar","666F6F626172"),
        ],
        'base32':[
            ("",""),
            ("f","MY======"),
            ("fo","MZXQ===="),
            ("foo","MZXW6==="),
            ("foob","MZXW6YQ="),
            ("fooba","MZXW6YTB"),
            ("foobar","MZXW6YTBOI======"),
        ],
        'base32hex':[
            ("",""),
            ("f","CO======"),
            ("fo","CPNG===="),
            ("foo","CPNMU==="),
            ("foob","CPNMUOG="),
            ("fooba","CPNMUOJ1"),
            ("foobar","CPNMUOJ1E8======"),
        ],
        'base64':[
            ("",""),
            ("f","Zg=="),
            ("fo","Zm8="),
            ("foo","Zm9v"),
            ("foob","Zm9vYg=="),
            ("fooba","Zm9vYmE="),
            ("foobar","Zm9vYmFy"),
        ],
        'base64urlsafe' : [
            (b'f','Zg=='),
            (b'fo','Zm8='),
            (b'foo','Zm9v'),
            (b'foob','Zm9vYg=='),
            (b'fooba','Zm9vYmE='),
            (b'foobar','Zm9vYmFy'),
            (b'\x00\x01\x02','AAEC'),
            (b'\xFF\xEF\xFE','_-_-'),
            (b'\xDE\xAD\xBE\xEF','3q2-7w=='),
            (b'\x99\x88\x77\x66\x55\x44\x33\x22\x11','mYh3ZlVEMyIR'),
        ]
    }

    def test_base16_encode(self):
        for test,res in self.testset['base16']:
            self.assertEqual(basefamily.base_encode(test,'base16'),res)
    def test_base32_encode(self):
        for test,res in self.testset['base32']:
            self.assertEqual(basefamily.base_encode(test,'base32'),res)
    def test_base32hex_encode(self):
        for test,res in self.testset['base32hex']:
            self.assertEqual(basefamily.base_encode(test,'base32hex'),res)
    def test_base64_encode(self):
        for test,res in self.testset['base64']:
            self.assertEqual(basefamily.base_encode(test,'base64'),res)
    def test_base64urlsafe_encode(self):
        for test,res in self.testset['base64urlsafe']:
            self.assertEqual(basefamily.base_encode(test,'base64urlsafe'),res)

if __name__ == '__main__':
    unittest.main()