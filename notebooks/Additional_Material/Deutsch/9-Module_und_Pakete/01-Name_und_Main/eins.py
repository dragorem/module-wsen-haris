def func():
    """ Beispielfunktion Modulimport """

    print("func() lief in eins.py")

print("Top-level print innerhalb von eins.py")

if __name__ == "__main__":
    print("eins.py wurde direkt ausgefuehrt")
else:
    print("eins.py wurde importiert und dabei ausgefuehrt")
