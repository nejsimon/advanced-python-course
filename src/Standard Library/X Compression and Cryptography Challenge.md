Coding Challenge: Compression & Cryptography

This challenge will test your ability to work with Python’s built-in compression and cryptography modules.

Part 1: Compression

Write a function compress_and_decompress(data: bytes, method: str) -> bytes that:

Accepts method as one of: "gzip", "bz2", "lzma".

Compresses the given data.

Immediately decompresses it and returns the result.

Raises ValueError if the method is not supported.

Write a function file_gzip_roundtrip(filename: str, text: str) that:

Writes text into a gzip-compressed file (filename.gz).

Reads it back and prints the content.

Part 2: Hashing & HMAC

Implement a function file_checksum(filename: str, algo: str = "sha256") -> str that:

Reads a file in binary mode.

Computes its checksum using hashlib with the chosen algorithm.

Returns the hex digest.

Example:

print(file_checksum("example.txt", "sha256"))


Implement a function sign_message(message: bytes, key: bytes) -> str that:

Uses hmac with SHA256.

Returns the hex digest of the signature.

Part 3: Password Security

Write a function secure_password_hash(password: str, salt: bytes = None) -> tuple[bytes, bytes] that:

Uses hashlib.pbkdf2_hmac with SHA256 and 100,000 iterations.

If no salt is provided, generate one with os.urandom(16).

Returns (salt, derived_key).

Write another function verify_password(password: str, salt: bytes, expected: bytes) -> bool that:

Recomputes the hash with the given salt.

Returns True if it matches the expected hash.

Part 4: Secure Tokens

Implement a function generate_token(nbytes: int = 16) -> str that:

Uses secrets.token_hex(nbytes).

Returns a secure random token string.

Implement a function is_token_unique(tokens: list[str], new_token: str) -> bool that:

Returns True if new_token is not already in tokens.

Bonus Challenge

Create a script that:

Takes a filename as input.

Compresses it with all three algorithms (gzip, bz2, lzma).

Prints out the compressed file sizes and SHA256 checksums.

Determines which compression method produced the smallest file.
