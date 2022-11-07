def update_password(uname, password):
        
        while True:
            current_user_name = input("Please enter your current username: ")
            current_password = input("Please enter your current password: ")
            
            if current_user_name != uname or current_password != password:
                print("Invalid username or password.")
                continue
            
            while True:
                new_pass = input("Please enter your new password: ")
                
                if validate_password(new_pass) == False:
                    print("Password must have at least 1 capital, 1 number, 1 special character and 6 characters. Please try again.")
                    continue
                else:
                    while True:
                        confirm_new_pass = input("Re-enter the new password: ")
                        if confirm_new_pass != new_pass:
                            print("The passwords do not match, please try again.")
                            continue
                        else:
                            password = new_pass
                            print("Password updated successfully!")
                            break
                
                break

        return password


