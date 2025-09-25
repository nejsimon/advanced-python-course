Standard Library: Compression & Cryptography

Python’s standard library provides robust tools for handling data compression and cryptographic operations. While not replacements for specialized third-party libraries (e.g., cryptography, PyNaCl, or PyJWT), these modules are useful for common tasks such as working with compressed files, hashing, and securely storing passwords.

Compression Modules
zlib

Provides access to the zlib compression library (DEFLATE).

Useful for compressing data in memory or working with .gz files.

Functions:

zlib.compress(data, level=9)

zlib.decompress(data)

zlib.crc32(data) – compute CRC checksums.

import zlib

data = b"hello world" * 10
compressed = zlib.compress(data)
decompressed = zlib.decompress(compressed)
print(len(data), "->", len(compressed))

gzip

Read and write .gz files.

Works like open(), but for gzip compression.

import gzip

with gzip.open("example.txt.gz", "wt") as f:
    f.write("Compressed text!")

with gzip.open("example.txt.gz", "rt") as f:
    print(f.read())

bz2

Support for the bzip2 compression algorithm.

Typically better compression ratio than gzip, but slower.

import bz2

compressed = bz2.compress(b"some large data here")
print(bz2.decompress(compressed))

lzma

Provides xz/LZMA compression.

Very high compression ratio, slower than gzip/bz2.

Good for archival purposes.

import lzma

data = b"A" * 1000
compressed = lzma.compress(data)
print(len(compressed))

Cryptographic Hashing
hashlib

Provides access to common secure hash functions:

md5, sha1, sha256, sha512, etc.

Used for checksums, signatures, and secure storage (though avoid MD5/SHA1 for security).

import hashlib

h = hashlib.sha256(b"secret message")
print(h.hexdigest())

hmac

Implements keyed-hashing for message authentication.

Ensures data integrity and authenticity.

Often used in API authentication.

import hmac
import hashlib

key = b"supersecret"
msg = b"hello"
signature = hmac.new(key, msg, hashlib.sha256).hexdigest()
print(signature)

Password Security
hashlib.pbkdf2_hmac

Built-in password hashing function.

Uses a secure key-derivation algorithm (PBKDF2).

Safer than storing plain hashes.

import hashlib
import os

password = b"mypassword"
salt = os.urandom(16)
dk = hashlib.pbkdf2_hmac("sha256", password, salt, 100000)
print(dk.hex())

Randomness & Secrets
secrets

Provides cryptographically secure random values.

Use for passwords, tokens, and cryptographic keys.

Prefer this over random for security.

import secrets

token = secrets.token_hex(16)  # 32-character hex string
print(token)

When to Use Standard Library vs Third-Party

✅ Use standard library for:

Checksums (CRC32, SHA256)

Basic compression tasks

Simple secure token generation

🚫 Avoid using only stdlib for:

Encryption/decryption (AES, RSA, etc.)

Full TLS/SSL handling (use ssl or third-party)

Password storage in production (consider argon2 or bcrypt)

Summary

Compression: zlib, gzip, bz2, lzma

Hashes: hashlib, hmac

Password hashing: pbkdf2_hmac

Security tokens: secrets

The standard library gives you strong primitives for many common security and compression needs, but for advanced cryptography and production-grade security, rely on specialized libraries.