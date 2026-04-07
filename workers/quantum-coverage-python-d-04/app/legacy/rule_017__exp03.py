from cryptography.fernet import Fernet

def execute():
    # rule_key: quantum.arq-q-0289-python
    Fernet.generate_key()

if __name__ == '__main__':
    execute()
