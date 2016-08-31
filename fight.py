from gladiator import Gladiator
import random
import os
import sys
import webbrowser


def main():
    max1 = random.randint(16, 25)
    min1 = random.randint(5, 15)
    max2 = random.randint(16, 25)
    min2 = random.randint(5, 15)

    print("""              ______
                       .-"      "-.
                      /            \\
                     |              |
                     |,  .-.  .-.  ,|
                     | )(__/  \__)( |
                     |/     /\     \|
           (@_       (_     ^^     _)
      _     ) \_______\__|IIIIII|__/__________________________
     (_)@8@8{}<________|-\IIIIII/-|___________________________>
            )_/        \          /
           (@           `--------` jgs



                  .-.
                  | |____________________________________________________
     _ _ _ _ _ _ _| |                                                  .'`.
    |_|_|_|_|_|_|_| |-mbfh-------------------------------------------.'****>
    `.            | |_______________________________________________.'***.'
      `.        .'| |                                               `**'
        `-.___.'  `-'                                              .'*`.
                                                                   `._.' .
                                                                   .   .'*`.
                                                                 .'*`. `._.'


         """)
    print("Choose your Gladiator!!!")
    print("Gladiator 1:  Perseus, HP 100, rage: 0;" + " " + "min damage: " +
          str(min1) + " " + "max damage: " + str(max1))
    print("Gladiator 2:  Spartacus, HP 100, rage: 0;" + " " + "min damage: " +
          str(min2) + " " + "max damage: " + str(max2))
    print("How to play!\nPress a to attack\npress h to heal(if you have at" +
          "least 10 rage)\npress q to wimp out\n")
    print('FIGHT!!!!!!')
    Perseus = Gladiator('Perseus', 100, 0, min1, max1)
    Spartacus = Gladiator('Spartacus', 100, 0, min2, max2)

    which_glad = input("which Gladiator are you?").strip().capitalize()
    if which_glad == "Perseus":
        glad1 = Perseus
        glad2 = Spartacus
    elif which_glad == "Spartacus":
        glad1 = Spartacus
        glad2 = Perseus
    elif which_glad == "Ares":
        print("Do you mean MARS ULTOR?")
        print("""""")
        sys.exit()
    else:
        print("sorry he died last week.")
        sys.exit()

    def turn1():
        action = input("what action do you want to complete?").strip().lower()
        if action == "a":
            print(glad1.attack(glad2))
            return glad1.attack(glad2)
        elif action == "h":
            return glad1.heal()
        elif action == "q":
            sys.exit()

    def turn2():
        action = input("what action do you want to complete?").strip().lower()
        if action == "a":
            print(glad2.attack(glad1))
            return glad2.attack(glad1)
        elif action == "h":
            return glad2.heal()
        elif action == "q":
            sys.exit()

    def dead():
        if Perseus.is_dead():
            print("FATALITY!!!! Perseus is DEAD! Spartacus WINS!")
            os.system("echo 'FATALITY!!!!!.'")
            os.system("say 'FATALITY!!!!!!'")
            print("""                                            .""--.._
                                               []      `'--.._
                                               ||__           `'-,
                                             `)||_ ```'--..       \\
                         _                    /|//}        ``--._  |
                      .'` `'.                /////}              `\/
                     /  .\""".\              //{///
                    /  /_  _`\\            // `||
                    | |(_)(_)||          _//   ||
                    | |  /\  )|        _///\   ||
                    | |L====J |       / |/ |   ||
                   /  /'-..-' /    .'`  \  |   ||
                  /   |  :: | |_.-`      |  \  ||
                 /|   `\-::.| |          \   | ||
               /` `|   /    | |          |   / ||
             |`    \   |    / /          \  |  ||
            |       `\_|    |/      ,.__. \ |  ||
            /                     /`    `\ ||  ||
           |           .         /        \||  ||
           |                     |         |/  ||
           /         /           |         (   ||
          /          .           /          )  ||
         |            \          |             ||
        /             |          /             ||
       |\            /          |              ||
       \ `-._       |           /              ||
        \ ,//`\    /`           |              ||
         ///\  \  |             \              ||
        |||| ) |__/             |              ||
        |||| `.(                |              ||
        `\\\\` /`                 /              ||
           /`                   /              ||
     jgs  /                     |              ||
         |                      \              ||
        /                        |             ||
      /`                          \            ||
    /`                            |            ||
    `-.___,-.      .-.        ___,'            ||
             `---'`   `'----'`
        """)
            webbrowser.open("https://www.youtube.com/watch?v=FsqJFIJ5lLs")
            sys.exit()
        elif Spartacus.is_dead():
            print("FATALITY!!!! Spartacus is DEAD! Perseus WINS!")
            os.system("echo 'FATALITY!!!!!.'")
            os.system("say 'FATALITY!!!!!!'")
            print("""                            ,--.
                              {    }
                              K,   }
                             /  `Y`
                        _   /   /
                       {_'-K.__/
                         `/-.__L._
                         /  ' /`\_}
                        /  ' /     -ART BY ZEUS-
                ____   /  ' /
         ,-'~~~~    ~~/  ' /_
       ,'             ``~~~%%',
      (                     %  Y
     {                      %% I
    {      -                 %  `.
    |       ',                %  )
    |        |   ,..__      __. Y
    |    .,_./  Y ' / ^Y   J   )|
    \           |' /   |   |   ||
     \          L_/    . _ (_,.'(
      \,   ,      ^^""' / |      )
        \_  \          /,L]     /
          '-_`-,       ` `   ./`
             `-(_            )
                 ^^\..___,.--`

        """)
            webbrowser.open("https://www.youtube.com/watch?v=FsqJFIJ5lLs")
            sys.exit()

    def showstuff():
        print(str(Perseus.name) + ": " + str(Perseus.health) + " " + "Rage: " +
              str(Perseus.rage), end='\t')
        print(str(Spartacus.name) + ": " + str(Spartacus.health) + " " +
              "Rage: " + str(Spartacus.rage))

    showstuff()
    while (glad1.is_dead() or glad2.is_dead())is False:
        turn1()
        dead()
        showstuff()
        turn2()
        dead()
        showstuff()
if __name__ == '__main__':
        main()
