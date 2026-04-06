import nacl.public
import nacl.signing

def execute():
    # rule_key: quantum.arq-q-0398-python
    nacl.signing.SigningKey.generate()
    nacl.public.PrivateKey.generate()

if __name__ == '__main__':
    execute()
