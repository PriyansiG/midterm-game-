# Project Title: Text-Based Adventure Game - Cave Adventure
# Author: Priyansi Govani 
# Summary: A simple text-based adventure game where the player navigates through =a mysterious cave, making decisions that lead to one of 8 possible endings.


#Initialisation of the game. The first choices given to the user would be to go either 'left' or 'right'.
def cave_adventure():
    #Printing instructions
    print("You wake up to find yourself in a cold, dark cave. The air is damp, and the faint echo of dripping water fills your ears.")
    print("You have no memory of how you got here. As you get up and dust yourself off, you notice two paths ahead:")
    print("1. To your left, a narrow tunnel leads deeper into darkness. The air is colder there, and you can faintly hear the sound of rushing water.")
    print("2. To your right, a wider passage seems to have some light coming from it. The source of the light is unclear, but you hear distant whispers echoing from within.")
    
    first_choice = input("Do you go left into the darkness (left) or right toward the light (right)? ").lower()#generalises input to lowercase letters
    
    if first_choice == "left":
        narrow_tunnel()
    elif first_choice == "right":
        wide_passage()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
        cave_adventure()  # Restart if input is invalid

#This leads to the second option choice when you enter 'left'
def narrow_tunnel():
    #Printing instructions
    print("\nYou decide to brave the narrow, dark tunnel, following the sound of rushing water.")
    print("The air becomes colder as you move deeper. Suddenly, the ground beneath you starts to crumble!")
    print("1. You can try to jump forward (jump).")
    print("2. You can attempt to climb back to safety (climb).")
    
    choice = input("Do you jump or climb? ").lower()#generalises input to lowercase letters
    
    #This represents the further output via the input, depicting the case scenarios
    if choice == "jump":
        jump_forward()
    elif choice == "climb":
        climb_back()
    else:
        print("Invalid choice. Please choose 'jump' or 'climb'.")
        narrow_tunnel()

#This leads to the second option choice when you enter 'right'
def wide_passage():
    #Printing instructions
    print("\nYou choose to investigate the wider passage, drawn by the mysterious light and whispers.")
    print("The light grows brighter, but so do the whispers. They now sound like a chant. You see a glowing object in the distance.")
    print("1. Approach the glowing object (approach).")
    print("2. Ignore the object and continue down the passage (ignore).")
    
    choice = input("Do you approach or ignore the object? ").lower()#generalises input to lowercase letters
    
    #This represents the further output via the input, depicting the case scenarios
    if choice == "approach":
        glowing_object()
    elif choice == "ignore":
        continue_passage()
    else:
        print("Invalid choice. Please choose 'approach' or 'ignore'.")
        wide_passage()


def jump_forward():
    #Printing instructions
    print("\nYou leap forward just in time, landing on solid ground.")
    print("But the tunnel has now split into two.")
    print("1. Take the path with more light (light).")
    print("2. Follow the path that leads deeper into darkness (darkness).")
    
    choice = input("Which path do you take, light or darkness? ").lower()#generalises input to lowercase letters
    
    #This represents the further output via the input, depicting the case scenarios
    if choice == "light":
        print("\nYou follow the light and emerge safely from the cave. You survived!")
        print("Ending 1: Escape to safety.")
    elif choice == "darkness":
        print("\nYou wander into the darkness, never to be seen again.")
        print("Ending 2: Lost in the depths.")
    else:
        print("Invalid choice. Please choose 'light' or 'darkness'.")
        jump_forward()


def climb_back():
    #Printing instructions
    print("\nYou try to climb back, but the crumbling rock gives way!")
    print("You fall into a deep underground river and are swept away.")
    print("1. Try to swim to shore (swim).")
    print("2. Let the current take you (float).")
    
    choice = input("Do you swim or float? ").lower()#generalises input to lowercase letters
    
    #This represents the further output via the input, depicting the case scenarios
    if choice == "swim":
        print("\nYou swim with all your strength and make it to a small cave. You're safe... for now.")
        print("Ending 3: Safe in a hidden cave.")
    elif choice == "float":
        print("\nYou let the current take you deeper into the underground. Eventually, you wash up on a shore... and find treasure!")
        print("Ending 4: Treasure found.")
    else:
        print("Invalid choice. Please choose 'swim' or 'float'.")
        climb_back()


def glowing_object():
    #Printing instructions
    print("\nYou approach the glowing object. It's a mystical crystal.")
    print("1. Touch the crystal (touch).")
    print("2. Leave it and walk away (leave).")
    
    choice = input("Do you touch or leave the crystal? ").lower()#generalises input to lowercase letters
    
    #This represents the further output via the input, depicting the case scenarios
    if choice == "touch":
        print("\nYou touch the crystal and are suddenly transported to another world. You're trapped forever in a strange realm.")
        print("Ending 5: Trapped in another dimension.")
    elif choice == "leave":
        print("\nYou wisely decide to leave the crystal alone and continue your journey. You find the cave's exit and escape.")
        print("Ending 6: Escaped, avoiding danger.")
    else:
        print("Invalid choice. Please choose 'touch' or 'leave'.")
        glowing_object()


def continue_passage():
    #Printing instructions
    print("\nYou ignore the glowing object and continue down the passage.")
    print("The whispers grow louder, and you start to feel dizzy.")
    print("1. Sit down to rest (rest).")
    print("2. Push forward despite the dizziness (push).")
    
    choice = input("Do you rest or push forward? ").lower()#generalises input to lowercase letters
    
    #This represents the further output via the input, depicting the case scenarios
    if choice == "rest":
        print("\nYou sit down, but the dizziness worsens. You lose consciousness, never to wake up again.")
        print("Ending 7: Lost to the cave's magic.")
    elif choice == "push":
        print("\nYou push forward, fighting the dizziness. You finally reach the end of the passage and escape.")
        print("Ending 8: Escaped through determination.")
    else:
        print("Invalid choice. Please choose 'rest' or 'push'.")
        continue_passage()

# Start the game
cave_adventure()