def main():
    try:
        a=int(input("enter a number:"))
        print(a)

    except Exception as e:
        print(e)
        return


    finally:
        print("hey i am inside of fially")

main()