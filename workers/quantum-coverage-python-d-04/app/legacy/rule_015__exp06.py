from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF, HKDFExpand

def execute():
    # rule_key: quantum.arq-q-0315-python
    HKDFExpand(algorithm=hashes.SHA256(), length=32, info=b"coverage")

if __name__ == '__main__':
    execute()
