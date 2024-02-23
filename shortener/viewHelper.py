from hashlib import blake2b
import base64


def hasher(link):
    h = blake2b(digest_size=8)

    link = link.encode("utf-8")

    h.update(link)

    hash = base64.b64encode(h.digest())
    return hash.decode("utf-8")
