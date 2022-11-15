# TextBytesEncoder
Module encoding and encrypting text by key
## Usage example
```python
from textbytesencoder import Encoder

encoder = Encoder(key=None, save_key=False)  # key: Optional[bytes] = None, save_key: Optional[bool] = False
print(encoder.encrypt(text))  # type(text) == str
print(encoder.decrypt(text))  # type(text) == bytes
```
During initialization, you can specify the optional `key` parameter (key, type and purpose see below) and the optional `save_key` parameter (saves the key to a separate file)
## Parameters
Parameter `key` of type bytes, generated using the `Fernet.generate_key()` function 
or using the `base64.urlsafe_b64encode(os.urandom(32))` function used to encode or decode text.
```python
print(encoder.key)
```

```python
encoder.key = b"key"  # key = Fernet.generate_key() or base64.urlsafe_b64encode(os.urandom(32))
```