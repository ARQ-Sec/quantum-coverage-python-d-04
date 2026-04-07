from Crypto.Cipher import DES, DES3

def execute():
    # rule_key: quantum.arq-q-0253-python
    DES.new(b"8bytekey", DES.MODE_ECB)
    DES3.new(b"Sixteen byte key", DES3.MODE_ECB)

if __name__ == '__main__':
    execute()
