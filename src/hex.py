import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]


match command:
    case "encode":
    y=[]
    for i in range(len(x)):
        n=hex(ord(x[i]))
        y.append(n)
        encoding = "".join(y)
    print(encoding)

    case "decode":
        number=encoding.split("0x")
        l=[]
        for i in range(len(number)):
            m=chr(int(i, base=16))
        decoding = " ".join(x)
        print(decoding)
