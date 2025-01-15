import hashlib
import sys


def hash_file(filename):
    """This function returns the SHA-256 hash of the file passed into it"""
    h = hashlib.sha256()

    with open(filename, "rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            h.update(chunk)

    return h.hexdigest()


def main():
    if len(sys.argv) != 3:
        print("Usage: python hashFile.py <file1> <file2>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    hash1 = hash_file(file1)
    hash2 = hash_file(file2)

    if hash1 == hash2:
        print("The files are identical.")
    else:
        print("The files are different.")


if __name__ == "__main__":
    main()
