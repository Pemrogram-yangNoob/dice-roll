import random
import os

#dice roll function,where i put the dice result to be called later
#function dice roll,di function ini aku taruh hasil dadu nya untuk dipanggil nanti

##this one is for the D6 dice(dice with six side)
##function yang ini buat dau D6(dadu 6 sisi)
def dice_roll():
    number = random.randint(1, 6)
    if number == 1:
        print("|‾‾‾‾‾‾‾‾‾‾‾|")
        print("|           |")
        print("|     0     |")
        print("|           |")
        print("|___________|")
    if number == 2:
        print("|‾‾‾‾‾‾‾‾‾‾|")
        print("|          |")
        print("|  0    0  |")
        print("|          |")
        print("|__________|")
    if number == 3:
        print("|‾‾‾‾‾‾‾‾‾‾‾|")
        print("|           |")
        print("|   0 0 0   |")
        print("|           |")
        print("|___________|")
    if number == 4:
        print("|‾‾‾‾‾‾‾‾‾‾|")
        print("|  0    0  |")
        print("|          |")
        print("|  0    0  |")
        print("|__________|")
    if number == 5:
        print("|‾‾‾‾‾‾‾‾‾‾‾|")
        print("|  0     0  |")
        print("|     0     |")
        print("|  0     0  |")
        print("|___________|")
    if number == 6:
        print("|‾‾‾‾‾‾‾‾‾‾|")
        print("|  0    0  |")
        print("|  0    0  |")
        print("|  0    0  |")
        print("|__________|")


##and this one is for the d20 dice(dice with 20 side,usually used in dnd"idk tho")
##dan yang ini buat dadu D20(dadu dengan 20 sisi,biasa dipake di permainan dnd"gatau deng")
def dnd_dice():
    number = random.randint(1, 20)
    if number == 1:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  01  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")
    
    elif number == 2: 
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  02  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 3:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  03  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 4:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  04  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 5:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  05  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")
       
    elif number == 6:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  06  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 7:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  07  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 8:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  08  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 9:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  09  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 10:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  10  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 11:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  11  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 12:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  12  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 13:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  13  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 14:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  14  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 15:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  15  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 16:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  16  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 17:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  17  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 18:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  18  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 19:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  19  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")

    elif number == 20:
        print("          //||\\\\    ")
        print("       ///  ||  \\\\\\   ")
        print("     //     ||     \\\\ ")
        print("  / /       ||       \\ \\")
        print(" /          ||          \\")
        print("|‾‾‾‾‾‾‾‾‾‾‾/\\‾‾‾‾‾‾‾‾‾‾‾|")
        print("|          /  \\          |")
        print("|\\        /    \\        /|")
        print("| \\      /  20  \\      / |")
        print("|  \\    /        \\    /  |")
        print(" |  \\  /__________\\__/  | ")
        print("  | /‾‾\\          /  \\ | ")
        print("  |/    \\        /    \\| ")
        print("   \\     \\      /     /  ")
        print("     \\    \\    /    /    ")
        print("       \\   \\  /   /      ")
        print("         \\__\\/__/        ")
    
    
# this is the main function,when the program start,this is the first thing that run
# ini adalah function utama,pas program nya mulai,ini yang bakal muncul pertama
def main():

    #the variabel current_option is used to save the information about the current choice that user mad
    #variabel current_option digunakan untuk menyimpan informasi tentang pilihan user saat ini
    current_option = None

    #code for user to make choice
    #code buat user milih
    while True:
        print("1. D6")
        print("2. D20")
        print("3. Clear The Screen")
        print("4. Exit Program")
        user_choice = input("Choose Action: ")
        
        if user_choice == "1":
            #"if current_option != 1" is to check if the previous action choosed is 1 or not and if not it will run clear_screen function so it clear the terminal so the d6 and d20 doesnt mix 
            #"if current_option != 1" digunain buat ngecheck apakah pilihan sebelumnya 1 atau bukan jika bukan maka akan jalanin function clear_screen buat bersihin terminal supaya d6 dan d20 ga nyampur
            if current_option != "1":
                clear_screen()
            #run dice roll function
            #jalanin function dice roll
            dice_roll()
            current_option = "1"

        elif user_choice == "2":
            if current_option != "2":
                clear_screen()
            dnd_dice()
            current_option = "2"

        #run the clear_screen function manually through choosing option
        #jalanin function clear_screen secara manual lewat milih opsi
        elif user_choice == "3":
            clear_screen()

        #to exit the program
        #buat keluar dari program
        elif user_choice == "4":
            break
        
        #if the user input isnt 1/2/3/4 then this invalid input will pop up
        #kalau user input bukan 1/2/3/4 tulisan invalid input bakal keluar
        else:
            print("Invalid Input")


## function for clearing terminal
##function buat bersihin terminal
def clear_screen():
    os.system('cls')
    

#to make the main function run first when the code start
#ngebuat function main jalan pertama waktu code nya mulai  
if __name__ == "__main__":
    main()


            



    
   
