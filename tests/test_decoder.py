import pytest
from passwordManagerByAscii import decoder

class Tests:
    def test_chracter_out_of_range(self):
        for i in range(32):
            input= chr(i)
            with pytest.raises(Exception):
                decoder.decode_password(input)
                
    def test_input_type(self):
        with pytest.raises(Exception):
            decoder.decode_password(123)
        with pytest.raises(Exception):
            decoder.decode_password(0.1)
        with pytest.raises(Exception):
            decoder.decode_password(None)

    def test_input_size(self):
        with pytest.raises(Exception):
            decoder.decode_password('B')
        with pytest.raises(Exception):
            decoder.decode_password('BD')
        decrypted= decoder.decode_password('BDG')
        assert decrypted=='A'

    def test_decrypt_decimal_126(self):
        decrypted = decoder.decode_password("\"$'")
        assert decrypted == '~'

    def test_incorrect_encryption(self):
        with pytest.raises(Exception):
            decoder.decode_password('notencrypted')