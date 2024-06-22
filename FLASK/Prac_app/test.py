

def func(ip):
    li = list(ip.split(":"))

    if len(li)!=8:
        return False
    for item in li:
        if len(item)!=4:
            return False
        try:
            int(item, 16)
        except:
            return False
    return True
        

if __name__ == "__main__":
    print(func("0000:1234:1111:2222:5555:6676:0aaa"))


# print(int("fffh", 16))