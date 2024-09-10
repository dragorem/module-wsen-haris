import eins

print("Top-level in zwei.py")

eins.func()

if __name__ == "__main__":
    print("zwei.py wurde direkt ausgefuehrt")
else:
    print("zwei.py wurde importiert und dabei ausgefuehrt")
