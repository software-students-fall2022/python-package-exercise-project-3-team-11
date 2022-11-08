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

### Check Password 