import hashlib
import os

import pyaes  # Biblioteca para criptografia simétrica


def verify_hash(encrypted_file, hash_file):
    # Calcular o hash do arquivo criptografado
    with open(encrypted_file, "rb") as f:
        file_data = f.read()
        file_hash = hashlib.sha256(file_data).hexdigest()

    # Ler o hash armazenado no arquivo hash_code.txt
    with open(hash_file, "r") as f:
        stored_hash = f.read().strip()

    # Comparar os hashes
    return file_hash == stored_hash


def decrypt_file(file_name):
    # Verificar se o hash do arquivo criptografado é igual ao hash armazenado
    if verify_hash("teste.txt.ransomwaretroll", "hash_code.txt"):
        ## abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()
        # Chave para descriptografia
        key = b"testeransomwares"
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        # Criar o arquivo descriptografado
        with open("teste.txt", "wb") as new_file:
            new_file.write(decrypt_data)
        return "O arquivo foi descriptografado com sucesso!."
    else:
        return "Os hashes são diferentes. O arquivo não será descriptografado."


if __name__ == "__main__":
    print(decrypt_file("teste.txt.ransomwaretroll"))
