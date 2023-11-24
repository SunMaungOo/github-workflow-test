import os

def main():
    print(f"Env value of HIDDEN_VALUE is {os.environ['HIDDEN_VALUE']}")

if __name__=="__main__":
    main()