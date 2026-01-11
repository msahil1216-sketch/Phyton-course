def shutdown():
    user_input = input("Shutdown? (Yes/No): ")

    if user_input == "Yes":
        print("Shutting down")
    elif user_input == "No":
        print("Abort Shut down")
    else:
        print("Sorry, your input is invalid")
        print("Please reconsider your input from the options (Yes/No)")

shutdown()