import jwt
import time
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


def get_token_ios(PATH, KEY_ID):
    # Load your private key from the .p8 file
    with open(PATH, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    # JWT headers
    headers = {
        "alg": "ES256",
        "kid": KEY_ID
    }
    # JWT payload
    payload = {
        "sub": "user",
        "exp": int(time.time()) + 20 * 60,  # Token expiry time, 20 minutes from now
        "aud": "appstoreconnect-v1"
    }

    # Generate the JWT
    token = jwt.encode(payload, private_key, algorithm="ES256", headers=headers)
    return token