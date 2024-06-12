import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(help="Enter a filename", dest="fname", type=str)
    parser.add_argument(help="Enter an integar value", dest="myint", type=int)
    parser.add_argument(help="Enter a float value", dest="myfloat", type=float)

    cliarg = parser.parse_args()

    fname = cliarg.fname
    myint = cliarg.myint
    myfloat = cliarg.myfloat

    print(myint * myfloat)

    myfile = open(fname, "w")

    myfile.write(str(myint * myfloat))



main()