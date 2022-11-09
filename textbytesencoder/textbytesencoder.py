# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2022-present D1ffic00lt

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import base64

from cryptography.fernet import Fernet


class Encoder(object):
    """
    Module encoding and encrypting text by key

    .. versionadded:: 1.0.0

    Attributes
    ----------
    :param key: :class:`bytes`
        key generated by the cryptography.fernet module used for encoding
        and decoding by the encrypt and decrypt functions
    :param save_key: :class:`bool`
        parameter, if the parameter is true,
        then the program will save the key to a separate file

    Methods
    -------
    encrypt(text: str = None) -> bytes
        encodes text (type str) to type bytes (using key encryption)
    decrypt(text: bytes = None) -> str
        decodes the result of the encrypt function by key
    """
    __slots__ = ("_key", "_file")

    def __init__(self, key: bytes = None, save_key: bool = False) -> None:
        """

        Parameters
        ----------
        :param key: :class:`bytes`
            key generated by the cryptography.fernet module used for encoding
            and decoding by the encrypt and decrypt functions
        :param save_key: :class:`bool`
            parameter, if the parameter is true,
            then the program will save the key to a separate file

        Raises
        -------
        :exc:`.TypeError`
            invalid token used to encode or decode text
        """
        self._key = Fernet.generate_key() if key is None else key
        if save_key:
            with open("key.dpcb", "+wb") as self._file:
                self._file.write(self._key)

    def encrypt(self, text: str = None) -> bytes:
        """
        А function that encodes text into bytes by key

        Parameters
        ----------
        :param text: :class:`str`
            the text to be encoded with the key

        Returns
        -------
        :class: `bytes`
            returns an object of type bytes encoded with
            the key and the cryptography.fernet.Fernet module

        Raises
        -------
        :exc:`cryptography.fernet.InvalidToken`
            invalid token used to encode or decode text
        """
        return Fernet(self._key).encrypt(self.__to_base64(text))

    def decrypt(self, text: bytes = None) -> str:
        """
        Function, bytes to text by key

        Parameters
        ----------
        :param text: :class:`bytes`
            the text to be decoded with the key

        Returns
        -------
        :class: `str`
            returns an object of type str, decorated with a
            key and a cryptography.fernet.Fernet module

        Raises
        -------
        :exc:`cryptography.fernet.InvalidToken`
            invalid token used to encode or decode text
        """
        return self.__from_base64(Fernet(self._key).decrypt(text))

    @property
    def key(self) -> bytes:
        return self._key

    @key.setter
    def key(self, value: str) -> None:
        self._key = value.encode()

    @staticmethod
    def __to_base64(text: str) -> bytes:
        return base64.b64encode(bytes(text, 'utf-8'))

    @staticmethod
    def __from_base64(text: bytes) -> str:
        return base64.b64decode(text).decode()

    def __repr__(self):
        attrs = [
            ('key', self.key)
        ]
        return '%s(%s)' % (self.__class__.__name__, ' '.join('%s=%r' % t for t in attrs))

    def __str__(self):
        return f'Encoder with key {self._key}'

    def __call__(self, *args, **kwargs):
        return self._key

    def __new__(cls, *args, **kwargs):
        return object.__new__(Encoder)

    def __hash__(self):
        return hash(self.key)


if __name__ == "__main__":
    _save_key = None
    _key = input("Enter key : ") if input("Do you already have a generated key? (Y/N) : ").lower() == "y" else None

    if _key is not None:
        if (_key[:2] == "b'" and _key[-1] == "'") or (_key[:2] == "b'" and _key[-1] == '"'):
            _key = _key[2:-1].encode()
        else:
            _key = _key.encode()
    else:
        _save_key = True if input("Save key? (Y/N) : ").lower() == "y" else False

    _model = Encoder(key=_key, save_key=_save_key)

    if input("Encode or decode a message? (E/D) : ").lower() == "e":
        _save_text = True if input("Save encoded text? (Y/N) : ").lower() == "y" else False
        _text = _model.encrypt(input("Enter text : "))
        if _save_text:
            with open("encoded_text.txt", "+wb") as _file:
                _file.write(_text)
        print(_text)
    else:
        _save_text = True if input("Save decoded text? (Y/N) : ").lower() == "y" else False
        _text = input("Enter text : ")
        if (_text[:2] == "b'" and _text[-1] == "'") or (_text[:2] == "b'" and _text[-1] == '"'):
            _text = _text[2:-1].encode()
        else:
            _text = _text.encode()
        _text = _model.decrypt(_text)
        if _save_text:
            with open("encoded_text.txt", "+w") as _file:
                _file.write(_text)
