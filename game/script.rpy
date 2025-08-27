# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg grass2 = "grass2.png"
image bg gloomy = "gloomy.png"
define rk = Character("Red King", color="#c00")
define you = Character("You", color="#ffffff")
screen delayed_voice:
    timer 0.45 action [Play("voice", "line1.mp3"), Hide("delayed_voice")]

default strength = 32
default troop_hp = 64
default attack_frame = 1
init python:
    class AttackTroop(Action):
        """
            You attack the giant!
        """
        def __call__(self):
            global strength, troop_hp, attack_frame
    
            if troop_hp > 0:
                attack_frame = (attack_frame % 3) + 1
                if attack_frame == 3:
                    troop_hp -= strength
                renpy.restart_interaction()
            else:
                renpy.notify("You won!")

screen giant_minigame:
    text "Health Left: [troop_hp]" xalign 0.5 yalign 0.25
    
    if attack_frame == 1:
        add "attack1.png" xalign 0.5 yalign 0.5 at Transform(zoom=0.75)
    elif attack_frame == 2:
        add "attack2.png" xalign 0.5 yalign 0.5 at Transform(zoom=0.75)
    elif attack_frame == 3:
        add "attack3.png" xalign 0.5 yalign 0.5 at Transform(zoom=0.75)
    imagebutton:
        idle "giant.png"
        xalign 1.0 yalign 1.0
        at Transform(zoom=0.75, alpha=0.0)
        action AttackTroop()
    
    textbutton "Exit" xalign 0.5 yalign 0.8


label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg grass2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show rk plot at left_move
    transform left_move:
        xalign -0.5
        linear 1.0 xalign 0.5

    play audio "laugh.mp3"
    show screen delayed_voice

    # These display lines of dialogue.
    rk "Fame, wealth, and power shall be mine soon." 
    show rk plot at Transform(xalign=-0.25, xzoom=-1.0)
    show bg gloomy
    with Dissolve(1.0)
    rk "With my troops, the Blue King cannot stop us!" 

    jump choices


    # This ends the game.

    return

label choices:
    default bad = False
    rk "Hey who is there?"
    menu:
        "Betray your king":
            you "Wait hold on! I am a good boy for you!"
            you "You and I have a common enemy!"
            jump choices1_a

        "Stay loyal to your king, but risk dying":
            $ randfloat = renpy.random.random()
            if randfloat < 0.75:
                jump start
            else:
                you "I must flee and tell the King at once"
                jump choices1_b

label choices1_a:
    $ bad = True
    rk "Well, well. Now what exactly does a little guy like you and I have in common?"
    you "Ever since he began to accept more troops, especially that hog, I haven't been able to fight once!"
    jump flags

label choices1_b:
    rk "Not so fast! We shall play a game to determine if you truly deserve your freedom!"
    show attack1
    call screen giant_minigame
    jump flags

label flags:
    if bad:
        you "Hey, what will I get as a reward pal!"
        rk "The finest barallel of elixir a barbarian could want"
    else:
        "Wow! Well Played!"
    return