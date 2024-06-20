with open("data.txt","r") as f:
    d = f.read()
    """Assalomu Alaykum
    Najot Talim O'quvchilar"""
    z = f.readline()
    "Assalomu Alaykum"
    a = f.readlines()
    # ["Assalomu Alaykum\n", "Najot Talim O'quvchilar\n"]
    print(a)