# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg grass2 = "grass2.png"
image bg gloomy = "gloomy.png"
image bg bar1 = "bar1.png"
image bg bar2 = "bar2.png"
image bg beach1 = "hr dream.png"
image bg beach2 = "beach.png"
image bg home1 = "hr home1.png"
image bg home2 = "hr home2.png"
image bg home3 = "hr home3.png"
default c1 = "a"
define rk = Character("Red King", color="#c00")
define you = Character("You", color="#00A1F0")
define hr = Character("Hog Rider", color="#c1842e")
define hog = Character("Hog", color="#e787d2")
define ar = Character("Archers", color="#ea7397")
define ba = Character("Archers", color="#f1dc3e")
define al = Character("Crowd", color="#7d7d7d")
define va = Character("Valkaryie", color="#ee802c")
define go = Character("Goblin", color="#71d63b")
define an = Character("Announcer", color="#98403a")
screen delayed_voice(filename):
    timer 0.45 action [Play("voice", filename), Hide("delayed_voice")]

default strength = 32
default troop_hp = 64
default attack_frame = 1
init python:
    class AttackTroop(Action):
        """
            you attack the giant!
        """
        def __call__(self):
            global strength, troop_hp, attack_frame
    
            if troop_hp > 0:
                attack_frame = (attack_frame % 3) + 1
                if attack_frame == 3:
                    troop_hp -= strength
                renpy.restart_interaction()
            else:
                renpy.notify("you won!")

screen giant_minigame:
    
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
    text "Health Left: [troop_hp]" xalign 0.5 yalign 0.25

    textbutton "Exit" xalign 0.5 yalign 0.8

transform left_move:
    zoom 0.75
    yalign 1.0
    xalign -0.5
    linear 1.0 xalign 0.5
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg grass2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show rk plot at left_move

    play audio "laugh.mp3"
    show screen delayed_voice("line1.mp3")

    # These display lines of dialogue.
    rk "Fame, wealth, and power shall be mine soon." 
    show rk plot at Transform(xalign=0.0, yalign=0.9, xzoom=-0.75, yzoom=0.75)
    show bg gloomy
    with Dissolve(1.0)
    show screen delayed_voice("line2.mp3")
    play audio "laugh.mp3"
   
    rk "With my troops, the Blue King won't know what's coming to him!" 
    jump c1

label c1:
    rk "Hey who's chubby...short? And yellow hair is that!"
    hide rk plot with Dissolve(0.5)
    show screen two_images("you lie1.png", "you lie2.png", 0.4, 0.9, 1.75)  with Dissolve(0.5)

    you "What do I do?"
    menu:
            "Stay loyal to your King":
                $ rand = renpy.random.random()
                if rand > 0.85:
                    hide screen two_images with Dissolve(0.5)
                    rk "Guards take him away!"
                    window hide
                    show screen bye
                    pause 2.0
                    hide screen bye
                    # You get beat up <ADD SCENE> -> Brainwashed to join the Red Army?
                    jump start
                else:
                    hide screen two_images with Dissolve(0.5)
                    you "Rats!"
                    $ c1 == "a"
                    jump c1a
            
            "Reveal you are a traitor":
                $ c1 == "b"
                hide screen two_images with Dissolve(0.5)
                hide bg gloomy
                show bg grass2
                show rk plot at Transform(xalign=1.0, yalign=1.0, zoom=0.65)
                show you plot at Transform(xalign=0.1, yalign=1.0, zoom=1.5)
                you "Wait hold on!"
                you "Heh. You and I both have something in common."
                you "I think we can work something out! What do you say?"
                jump c1b

label c1a:
    rk "Well if it isn't a runt for the Blue King!"
    menu:
        "Lie about your affiliation":
            you "What! No?"
            you "Don't you know who I am?"
            rk "Hmmm..."
            rk "I don't actually know."
            rk "Are you Tom, Jeff, or Jerry? You barbarians all look the same."
            you "I'm Jerry."
            rk "I see."
            $ rand = renpy.random.random()

            if rand < 0.25:
                rk "Ah yes, Jeff!"
                $ lie_name = True
                jump c1a1
            else:
                rk "Do you find me for a fool!"
                rk "Guards call Tom, Jeff, and Jerry take this imbecile away"
                jump start
    
        "Stay truthful to your king":
            you "I could never dare to be seen serving a coward!"
            
            $ rand = renpy.random.random()
            if rand > 0.1:
                rk "Well now..."
                rk "We have quite the bratty snot."
                rk "Like father like son, huh?"
                jump c1a2
            else:
                rk "Farewell... Guards feed this fool to the Pekka's playhouse."
                rk "At least there he could be of some use!"
                jump start

label c1a1:
    rk "However, I have sneaking suspicion of who you say you really are"
    rk "How can I trust you?"
    you "Why would I lie!"
    rk "Actually I have an idea. Let's play a game..."
    rk "To see if you really are who you say you are!"
    you "Ok!"
    rk "You must know I hate rubbish, weaklings!"
    rk "Therefore, you will duel against my strongest troop!"
    rk "Here's the catch, if you run out of time, or you lose the game is over!"
    rk "Prove me wrong that you aren't the same old trash as your brothers!"
    call screen giant_minigame
    # if user wins
    rk "I am satisfied with you! Jerry, Jeff or whatever..."
    you "Thank you!"
    rk "Well now, child. I have a mission specifically for you!"
    rk "I want you to go into our enemy's territory"
    you "But my Lord, isn't that dangerous?"
    rk "I'm sure you will figure it out!"
    rk "You and the rest of the barbarians all look the same!"
    you "Very well..."
    you "Lord, what would you like me to do there?"
    rk "Terroize the village!"
    you "How so?"
    rk "Child you ask too many questions!"
    you "I will not do that against sir!"
    rk "Asking questions make people become idiots like that twat!"
    rk "There will be archers waiting at the tavern for you and will tell you what to do!"
    you "(Leave)"
    rk "This twat really takes me for a fool!"
    jump c2b

label c1a2:
    rk "You know, I like people who are overconfident!"
    rk "Do you know why?"
    menu:
        "Why?":
            rk "Because they are weak and easy to exploit!"
            jump c1a2a
        "I could care less":
            jump c1a2a
    menu:
        "It's the hog!":
            jump c1a2a1
        "No I don't!":
            jump c1a2a2
    rk "My child, there will be two archers waiting for you at the tavern"
    rk "There they will instruct what you shall do!"
    you "The tavern..."
    rk "Yes! Hurry now! Time is running out."
    #End scene with evil smirk
    jump c2b

label c1a2a:
    rk "I'll tell you something."
    rk "Deep down you know your king is cruel!"
    you "What terrible lies!"
    rk "You know it's the truth!"
    rk "Tell me son, when was the last time that snot put you on his deck?"
    rk "I don't even need my fingers to count!"
    you "Why are you telling me this!"
    rk "I know deep down, you hate him..."
    you "That's not true!"
    rk "Oh ho! But it is!"
    you "What blasphemy!"
    rk "Calm down child."
    rk "I can fix you..."
    rk "You are flustered because someone had stolen your righteous spot from his deck!"
    rk "Am I wrong?"
    you "Well...not exactly..."
    rk "See, the difference between me and that lowlife is I care about my troops"
    rk "I would never, ever, cast any of them aside."
    rk "In return they stay loyal to me!"
    rk "However, that snot clearly does not see the potential you have!"
    rk "Casting you aside like you are replaceable!"
    you "Yea! Screw that snot of a loser!"
    rk "What do you say?"
    rk "You and I work together."
    rk "I'll make you our number one..."
    you "Do you mean it!"
    rk "Of course."
    rk "However, I ask that you do as I say in return."
    you "Of course I will now!"
    rk "(Discuss Plan)"
    you "Wait...I have one concern though."
    rk "Save it for later. We don't have all day here!"
    rk "Get going or do you want me to repeat myself?!"
    jump c2b

label c1a2a1:
    rk "Yes, yes!"
    you "It's all his fault"
    you "Tsh"
    you "Ever since that intolerable man and his pig joined forces my life has been ruined."
    you "My spotlight is gone now!"
    rk "That's right, it's all of his fault!"
    rk "And you didn't come here just to spy!"
    rk "You seek something else, correct?"
    you "Yes! If you help me, I'll help you be victorious tommorow!"
    rk "Very well!"
    
label c1a2a2:
    rk "You are in denial, child."
    rk "But, do not fret, I can help you."
    rk "Like the rest of my children, I care about them unlike that old snot face."
    rk "What do you say, I bring you glory, fame, and power."
    you "Do you really mean it!"
    rk "Precisely"
    rk "However you must help me..."
    # Fake tears
    rk "Because...because that brat will win tommorow's fight"
    rk "My vulnerable children will be hurt..."
    you "Hey! Don't worry! What do you want me to help you with"
    # Evil smile
    rk "Do you know who the 'Hog Rider' is?"
    you "Yes! He is the one who has stolen by spot!"
    rk "Well you will happy to know that I want you to sabotage the games tomorrow!"
    rk "It's a win-win for both of us!"
    rk "That brat will have no choice but to choose you instead of him!"
    you "That's what I wanted all along!"

label c1b:
    rk "What could you possibly share in common with me?"
    rk "You serve that lowly snot for crying out loud!"
    you "You jest! I stopped caring about that rubbish king for a long time now!"
    rk "Oho!"
    you "I can't stand that mohawk man and his hog."
    you "Ever since they became a team, my glory as the barbarian has been cast aside!"
    rk "I see!"
    you "So...Can you help me?"
    rk "Of course!"
    rk "However, you must do as I say to ensure success!"
    rk "(Discusses the plan with you)"
    you "Ok! Sounds easy enough!"
    you "Wait...I have one concern though."
    rk "Save it for later. We don't have all day here!"
    rk "Get going or do you want me to repeat myself?!"
    hide rk plot
    hide you plot
    hide bg grass2
    jump c2b

label c2a:
    hr "HOG RIDERRRRR!!!"
    hr "How's your day going Jeff?"
    ba "Jerry..." 
    hr "Oh that's your brother! What's up with being a downer?"
    ba "It's been a rough day. Grab me a barrel of elixir."
    hr "BALRIGHT!"
    you "Hey!"
    hr "So that's your brother!"
    you "Just because the King favours you more now, doesn't mean you're all of that!"
    hr "Hey, hey! I am sorry that I am helping our King win for once…"
    you "We were doing just fine without you!"
    hr "Hmmm. Remind me of the last time we won without me and my hog?"
    you "I've had enough of you! How much for the pork!"
    hr "WHAT DID YOU JUST SAY?"
    ar "Ugh. Cut it out the two of you! You guys are such a drag."
    ba "..."

label c2b:
    show bg bar1
    hr "HOG RIDERRRRR!!!"
    hr "Who's excited for tomorrowwwww!"
    hide bg bar1
    show bg bar2
    ar "And why would we..."
    hide bg bar2
    show bg bar1
    hr "Well it's the game for ultimate champion~"
    hr "How could you not be excited?"
    hide bg bar1
    show bg bar2
    ar "Maybe its exciting for you because you actually get to play"
    ar "We troops are just spectators at this point for the king!"
    you "Aye!"
    hide bg bar2
    show bg bar1
    hr "Hey, the King just sees potential in me that's all!"
    hide bg bar1
    show bg bar2
    you "Oh yea? Who would have guessed..."
    you "If it weren't for you...We would still be on our king's deck!"
    hide bg bar2
    show bg bar1
    hr "And if it weren't for me, my hog would have been roast!"
    hide bg bar1
    show bg bar2
    you "You would still be stuck here cleaning from our scraps if it weren't for you and that ugly pig!"
    ar "That's right!"
    hide bg bar2
    show bg bar1
    hr "Don't you dare speak about my precious hog like that!"
    hide bg bar1
    show bg bar2
    you "Boo hoo! What are you going to do?"
    ar "Your highness isn't here to save you!"
    hide bg bar2
    show bg bar1
    hr "How dare you speak about the king like that!"
    hr "That's it! You are not welcomed into my tavern anymore!"
    hide bg bar1
    show bg bar2
    you "Good! Your elixir taste like crap anyways!"
    hide bg bar2
    show bg bar1    
    hr "Good grief! That barbarian truly lives up to his name!"
    hide bg bar1
    jump c3b

# The Next Day
label c3b:
    call screen change_scene("The Next Day")
    show beach
    hr "Don't you love the warmth of the sun?"
    hog "Oink oink!"
    hr "The fresh smell of the sea!"
    hog "Oinkkkkk..."
    hr "The smoky smell of bacon..."
    hide bg beach1
    show hr fear
    hr "Wait bacon?!"
    ar "Hehe"
    hide hr fear
    show hr fear2
    va "It's your precious hog"
    hr "Oh my RIDERRR!"
    hr "This has got to be a dream!"
    hr "Where are you piggy?"
    hide hr fear2
    show bg beach2
    show hr shocked at Transform(zoom=0.75, yalign=1.0)
    show screen two_images("hog outline.png", "hog outline1.png", 0.75, 0.5, 0.9)
    hr "This must be a dream!"
    hr "My precious sweet pie could never be used for bacon!"
    hide hr shocked
    hide screen two_images
    show hr fear2
    show ar plot at slide_in_from_left
    ar "But it's not!"
    show you smile at slide_in_from_right
    you "This the king's punishment!"
    you "Hahaha"
    va "Do you like it medium rare or well-done?"
    ar "I prefer it raw!"
    you "I normally don't eat it rare..."
    you "But given this is a job well-done, I'm all for it!"
    hr "NOOOOOOOOO!!!"
    call clear 
    call screen change_scene("...")
    # Wake up
    show hr bed
    hr "Whew..."
    hr "It was a dream..."
    hr "But I should really get ready for the battle!"

    #(goblins smirk outside from his house)
    call clear
    show bg home1
    show hr smile at Transform(xalign=1.0, yalign=1.0, zoom=1.5)

    hr "Sweet sunshine!"
    show go plot at Transform(xalign=0.05, yalign=1.0, yzoom=0.45, xzoom= -0.45)
    hr "How do you do!"
    go "Giberrish! Giberrish!!!"
    hr "That's what I like to hear!"
    hr "Right piggy?"
    show hr sad at Transform(xalign=1.0, yalign=1.0, zoom=1.5)
    hr "Wait a minute..."
    hr "Where did my cute, pink, precious squishy melon go?"

    #(Look under bed sheets)
    show hr shocked at Transform(xalign=1.0, yalign=1.0, xzoom=-0.5, yzoom=0.5)

    hr "I need to find my piggy!"
    hr "Hey do you know where he is?"
    go "Gib-errrish!"
    hr "Hmmm..."
    hr "That's unfortunate."
    hr "Well, see you later at the arena!"
    go "Giberish!"
    call clear
    show bg home2
    show hr sad at Transform(xalign=-0.1, yalign=1.0, xzoom=-1.25, yzoom=1.25)

    hr "I know you like to play games and all but today we don't have time for that!"
    hr "..."
    hr "There's fresh carrot for you downstairs!"
    hr "..."
    #(Transition to him searching his entire house)
    hr "That's strange, I'm sure he would fall for that."
    #(News turns on)
    hr "Where could he possibly be?"
    call clear
    show bg home3
    an "Good morning everyone!"
    an "We are live from TV Storyboard."
    an "Let's hear word from our reporter, Jess at the Arena"
    call clear
    show news at zoom_out
    an "Who is excited for today's match?"
    an "I sure am!"
    an "After yesterdays upsetting match 3-2 for Red, things look dicey!"
    an "As long as the Hog Rider pulls his act together..."
    an "Blue appears like the clear victor!"
    an "Only time will tell..."
    an "Back to you Jessica!"
    call clear
    show bg home3
    an "I certainly can hear plenty of cheering out there."
    an "With one more hour left on the clock..."
    an "Get your popcorn, or head towards the tavern for elixir because..."
    an "This is a battle you cannot miss!"
    call clear
    show bg home2
    show hr sad at Transform(xalign=-0.1, yalign=1.0, xzoom=-1.25, yzoom=1.25)
    hr "Oh no! This is a disaster!"
    hr "I need to find that piggy quick."
    hr "My king and my team needs be down at the arena!"
    call clear
    call screen change_scene("6 Hours Before")
    jump c4

label c4:
    you "You guys think this is a good idea?"
    ar "Relax!"
    ar "It's not like we are going to cook the pig alive!"
    go "Gibberish!!!"
    ar "Come on are you really going to chicken out last minute!"
    menu:
        "Of course, I'm not!":
            jump c4a
        "I don't know...":
            jump c4b # ADD DIALOGUE FOR THIS SH


label c4a:
    you "So, what do we do..."
    ar "Simple, we will sneak into his house..."
    ar "And then slice his pig into pork chop!"
    # show you fear    
    ar "Just kidding."
    ar "But if we did, would you?"
    menu:
        "Uhh...I dunno":
            jump c4p
        "I am salivating thinking about it":
            jump c4a2

label c4p:
    if c1 == "a":
        you "But that man and his hog make one heck of a partner"
        you "I don't know about this..."
        you "If we want to stand a chance against the Red King...!"
        you "We need him!"
        ar "But…but what about us?"
        ar "We, the weak will never be important if we are merely stepping stools!"
        go "Gibberish! Gold!"
        # you (Look at your small muscles)
        menu:
            "I am too foolish!":
                jump c4a1
            "No, I refuse!":
                jump c4a1 # CHANGE THIS BRUH
    if c1 == "b":
        you "Must I really betray my king?"
        ar "This is not betrayal, this is justice!" (VERBAL IRONY!)
        ar "Wouldn't you agree? Or are you too much of a coward!"
        you "Ok fine!"
        you "I will do it then."
        jump c4a1

label c4a1:
    ar "You seem a little hesitant!"
    you "No I am not!"
    ar "Ok then, grab his pig and do it!"
    you "Do what?"
    ar "Roast the pig!"
    ar "The goblins deserve to this feast!"
    # show you fear
    you "Ok..."
    you "But what if I fail?"
    ar "You won't."
    ar "Now shoot."
    jump c4a1a

label c4a2:
    ar "That's the spirit!"
    you "So who's going to do it?"
    ar "You of course!"
    ar "We will watch over..."
    ar "Make sure nobody tries anything funny!"
    ar "Kapeesh?"
    you "Bahlright..."
    jump c4a1a

label c4a1a:
    you "Ah ha, there you are buddy!"
    hog "oink?"
    you "Shhh, easy now!"
    you "Your companion asked me to come get you!"
    hog "oink oink?"
    you "Yeah..."
    you "He's busy with the king."
    hog "oink! oink!"
    you "..."
    you "Sorry things just have to be this way! No hard feelings!"
    menu:
        "Kidnap the pig":
            jump c4a1a1
        "Betray the plan":
            jump c4a1b

label c4a1a1:
    you "Let's see how heavy you are"
    pig "OINK OINK!"
    you "Chill!"
    you "It's not like anything I'll kidnap!"
    pig "OINK. OINK. OINK."
    you "You are pissing me off"
    you "Ok fine, let's play a game."
    pig "oink?"
    you "Yea! The winner gets corn!"
    you "Loser has to do what I say."
    pig "Oink!"
    you "Looks like you love games"
    you "Heh. But this game won't be favourable for you buddy"
    you "The premise is simple if you get to the corn before me, you win"
    you "But here's the catch!The amount of steps you can take per turn is dependent on what number you and I pick!"
    pig "oink?"
    you "We will add both of our numbers that we pick from 1-10"
    you "If the sum is odd I move the amount of steps I chose and if it's even then your move!"
    you "The game ends when either of us have made 100 steps"
    jump corn_minigame
    # jump c4a1ab

label c4a1ab:
    you "Nobody is going to know..."
    you "I just need to buy some time..."
    you "I know!"
    call change_scene("Moments Later...")
    you "There!"
    you "Now be a good boy and stay here ok?"
    hog "Oink! Oink!"
    call change_scene("More Momenets Later...")
    #(walk back to the rest of the team
    you "Hey where'd everyone go?"

label corn_minigame:
    $ player_progress = 0
    $ pig_progress = 0

    show screen race_screen

    while player_progress < 10 and pig_progress < 10:
        $ renpy.pause(0.1)

    hide screen race_screen
    if player_progress >= 10 and pig_progress >= 10:
        you "It was close, but I got the corn!"
        hog "OINK!!"
    elif player_progress >= 10:
        you "Ha! I got the corn first!"
        hog "OINK!!"
    else:
        hog "OINK! OINK!"
        you "Argh — the pig wins and eats the corn."

    return    
# lose:
# 	pig "OINK!"
# 	you "Ok here is your prize"
# 	(You capture the pig in the net)
# 	you "Hey man, no hard feelings"
# 	jump c4a1a1

# win:
# 	pig "oink…"
# 	you "Well, no hard feelings"
# 	(You capture the pig in the net)
# 	jump c4a1a1


label clear:
    scene black with Dissolve(0.6)
    hide screen change_scene
    hide screen bye
    hide screen two_images
