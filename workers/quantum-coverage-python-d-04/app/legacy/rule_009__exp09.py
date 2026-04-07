import rsa

def execute():
    # rule_key: quantum.arq-q-0396-python
    pub, priv = rsa.newkeys(2048)
    rsa.encrypt(b"coverage", pub)

if __name__ == '__main__':
    execute()
