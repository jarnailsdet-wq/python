#Api error
while True:
    num = int(input("Enter code: "))

    match num:
        case 404:
            print("Bad request")
        case 401:
            print("unauthorized")
        case 500:
            print("internal error")
        case _:
            print("unknown error")
            break


