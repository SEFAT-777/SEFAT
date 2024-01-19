import platform
b = platform.__main__()[0]
if b == '64bit':
    import SEFAT
elif b == '32bit':
    print("32bit Not Supported! Sorry")
