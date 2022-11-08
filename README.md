![Python build & test](https://github.com/software-students-fall2022/python-package-exercise-project-3-team-11/actions/workflows/build.yaml/badge.svg)

# Password Manager Package
A little exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.


## Team
- Victoria Zhang: [Github](https://github.com/Ruixi-Zhang)
- Jenny Shen: [Github](https://github.com/JennyShen10792)
- Tiffany Lee: [Github](https://github.com/les5185)
- Seok Tae Kim: [Github](https://github.com/)
- Khalifa AlFalasi: [Github](https://github.com/)

## Functions
### Validate Password

### Generate Password
- The `generate_password` function can generate a random password within length 6 to 15. The password is guarantee meet the requirement above.
- Generate a password given a length. Note: if the length is greater than 15 or lower than 6. It will generate a random password  within the 6 and 15 range.
    ```python
    from passwordManager import generator
    password = generator.generate_password(10)
    ```
- Generate a password without specifying length. Will generate a password with random length within 6 and 15 range.
    ```python
    from passwordManager import generator
    password = generator.generate_password()
    ```
### Encode Password

### Decode Password
- The `decode_password` function can decrypt an encrypted password that is created by the `encode_password` function. 
- Function takes in a string type and will raise error if unmatched types are give.
- Function will also raise error if the value in the string either does not match encryption format, or if any of the character is not in the decimal range of 33 to 126. 
- Function returns a decoded string.
    ```python
    from passwordManager import decoder, encrypt
    encrypted_password = encrypt.encode_password('hello')
    decoded_password= decoder.decode_password(encrypted_password)
    #decoded_password is 'hello'
    ```
### Check Password 