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
image bg night = "hr night.png"
image bg night2 = "hr night2.png"
image bg corngame = "hr night3.png"
default winner = None
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

    # play audio "laugh.mp3"
    # show screen delayed_voice("line1.mp3")

    # These display lines of dialogue.
    rk "Fame, wealth, and power shall be mine soon." 
    show rk plot at Transform(xalign=0.0, yalign=0.9, xzoom=-0.9, yzoom=0.9)
    show bg gloomy
    with Dissolve(1.0)
    # show screen delayed_voice("line2.mp3")
    # play audio "laugh.mp3"
   
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
                    show you fear at Transform(xalign=0.5, yalign=1.25, zoom=1.6)
                    you "Rats!"
                    $ c1 == "a"
                    call clear
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
    show bg grass2
    show rk plot at Transform(xalign=0.0, yalign=1.0, xzoom=-0.6, yzoom=0.6)
    show you sad at Transform(xalign=0.9, yalign=1.25, zoom=1.0)
    rk "Well if it isn't a runt for the Blue King!"
    menu:
        "Lie about your affiliation":
            show you lie1 at Transform(xalign=0.9, yalign=1.0, zoom=1.45)
            you "What! No?"
            show you lie2 at Transform(xalign=0.9, yalign=1.0, zoom=1.45)
            you "Don't you know who I am?"
            rk "Hmmm..."
            rk "I don't actually know."
            rk "Are you Tom, Jeff, or Jerry? You barbarians all look the same."
            show you lie1 at Transform(xalign=0.9, yalign=1.0, zoom=1.45)
            you "I'm Jerry."
            rk "I see."
            $ rand = renpy.random.random()

            if rand < 0.75:
                show you smile at Transform(xalign=0.9, yalign=1.0, zoom=1.5)

                rk "Ah yes, Jeff!"
                $ lie_name = True
                jump c1a1
            else:
                rk "Do you find me for a fool!"
                rk "Guards call Tom, Jeff, and Jerry take this imbecile away"
                call clear
                jump start
    
        "Stay truthful to your king":
            show you smile at Transform(xalign=0.9, yalign=1.25, zoom=1.0)
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
    rk "However, I have sneaking suspicion of who you say you really are..."
    rk "How can I trust you?"
    show you lie2 at Transform(xalign=0.9, yalign=1.0, zoom=1.45)
    you "Why would I lie!"
    rk "Actually I have an idea. Let's play a game..."
    rk "To see if you really are who you say you are!"
    show you lie1 at Transform(xalign=0.9, yalign=1.0, zoom=1.45)
    you "Ok!"
    rk "You must know I hate rubbish..."
    rk "Weaklings..."
    rk "Therefore, you will duel against the giant!"
    rk "Please do prove me wrong"
    rk "Click to Attack!"
    call clear
    call screen change_scene("Remember Click to Attack!")
    window hide
    $ success = renpy.call_screen("giant_minigame")
    window show
    if success:
        show bg grass2
        show rk plot at Transform(xalign=0.0, yalign=1.0, xzoom=-0.6, yzoom=0.6)
        show you lie1 at Transform(xalign=0.9, yalign=1.0, zoom=1.45)
        rk "I am satisfied with you! Jerry, Jeff or whatever..."
        you "Thank you!"
        rk "Well now, child. I have a mission specifically for you!"
        jump c2b
    else:
        show bg gloomy
        show rk plot at Transform(xalign=0.0, yalign=1.0, xzoom=-0.6, yzoom=0.6)
        show you sad at Transform(xalign=0.9, yalign=1.0, zoom=1.45)
        rk "Pathetic. You could not finish the trial in time."
        rk "Return when you have some real strength."
        call clear
        jump start

label c1b:

    rk "What could you possibly share in common with me?"
    rk "You serve that lowly snot for crying out loud!"
    show you lie2 at Transform(xalign=0.05, yalign=1.0, zoom=1.45)
    you "You jest! I stopped caring about that rubbish king for a long time now!"
    rk "Oho!"
    show you neutral at Transform(xalign=0.03, yalign=1.0, zoom=1.45)
    you "I can't stand that mohawk man and his hog."
    you "Ever since they became a team..."
    you "My glory as the barbarian has been cast aside!"
    rk "I see!"
    show you plot at Transform(xalign=0.05, yalign=1.0, zoom=1.45)
    you "So...Can you help me?"
    show rk plot at Transform(xalign=0.95, yalign=1.2, xzoom=1.15, yzoom=1.15)
    rk "Of course!"
    rk "However, you must do as I say to ensure success!"
    show you plot at Transform(xalign=0.05, yalign=1.0, zoom=1.45)
    show rk plot at Transform(xalign=1.0, yalign=1.0, xzoom=1.0, yzoom=1.0)
    you "Ok! Sounds easy enough!"
    show you sad at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    you "Wait...I have one concern though."
    show rk plot at Transform(xalign=0.95, yalign=1.2, xzoom=1.15, yzoom=1.15)
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
    show bg night
    show you fear at Transform(xalign=0.95, yalign=1.25, zoom=1.6)
    you "You guys think this is a good idea?"
    show ar smile at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "Relax!"
    ar "It's not like we are going to cook the pig alive!"
    hide ar smile
    show go plot at Transform(xalign=0.15, yalign=0.65, xzoom=-0.35, yzoom=0.35)
    show ar smile at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    go "Gibberish!!!"
    hide ar smile
    show ar plot at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "Come on are you really going to chicken out last minute!"
    menu:
        "Of course, I'm not!":
            call clear
            jump c4a
        "I don't know...":
            call clear
            jump c4b


label c4a:
    show bg night
    show you lie1 at Transform(xalign=0.95, yalign=1.25, zoom=1.6)
    show go plot at Transform(xalign=0.15, yalign=0.65, xzoom=-0.35, yzoom=0.35)
    show ar plot at Transform(xalign=0.0, yalign=1.0, zoom=0.75)

    you "So, what do we do..."
    ar "Simple, we will sneak into his house..."
    ar "And then slice his pig into pork chop!"
    show ar smile at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    show you fear at Transform(xalign=0.95, yalign=1.25, zoom=1.6)
    # show you fear    
    ar "Just kidding."
    ar "But if we did, you wouldn't mind right?"
    menu:
        "Uhh...I dunno":
            call clear
            jump c4p
        "I am salivating thinking about it":
            call clear
            jump c4a2

label c4b:
    ar "Cmon I know you are that much of a weakling..."
    ar "Are you really going to betray us..."
    ar "Even after our king specifically gave you a mission?"
    ar "We have never had that honour!"
    you "You're right..."
    ar "Think about the glory!"
    ar "Isn't that what you want?"
    ar "You came to the king seeking the very power the hog rider has stolen from you"
    you "Yea..."
    ar "And now you can take it back!"
    ar "What do you say?"
    ar "Or are you still the same old coward I thought you were..."
    you "No I am not!"
    you "But do you promise the king will make me like him?!"
    ar "Of course!"
    ar "We would never lie!"
    you "Ok fine, I'll do it..."
    jump c4a2

label c4p:
    if c1 == "b":
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
                jump c4b
    if c1 == "a":
        show bg night
        show you sad at Transform(xalign=0.85, yalign=1.1, zoom=1.0)
        show go plot at Transform(xalign=0.15, yalign=0.65, xzoom=-0.35, yzoom=0.35)
        show ar smile at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
        you "Must I really"
        show ar plot at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
        ar "This is not betrayal, this is justice!"
        ar "Justice against the atrocities committed by the Hog Rider!"
        show ar talk at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
        ar "Wouldn't you agree?"
        show you lie2 at Transform(xalign=0.95, yalign=1.25, zoom=1.6)

        you "I guess so..."
        show ar plot at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
        ar "Are you too much of coward to leave a blind eye to this?!"
        show you sad at Transform(xalign=0.85, yalign=1.1, zoom=1.0)
        you "Ok fine!"
        show you fear at Transform(xalign=0.95, yalign=1.25, zoom=1.6)
        you "I will do it then."
        call clear
        jump c4a1

label c4a1:
    show bg night
    show go plot at Transform(xalign=0.15, yalign=0.65, xzoom=-0.35, yzoom=0.35)
    show ar sad at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    show you fear at Transform(xalign=0.95, yalign=1.25, zoom=1.6)
    ar "You still seem a little hesitant!"
    you "No I am not!"
    show ar talk at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "Ok then, grab his pig and do it!"
    you "Do what?"
    show ar plot at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "Roast the pig!"
    show ar smile at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "The goblins deserve a feast!"
    go "Giiberish!"
    # show you fear
    show you sad at Transform(xalign=0.85, yalign=1.1, zoom=1.0)
    you "Ok..."
    you "But what if I fail?"
    show ar plot at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "You won't."
    ar "Now shoot."
    call clear
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
    show bg night2
    show you plot at Transform(xalign=0.1, yalign=1.1, zoom=1.25)
    you "Ah ha, there you are buddy!"
    show hog bruh at Transform(xalign=1.0, yalign=1.0, zoom=1.0)
    hog "oink?"
    you "Your a lot bigger in person, wow!"
    you "Shhh, easy now!"
    menu:
        "Continue with kidnapping":
            call clear
            jump c4a1a1
        "Betray the plan":
            hide you plot
            show screen two_images("you lie1.png", "you lie2.png", 0.05, 1.1, 1.25)  with Dissolve(0.5)
            you "The king asked me to come get you!"
            show hog plot at Transform(xalign=1.0, yalign=1.0, zoom=1.0)
            hog "oink oink?"
            you "Yeah..."
            you "It's about your buddy"
            hog "oink! oink!"
            you "..."
            show hog sad at Transform(xalign=1.0, yalign=1.0, zoom=1.0)
            you "He's been kidnapped!"
            hog "OINK!"
            call clear
            jump c4a1ab

label c4a1a1:
    show bg night2
    show you plot at Transform(xalign=0.1, yalign=1.1, zoom=1.25)
    show hog sad at Transform(xalign=1.0, yalign=1.0, zoom=1.0)
    you "Let's see how heavy you are"
    show hog angry at Transform(xalign=1.0, yalign=1.0, zoom=1.0)
    hog "OINK OINK!"
    you "Chill!"
    you "Relax, it's not like I'm kidnapping you or anything!"
    hog "OINK. OINK. OINK."
    show you fear at Transform(xalign=-0.1, yalign=1.1, zoom=1.25)
    you "You are pissing me off"
    hog "OINK!"
    show you smile at Transform(xalign=-0.1, yalign=1.1, zoom=1.25)
    you "Ok fine, let's play a game."
    show hog bruh at Transform(xalign=1.0, yalign=1.0, zoom=1.0)
    hog "oink?"
    show you plot at Transform(xalign=0.1, yalign=1.1, zoom=1.25)
    you "Yea!"
    you "If you win, I leave!"
    you "If you lose, you have to do what I say."
    show hog plot at Transform(xalign=1.0, yalign=1.0, zoom=1.0)
    hog "Oink! Oink!"
    show you smile at Transform(xalign=-0.1, yalign=1.1, zoom=1.25)
    you "Looks like you love games..."
    you "Heh. But this game won't be favourable for you buddy..."
    show you plot at Transform(xalign=0.1, yalign=1.1, zoom=1.25)
    call clear
    call screen change_scene("Press Space to Run...")
    call corn_minigame
    if winner == "player" or winner == "tie":
        you "Well, follow me..."
        show bg night2
        show you plot at Transform(xalign=0.1, yalign=1.1, zoom=1.25)
        show hog sad at Transform(xalign=1.0, yalign=1.0, zoom=1.0)
        window hide
    else:
        you "Heh..."
        you "I never said which corn!"
        you "I had one in my pocket all along!"
        you "Now, follow me..."
        window hide
    menu:
        "Put him on a leash":
            you "Now stay quite..."
            you "Heh..."
            call clear
            ar "Well done!"
            ar "Bring the hog to the goblins"
            you "Ok..."
            ar "Now, your work has been done..."
            ar "The king sees no further use in you!"
            you "What?!"
            ar "What are you going to do?"
            ar "Fight all of us at once?"
            ar "Yea shoot!"
        "Put him in a box":
            you "Ok, now be quite..."
            call clear
            jump c4a1ab
    # THE PIG IS NOT INSIDE THE CRATE/THE PIG ON A LEASH ISNT THE SAME PIG

label c4a1ab:
    show bg night2
    show you sad at Transform(xalign=0.5, yalign=1.0, zoom=1.0)
    you "Nobody is going to know..."
    you "I just need to buy some time..."
    call screen change_scene("Moments Later...")
    show you neutral at Transform(xalign=0.5, yalign=1.0, zoom=1.5)
    you "There!"
    you "Now be a good boy and stay here ok?"
    hog "Oink! Oink!"
    call clear
    call screen change_scene("More Momenets Later...")
    show bg night
    show you sad at Transform(xalign=0.5, yalign=1.0, zoom=1.0)
    you "Hey where'd everyone go?"
    scene black with Dissolve(0.8)
    window hide
    show text "{size=56}{color=#ffffff}To be continued...{/color}{/size}" at Transform(xalign=0.5, yalign=0.5)
    pause 3.5
    hide text
    return

label corn_minigame:
    show bg corngame 
    # show you plot2 at Transform(xalign=0.0, yalign=0.6, zoom=0.2)
    # show hog smile at Transform(xalign=-0.03, yalign=0.75,zoom=0.5)
    $ player_progress = 0
    $ pig_progress = 0
    you "Press Space Remember!"
    call screen change_scene("Ready? 3, 2, 1...")

    window hide
    $ winner = renpy.call_screen("race_screen")
    window show
    hide screen race_screen

    if winner == "player":
        you "It was close, but I got the corn!"
        hog "OINK!!"
    elif winner == "pig":
        hog "OINK OINK!!"
        you "Argh..."
    else:
        you "It's a tie, so I win!"
        hog "OINK OINK OINK..."
    return

label clear:
    scene black with Dissolve(0.6)
    hide screen change_scene
    hide screen bye
    hide screen two_images
