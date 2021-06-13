import random
import file1


print("How many players want to play and it will be best of three.")
print("\nNote:The max player is 3 and min is 2.")
user = int(input("Enter the player's number:"))


if user == 2:
    user_input = input("\nEnter the Player1 name:")
    user_input2 = input("Enter the player2 name:")
    print("\n")
    game = ["Rock","Paper","Scissor"]


    game_choice = random.choice(game)
    print(user_input,":",game_choice)

    game_choice1 = random.choice(game)
    print(user_input2,":",game_choice1,"\n")

    user_input3 = input("Enter q for quite or press enter for continue playing:")
    while user_input3 != "q":
        storage = file1.run()
        print(user_input,":", storage)

        storage2 = file1.user2_run()
        print(user_input2,":", storage2)
        user_input3 = input("\nEnter q for quite or press enter for continue playing:")

    print("\nThanks for Playing!")


elif user == 3:
    name_input = input("\nEnter the Player1 name:")
    name_input1 = input("Enter the Player2 name:")
    name_input2 = input("Enter the Player3 name:")
    print("\n")

    game1 = ["Rock","Paper","Scissor"]

    selection = random.choice(game1)
    print(name_input,":",selection)

    selection1 = random.choice(game1)
    print(name_input1,":",selection1)

    selection2 = random.choice(game1)
    print(name_input2,":",selection2,"\n")

    user_input4 = input("Enter q for quite or press enter for continue playing:")
    while user_input4 != "q":
        storage0 = file1.run()
        print(name_input,":", storage0)

        storage4 = file1.user2_run()
        print(name_input1,":", storage4)

        selection4 = file1.user_3_run()
        print(name_input2,":", selection4)

        user_input4 = input("\nEnter q for quite or press enter for continue playing:")

    print("\nThanks for Playing!")
#Done
