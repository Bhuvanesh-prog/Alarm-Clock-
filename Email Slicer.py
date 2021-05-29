email = input("Enter your email:").strip()
username = email[:email.index("bhuvanesh1320@gmail.com")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your user name is '{username}'and your domain is '{domain_name}'")
print(format)
