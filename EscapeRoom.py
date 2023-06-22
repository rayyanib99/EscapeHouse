# Developer: Rayyan Abdulmunib
# Description: Escape House text-based game.
# Date: 04/16/2023


# Define a function to display the game map to the player
def showMap():

    # Print game map header
    print("Game Map: ")

    # Print a series of statements to make the game map
    print("                        ---------------     east     -----------")
    print("                        | LIVING ROOM |    ----->    | GALLERY |")
    print("                        |   (Keys)    |    <-----    | (Wallet)|")
    print("                        ---------------     west     -----------")
    print("                           |  ^                      -----------")
    print("                         s |  | n                    | KITCHEN |")
    print("                         o |  | o                    |  FIRE!  |")
    print("                         u |  | r                    -----------")
    print("                         t |  | t                     s |  ^ n  ")
    print("                         h |  | h                     o |  | o  ")
    print("                           v  |                       u |  | r  ")
    print("-----------    east     ------------                  t |  | t  ")
    print("| LIBRARY |   ----->    |          |                  h v  | h  ")
    print("| (Phone) |   <-----    |   HALL   |      east       -----------")
    print("-----------    west     | No Item. |     ----->      | STORAGE |")
    print("                        |          |     <-----      | (Shoes) |")
    print("                        ------------      west       -----------")
    print("                         s |  ^ n                               ")
    print("                         o |  | o                               ")
    print("                         u |  | r                               ")
    print("                         t |  | t                               ")
    print("                         h v  | h                               ")
    print("                       -------------      east      ----------- ")
    print("                       |  BEDROOM  |     ----->     |  GARAGE | ")
    print("                       | (Clothes) |     <-----     |   (Car) | ")
    print("                       -------------      west      ----------- ")

# Define a function to display instructions of the game to the player
def showInstructions():

    # Print a series of introductory messages to the player with instructions
    print("Welcome to the Escape House Game")
    print("Collect the 6 items needed to escape the house before the house burns down or burn in the fire.")
    print("Move command: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")

    # Print dotted line
    print("----------------------")

# Define a function to print the player's status by based on their current room, inventory list, and rooms dictionary
def showStatus(currentRoom, inventory, rooms):

    # Print current status of player
    print("You are in the", currentRoom)

    # Print the current inventory
    print("Inventory:", inventory)

    # If the current room is the starting room or the Hall
    if currentRoom == "Hall":

        # Display there is nothing to collect message
        print("There is nothing in this room to collect.")

    # If the current room is the Kitchen with the fire
    elif currentRoom == "Kitchen":

        # Display you walked into the fire message
        print("You walked into the fire.")

    # If the item in the current room is already in the inventory
    elif rooms[currentRoom]["item"] in inventory:

        # Print empty/blank line
        print()

    # Otherwise
    else:

        # Display the nearby item in the room
        print("You see your", rooms[currentRoom]["item"])

    # Print dotted line
    print("----------------------")

# Main
if __name__ == '__main__':

    # Initialize the starting room to the Hall
    current_room = "Hall"

    # Initialize inventory list to store the items collected by the player
    inventory = []

    # The dictionary links a room to other rooms
    rooms = {"Hall" : {"North" : "Living Room", "South" : "Bedroom", "East" : "Storage", "West" : "Library", "item" : ""},
             "Living Room" : {"East" : "Gallery", "South" : "Hall", "item" : "Keys"},
             "Gallery": {"West" : "Living Room", "item" : "Wallet"},
             "Library" : {"East" : "Hall", "item" : "Phone"},
             "Storage" : {"North" : "Kitchen", "West" : "Hall", "item" : "Shoes"},
             "Bedroom" : {"North" : "Hall", "East" : "Garage", "item" : "Clothes"},
             "Garage" : {"West" : "Bedroom", "item" : "Car"},
             "Kitchen" : {"South" : "Storage"}}

    # Call the showMap function to display the game map to the player
    showMap()

    # Call the showInstructions function to display the instructions to the player
    showInstructions()

    # Call the showStatus function to show the player his current status in the game
    showStatus(current_room, inventory, rooms)

    # Loop until true
    while (True):

        # If the player enters the room with the fire (Kitchen)
        if current_room == "Kitchen":

            # Display losing message
            print("UH OH... GAME OVER!")
            print("Thanks for playing. Goodbye.")
            break

        # If the player collects all 6 items needed to escape the burning house
        elif len(inventory) == 6:

            # Display winning message
            print("Congratulations! You have collected all the items and escaped the burning house!")
            print("Thanks for playing. Hope you enjoyed it.")
            break

        # Prompt the player to enter their next move
        player_input = input("Enter your move or enter 'Exit' to quit: ")

        # Split the player's input into two words
        next_move = player_input.split(' ')

        # Store the first word from the input into action
        action = next_move[0].title()

        # If the player's input is "go" and has more than 1 word
        if (action.upper() == "GO" and len(next_move) > 1):

            # If the player's entry following "go" is a valid direction
            if (next_move[1].title() == "North" or next_move[1].title() == "East" or next_move[1].title() == "South" or next_move[1].title() == "West"):

                # Store the second word onwards in direction with first letter capitalized
                direction = next_move[1].title()

                # Change the current room to the room the player wants to move in
                current_room = rooms[current_room][direction]

                # Call the showMap function to display the game map to the player
                showMap()

                # Display the player's current status by calling the showStatus function
                showStatus(current_room, inventory, rooms)

            # Otherwise, if the player's entry following "go" is not an invalid direction
            else:
                # Print error message
                print("That is not a valid direction. Please try again.")

                # Call the showMap function to display the game map to the player
                showMap()

                # Call the showInstructions function to display the instructions to the player
                showInstructions()

        # If the player's input is "get" and has more than 1 word
        elif (action.upper() == "GET" and len(next_move) > 1):

            # If the player's entry following "get" is a valid item
            if (next_move[1].title() in rooms[current_room]["item"]):

                # Store the second word onwards in direction with first letter capitalized
                item = next_move[1].title()

                # If the item that the player wants to get is in the room
                if item == rooms[current_room]["item"]:

                    # If the item in the room is not in the inventory
                    if item not in inventory:

                        # Add the item to the inventory
                        inventory.append(rooms[current_room]["item"])

                        # Print a message that shows the player the item has been collected from the room
                        print(rooms[current_room]["item"], "has been collected.")

                        # Call the showMap function to display the game map to the player
                        showMap()

                        # Display the player's current status by calling the showStatus function
                        showStatus(current_room, inventory, rooms)

                    # Otherwise, if the item is in the inventory already
                    else:

                        # Print a message that says the item already exists
                        print(rooms[current_room]["item"], "is already in inventory.")

            # Otherwise, if the player's entry after "get" is not the item in the room
            else:

                # Print error message
                print("Item is not here. Please try again.")

                # Call the showMap function to display the game map to the player
                showMap()

                # Call the showInstructions function to display the instructions to the player
                showInstructions()

        # If the player wants to quit and enter 'Exit'
        elif (action.upper() == "EXIT"):

            # Print farewell message and break out of the loop
            print("Sorry to see you go. Goodbye!")
            break

        # Otherwise
        else:

            # Data Validation: print error message
            print("Invalid command. Please enter a valid command.")

            # Call the showMap function to display the game map to the player
            showMap()

            # Call the showInstructions function to display the instructions to the player
            showInstructions()

