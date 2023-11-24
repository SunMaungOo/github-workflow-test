import os

def main():

    tmp_value = os.getenv("TMP_VALUE")

    print("Env value of TMP_VALUE is",tmp_value)

if __name__=="__main__":
    main()