with open("dosya.txt", "r") as f:
    lines = f.readlines()
    for item in lines:
        print(item.strip())