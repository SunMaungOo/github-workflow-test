import os

def main():
    print("Everything work out correctly")
    print(f"Env value of AGE is {os.environ["AGE"]}")


if __name__=="__main__":
    main()