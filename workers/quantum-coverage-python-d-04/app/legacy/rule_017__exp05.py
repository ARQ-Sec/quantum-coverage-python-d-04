from cryptography.hazmat.primitives.asymmetric import ed25519, x25519

def execute():
    # rule_key: quantum.arq-q-0336-python
    x25519.X25519PrivateKey.generate()
    ed25519.Ed25519PrivateKey.generate()

if __name__ == '__main__':
    execute()
