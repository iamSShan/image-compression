import sys
import img_manipulation

def validator():
    """
    Validates user input when the program starts running
    User can chose between 1 and 2, or he can either quit.
    """
    for i in range(1, 1000000):
        inp = input("Enter now: ")
        if inp == '1' or inp == '2':
            break;
        elif inp == '3':
            sys.exit()
        else:
            print("Wrong input. Try again\n")
            continue;
    return inp

if __name__ == "__main__":
    location_img = "input/422kbimg.jpg"
    print("*** \nEnter 1 to losslessly compress the image ***\n")
    print("Or\n")
    print("*** Enter 2 for decreasing the dimensions of the image ***\n")
    print("Or\n")
    print("*** Enter 3 to quit ***\n\n")
    inp =  validator()
    if inp ==  '2':
        img_manipulation.handle_decrement(location_img)
    elif inp == '1':
        img_manipulation.start_optimization(location_img)
