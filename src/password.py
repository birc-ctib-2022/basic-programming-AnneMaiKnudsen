import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

if any([a.islower() for a in password]):
    if any([a.isupper() for a in password]):
        if any([a.isnumeric() for a in password]):
            if any([a in "$#@" for a in password]):
                if len(password) < 17 and len(password) > 5:
                    is_valid=True



# Do all the requirement checks here.

print(is_valid)
