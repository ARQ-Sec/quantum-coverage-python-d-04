from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF, HKDFExpand
from cryptography.hazmat.primitives.asymmetric import x25519
import oqs

def execute():
    # rule_key: quantum.arq-q-0350-python
    oqs.KeyEncapsulation("ML-KEM-768")
    x25519.X25519PrivateKey.generate()
    HKDF(algorithm=hashes.SHA256(), length=32, salt=None, info=b"hybrid")

if __name__ == '__main__':
    execute()
