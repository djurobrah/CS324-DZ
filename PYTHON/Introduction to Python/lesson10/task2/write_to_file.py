zoo = ['lion', "elephant", 'monkey']

if __name__ == "__main__":
    f = open("output.txt", "a")

    for i in zoo:
        f.write(f.readlines()[i])

    f.close()
