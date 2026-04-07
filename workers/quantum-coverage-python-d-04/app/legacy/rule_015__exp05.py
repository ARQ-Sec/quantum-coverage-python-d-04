from cryptography.hazmat.primitives.asymmetric import x25519

def execute():
    # rule_key: quantum.arq-q-0310-python
    private_key: x25519.X25519PrivateKey = x25519.X25519PrivateKey.generate()
    public_key: x25519.X25519PublicKey = private_key.public_key()

if __name__ == '__main__':
    execute()
