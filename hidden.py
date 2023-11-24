import os

def main():
    print(f"Env value of TMP_VALUE is {os.environ['TMP_VALUE']}")

if __name__=="__main__":
    main()