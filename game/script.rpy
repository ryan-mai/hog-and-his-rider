# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg grass2 = "grass2.png"
image bg gloomy = "gloomy.png"
image bg bar1 = "bar1.png"
image bg bar2 = "bar2.png"
image bg backyard = "hr_backyard.png"
image bg beach1 = "hr_dream.png"
image bg beach2 = "beach.png"
image bg home1 = "hr_home1.png"
image bg home2 = "hr_home2.png"
image bg home3 = "hr_home3.png"
image bg home3b = "hr_home3b.png"
image bg night = "hr_night.png"
image bg night_box = "hr_night_box.png"
image bg night2 = "hr_night2.png"
image bg night2_box = "hr_corn_box.png"
image bg corngame = "hr_night3.png"
image bk fear = "bk_fear.png"
image bg s1 = "rk_s1.png"
image bg s2 = "rk_s2.png"
image bg s3 = "rk_s3.png"
image bg s4 = "rk_s4.png"
image bg s5 = "rk_s5.png"
image bg s6 = "rk_s6.png"
image bg s7 = "rk_s7.png"
image bg s8 = "rk_s8.png"
image bg bk = "bk_bg.png"
image bk down = "bk_down.png"
image bk up = "bk_up.png"
image ar plot = "ar_plot.png"
image ar sad = "ar_sad.png"
image ar smile = "ar_smile.png"
image bg shed = "hr_shed.png"
image ar talk = "ar_talk.png"
image go plot = "go_plot.png"
image hog angry = "hog_angry.png"
image hog bruh = "hog_bruh.png"
image hog na = "hog_na.png"
image hog outline = "hog_outline.png"
image hog outline1 = "hog_outline1.png"
image hog plot = "hog_plot.png"
image hog sad = "hog_sad.png"
image hog smile = "hog_smile.png"
image hr bed = "hr_bed.png"
image hr fear = "hr_fear.png"
image hr fear2 = "hr_fear2.png"
image hr sad = "hr_sad.png"
image hr shocked = "hr_shocked.png"
image hr smile = "hr_smile.png"
image hr talk = "hr_talk.png"
image news = "news.png"
image purple choice = "purple_choice.png"
image rk plot = "rk_plot.png"
image rk excited = "rk_excited.png"
image you fear = "you_fear.png"
image you lie1 = "you_lie1.png"
image you lie2 = "you_lie2.png"
image you neutral = "you_neutral.png"
image you plot = "you_plot.png"
image you plot2 = "you_plot2.png"
image you sad = "you_sad.png"
image you smile = "you_smile.png"
default winner = None
default c1 = "a"
define rk = Character("Red King", color="#c00")
define bk = Character("Red King", color="#1a93ff")
define you = Character("You", color="#31bde8")
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
    pause 1.0
    scene black with Dissolve(0.8)
    window hide
    show text "{size=28}{color=#ff3425}Under Section 107 of the Copyright Act 1976, allowance is made for \"fair use\" for purposes such as commentary, news reporting, scholarship, and research.\nFair use is a use permitted by copyright law that might otherwise be infringing.\nNon-profit, educational, or personal use tips the balance in favor of fair use.\nAll assets used in this project are the property of Supercell.\nThis is a fan-made project inspired by Supercell's game Clash Royale and is not affiliated with, endorsed, or sponsored by Supercell.{/color}{/size}" at Transform(xalign=0.5, yalign=0.5)
    pause 3.5
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
    show screen two_images("you_lie1.png", "you_lie2.png", 0.4, 0.9, 1.75)  with Dissolve(0.5)

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
        call clear
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
    hr "Hey, hey! I am sorry that I am helping our King win for once..."
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
    show bg beach1
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
    show screen two_images("hog_outline.png", "hog_outline1.png", 0.75, 0.5, 0.9)
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
    an "Back to you Jess!"
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
    window hide
    menu:
        "Of course, I'm not!":
            call clear
            jump c4a
        "I don't know...":
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
    show ar sad at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "Even after our king specifically gave you a mission?"
    ar "We have never had that honour!"
    show you sad at Transform(xalign=0.85, yalign=1.1, zoom=1.0)
    you "You're right..."
    show ar plot at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "Think about the glory!"
    ar "Isn't that what you want?"
    ar "You came to the king seeking the very power the hog rider has stolen from you"
    show you fear at Transform(xalign=0.95, yalign=1.25, zoom=1.6)
    you "Yea..."
    ar "And now you can take it back!"
    ar "What do you say?"
    show ar talk at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "Or are you still the same old coward I thought you were..."
    show you lie1 at Transform(xalign=0.95, yalign=1.25, zoom=1.6)
    you "No I am not!"
    you "But do you promise the king will make me like him?!"
    show ar smile at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "Of course!"
    ar "We would never lie!"
    show you sad at Transform(xalign=0.85, yalign=1.1, zoom=1.0)
    you "Ok fine, I'll do it..."
    jump c4a2

label c4p:
    if c1 == "b":
        you "But that man and his hog make one heck of a partner"
        you "I don't know about this..."
        you "If we want to stand a chance against the Red King...!"
        you "We need him!"
        ar "But...but what about us?"
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
    show ar talk at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "That's the spirit!"
    show you lie2 at Transform(xalign=0.95, yalign=1.25, zoom=1.6)
    you "So who's going to do it?"
    show ar plot at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "You of course!"
    ar "We will watch over..."
    show ar smile at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
    ar "Make sure nobody tries anything funny!"
    ar "Kapeesh?"
    show you fear at Transform(xalign=0.95, yalign=1.25, zoom=1.6)
    you "Bahlright..."
    call clear
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
            show screen two_images("you_lie1.png", "you_lie2.png", 0.05, 1.1, 1.25)  with Dissolve(0.5)
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
        show bg night2
        show you plot at Transform(xalign=0.1, yalign=1.1, zoom=1.25)
        show hog sad at Transform(xalign=1.0, yalign=1.0, zoom=1.0)
        you "Heh..."
        you "I never said which corn!"
        you "I had one in my pocket all along!"
        window hide
    menu:
        "Put him on a leash":
            you "Now stay quite..."
            you "Heh..."
            call clear
            show bg night
            show go plot at Transform(xalign=0.05, yalign=1.0, yzoom=0.45, xzoom= -0.45)

            show ar plot at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
            show you plot2 at Transform(xalign=0.95, yalign=1.0, xzoom=-0.5, yzoom=0.5)
            show hog sad at Transform(xalign=1.0, yalign=1.0, zoom=0.7)

            ar "Well done!"
            ar "Bring the hog to the goblins"
            you "Ok..."
            show hog sad at hog_slide
            pause 2.0
            ar "Now, your work has been done..."
            show you fear at Transform(xalign=1.2, yalign=1.5, zoom=3.5)
            you "What do you mean?"
            show ar smile at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
            ar "The king sees no further use in you!"
            you "This must be a joke!"
            show ar plot at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
            ar "What are you going to do?"
            ar "Fight all of us at once?"
            show ar sad at Transform(xalign=0.0, yalign=1.0, zoom=0.75)
            ar "Yea shoot you scum!"
            jump c5b
        "Put him in a box":
            call clear
            show bg night2_box
            show you plot at Transform(xalign=0.9, yalign=1.1, xzoom=-1.25, yzoom=1.25)
            you "Ok, now be quiet..."
            hog "oin..k"
            call clear
            jump c4a1ab
    # THE PIG IS NOT INSIDE THE CRATE/THE PIG ON A LEASH ISNT THE SAME PIG

label c4a1ab:
    show bg night2
    show you sad at Transform(xalign=0.5, yalign=1.0, zoom=1.0)
    you "Nobody is going to know..."
    call screen change_scene("Moments Later...")
    show you neutral at Transform(xalign=0.5, yalign=1.0, zoom=1.5)
    you "Now be a good boy and stay here ok?"
    call clear
    call screen change_scene("More Momenets Later...")
    jump c5a
    # scene black with Dissolve(0.8)
    # window hide
    # show text "{size=56}{color=#ffffff}To be continued...{/color}{/size}" at Transform(xalign=0.5, yalign=0.5)
    # pause 5.0
    # hide text
    # jump start

label c5a:
    call clear
    show bg night_box
    show you sad at Transform(xalign=0.7, yalign=1.0, zoom=1.0)
    you "Hey where'd everyone go?"
    show you neutral at Transform(xalign=0.7, yalign=1.0, zoom=1.5)
    you "Was I set up?!"
    you "No..."
    show you sad at Transform(xalign=0.7, yalign=1.0, zoom=1.0)
    you "No, that is preposterous!"
    show you smile at Transform(xalign=0.7, yalign=1.0, zoom=1.5)
    you "The righteous Red King would never do such a thing!"
    you "He must have had a reason!"
    show you plot at Transform(xalign=0.7, yalign=1.0, zoom=1.5)
    you "Yeah! He's smart."
    show you lie1 at Transform(xalign=0.7, yalign=1.0, zoom=1.5)
    you "And I'm smart too..."
    show you lie2 at Transform(xalign=0.7, yalign=1.0, zoom=1.5)
    you "The king must have had a reason"
    show you plot2 at Transform(xalign=0.7, yalign=1.0, zoom=0.8)
    you "And whatever reason that was..."
    show you plot at Transform(xalign=0.7, yalign=1.0, zoom=1.5)
    you "It was surely noble..."
    you "I think this is all part of the king's plan..."
    show you plot2 at Transform(xalign=0.7, yalign=1.0, zoom=0.8)
    you "To make me great again!"
    you "He wants me to keep a hold of him..."
    show you lie1 at Transform(xalign=0.7, yalign=1.0, zoom=1.5)
    you "Unscathed..."
    show you lie2 at Transform(xalign=0.7, yalign=1.0, zoom=1.5)
    you "Just until the battle ends..."
    show you smile at Transform(xalign=0.7, yalign=1.0, zoom=1.5)
    you "The Red King is truly so noble!"

label c5b:
    call clear
    show bg night
    show you sad at Transform(xalign=0.4, yalign=1.0, zoom=1.0)
    you "Oh no!"
    you "What have I done!"
    show you fear at Transform(xalign=0.4, yalign=1.0, zoom=1.6)
    you "I should have trusted my guts..."
    show you sad at Transform(xalign=0.4, yalign=1.0, zoom=1.0)
    you "I'm such a fool..."
    you  "A failure..."
    show you fear at Transform(xalign=0.4, yalign=1.0, zoom=1.6)
    you "I can see why the king doesn't want me on his team anymore..."
    you "Not only did I give up the hog..."
    show you sad at Transform(xalign=0.4, yalign=1.0, zoom=1.0)
    you "I also was tricked."
    you "Tricked into believing the Red King was noble!"
    you "What should I do?"
    menu:
        "Go After the Archers":
            show you plot2 at Transform(xalign=0.4, yalign=1.0, zoom=0.65)
            you "I must rescue the hog!"
            you "Even if I was never a warrior to the king..."
            show you plot at Transform(xalign=0.4, yalign=1.0, zoom=1.5)
            you "I will die trying to become one!"
            scene black with Dissolve(0.8)
            window hide
            show text "{size=56}{color=#ffffff}You End Up Dying Like a Fool...{/color}{/size}" at Transform(xalign=0.5, yalign=0.5)
            pause 2.0
            show text """{size=24}{color=#ff3425}
                The ultimate championship match commences and the Blue King loses in utter defeat.
                The score is 0-3 and you end up being the scapegoat for the Blue Team losing.
            {/color}{/size}""" at Transform(xalign=0.5, yalign=0.5)
            pause 12.0
            show text """{size=24}{color=#ff3425}
                The Red King, however, thanks you for this and from then on, a cycle of corruption,
                and violence continues for years. As for the Hog Rider's pig, his hog ends up becoming enslaved
                working for days on end without food.
            {/color}{/size}""" at Transform(xalign=0.5, yalign=0.5)
            pause 12.0
            show text """{size=24}{color=#ff3425}
                In fact, the Arena becomes a circus for the Red King's entertainment
                with the pig becoming targets for the audience to throw waste at. On the other hand, the Hog Rider simply lives
                his days impoverished and outworked, building the Red King's never ending wall.
            {/color}{/size}""" at Transform(xalign=0.5, yalign=0.5)
            pause 12.0
            hide text
            jump start
        "Tell the Hog Rider":
            show you lie1 at Transform(xalign=0.4, yalign=1.0, zoom=1.5)
            you "I should tell him"
            show you lie2 at Transform(xalign=0.4, yalign=1.0, zoom=1.5)
            you "But after what I said to him at the bar..."
            show you lie1 at Transform(xalign=0.4, yalign=1.0, zoom=1.5)
            you "No."
            show you sad at Transform(xalign=0.4, yalign=1.0, zoom=1.0)
            you "That would be a bad idea..."
            you "It's pointless..."
            you "I never doing anything right"
            show you lie1 at Transform(xalign=0.4, yalign=1.0, zoom=1.5)
            you "But..."
            show you lie2 at Transform(xalign=0.4, yalign=1.0, zoom=1.5)
            you "We were never going to win anyways..."
            show you sad at Transform(xalign=0.4, yalign=1.0, zoom=1.0)
            you "..."
            jump c6

label c6:
    call clear
    call screen change_scene("6 hours after...")
    show bg home2
    show hr sad at Transform(xalign=-0.1, yalign=1.0, xzoom=-1.25, yzoom=1.25)
    hr "Hmmmm, maybe my cutiepie is outside..."
    call clear
    #Change scene
    show bg backyard
    show hr smile at Transform(xalign=1.1, yalign=1.0, xzoom=1.25, yzoom=1.25)
    hr "Well what do we have here"
    show hr talk at Transform(xalign=1.1, yalign=1.5, xzoom=1.25, yzoom=1.25)
    hr "It seems like he was up all night moving and grooving!"
    hr "Wait a minute..."
    show hr shocked at Transform(xalign=1.1, yalign=1.5, xzoom=-1.0, yzoom=1.0)
    hr "Who's tiny footprints are these?"
    hr "These sure aint mine..."
    show hr talk at Transform(xalign=1.1, yalign=1.5, xzoom=1.25, yzoom=1.25)
    hr "I wouldn't say I'm a detective or anything..."
    hr "But this is suspicious!"
    show hr sad at Transform(xalign=1.1, yalign=1.0, xzoom=1.25, yzoom=1.25)
    hr "Who's feet could be this small?"
    hr "Hmmmm"
    show hr talk at Transform(xalign=1.1, yalign=1.5, xzoom=1.25, yzoom=1.25)
    hr "Could it be?"
    hr "The barbarian..."
    show hr sad at Transform(xalign=1.1, yalign=1.0, xzoom=1.25, yzoom=1.25)
    hr "Maybe I'm just be overthinking it!"
    hr "Let me take a look inside the shed"
    call clear
    show bg shed
    show hr talk at Transform(xalign=1.1, yalign=1.5, xzoom=1.25, yzoom=1.25)
    show hog smile at Transform(xalign=-0.3, yalign=1.0, zoom=1.0)
    hr "Oh!"
    hr "There you are Squealer!"
    show hog plot at Transform(xalign=0.1, yalign=1.0, zoom=1.0)
    show hr shocked at Transform(xalign=1.1, yalign=1.5, xzoom=-1.0, yzoom=1.0)
    hr "So who's footprints were those outside?"
    hr "Wait is it your lil bro's?"
    show hr talk at Transform(xalign=1.1, yalign=1.5, xzoom=1.25, yzoom=1.25)
    show hog sad at Transform(xalign=0.1, yalign=1.0, zoom=1.0)
    hr "Bamma?"
    hog "Oink?"
    show hog plot at Transform(xalign=0.1, yalign=1.0, zoom=1.0)
    show hr sad at Transform(xalign=1.1, yalign=1.0, xzoom=1.25, yzoom=1.25)
    hr "..."
    show hr shocked at Transform(xalign=1.1, yalign=1.5, xzoom=-1.1, yzoom=1.1)
    hr "Your brother..."
    show hr shocked at Transform(xalign=1.1, yalign=1.5, xzoom=-1.2, yzoom=1.2)
    hr "Has been kidnapped..."
    show hog sad at Transform(xalign=0.1, yalign=1.0, zoom=1.0)

    #angry hog
    hog "OINK!" 
    show hr talk at Transform(xalign=1.1, yalign=1.5, xzoom=1.25, yzoom=1.25)
    hr "I saw footprints that I thought were yours!"
    hog "oink. oinkkk...oink!"
    show hr shocked at Transform(xalign=1.1, yalign=1.5, xzoom=-1.1, yzoom=1.1)
    hr "You can smell where he is?"
    show hr shocked at Transform(xalign=1.1, yalign=1.5, xzoom=-1.2, yzoom=1.2)
    hr "Where?"
    show hog smile at Transform(xalign=0.0, yalign=1.05, xzoom=-1.0, yzoom=1.0)
    hog "oinnk. oinkk! OINK!"
    show hr talk at Transform(xalign=1.1, yalign=1.5, xzoom=1.25, yzoom=1.25)
    hr "WHAT!!!"
    show hog sad at Transform(xalign=0.1, yalign=1.0, zoom=1.0)
    show hr shocked at Transform(xalign=1.1, yalign=1.5, xzoom=-1.1, yzoom=1.1)
    hr "That barbarian truly has no limits..."
    jump c7

label c7:
    call clear
    call screen change_scene("At the Arena")
    show news2
    an "The crowd is going wild"
    an "Oh?"
    hide news2
    show rk excited
    an "Looks like the Red King is especially excited!"
    an "One might ask what reason is there for the king to be so happy?"
    hide rk excited
    show news
    an "Remember, they had just lost the other day 3-2 against the Blue King!"
    an "Back to you Jess!"
    hide news
    show bg home3b
    an "Well folks, it looks like the battle is starting soon!"
    an "Grab your elixir because this is a match you cannot miss"
    an "Quite frankly, this is the end-all, be-all."
    hide bg home3b
    show rk excited
    an "It will decide who the true king of the Arena is..."
    an "Blue or Red?"
    jump c8

label c8:
    call clear
    show bk fear
    bk "Where is our star?"
    bk "The Hog Rider..."
    show bg s1
    you "..."
    ar "..."
    bk "Hey you!"
    show bg s2
    bk "Yes, you archer..."
    bk "Go look for the Hog Rider!"
    show bg s3
    bk "This is not good for us!"
    #Change to stands
    show bg s4
    bk "We need more time..."
    show bg s5
    bk "Our Hog Rider is not here!"
    show bg s6
    an "Sorry, no extra time..."
    call clear
    show bg s5
    bk "Tsh..."
    bk "Hey you barbarian."
    you "Me?"
    show bg s7
    bk "Yes, you..."
    bk "You shall be our substitute"
    show bg s8
    you "Wha...what?"
    you "But..."
    show bg bk
    hide bk fear
    show you sad at Transform(xalign=0.1, yalign=1.0, xzoom=0.8, yzoom=0.8)
    you "But I'm not like the Hog Rider!"
    show bk down at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    bk "Look."
    bk "We may not be as strong without him..."
    bk "But the key difference between my deck and his is..."
    show bk up at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    bk "Having you!"
    show you lie2 at Transform(xalign=0.1, yalign=1.0, zoom=1.5)
    you "Whaa??"
    show you lie1 at Transform(xalign=0.1, yalign=1.0, zoom=1.5)
    bk "We work together, while he controls"
    show you plot at Transform(xalign=0.1, yalign=1.0, zoom=1.5)
    you "Then, why did you choose the Hog Rider over me!"
    show bk down at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    bk "Because the Hog Rider wins battles..."
    show you sad at Transform(xalign=0.0, yalign=1.0, zoom=1.0)
    you "I knew it!"
    show you plot at Transform(xalign=0.1, yalign=1.0, zoom=1.5)
    bk "But..."
    show bk up at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    bk "But you, you Barbarian, win wars."
    show you neutral at Transform(xalign=0.1, yalign=1.0, zoom=1.5)
    you "What do you mean?"
    bk "The Red King cares nothing more than power."
    bk "However, because of this..."
    show bk down at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    bk "His ambition blinds him of what really matters..."
    show you smile at Transform(xalign=0.1, yalign=1.0, zoom=1.5)
    bk "Teamwork."
    show bk up at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    bk "While he simply duels with tanks..."
    show bk down at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    show you plot2 at Transform(xalign=0.0, yalign=1.0, zoom=0.6)
    bk "Such as Megaknights and the Electro Giant..."
    bk "He simply never wins with those troops alone..."
    bk "He needs support, a team that works in unison."
    show bk up at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    bk "That is why we win."
    show bk down at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    show you smile at Transform(xalign=0.0, yalign=1.0, zoom=1.5)
    bk "Not simply because of our Hog Rider..."
    bk "But from the help of troops."
    show you plot2 at Transform(xalign=0.0, yalign=1.0, zoom=0.6)
    show bk up at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    bk "The Ice Golem and Skeletons that are otherwise seen as garbage..."
    show bk down at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    bk "To the Red King, is not to us!"
    show bk up at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    bk "You are not a replacement."
    bk "You are the heart, the spark that rallies us togther..."
    you "Do you really mean it!"
    show bk down at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    bk "Now, now..."
    bk "You must focus on the battle at hand!"
    call clear
    show you fear at Transform(xalign=0.0, yalign=1.0, zoom=1.2)
    show bk down at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    you "But I must tell you something first..."
    show bk up at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    bk "What is it?"
    show you sad at Transform(xalign=0.0, yalign=1.0, zoom=1.2)
    you "To tell you the truth..."
    show bk down at Transform(xalign=1.0, yalign=1.0, zoom=1.1)
    you "I am the reason the Hog Rider is absent."
    show bk up at Transform(xalign=1.0, yalign=1.0, zoom=1.2)
    bk "What could you possibly mean?"
    show you fear at Transform(xalign=0.0, yalign=1.0, zoom=1.2)
    you "I did it."
    show you sad at Transform(xalign=0.0, yalign=1.0, zoom=1.1)
    you "The hog rider is searching for his hog at this very moment..."
    you "But the Red King has it with him..."
    you "I help steal it."
    show bk up at Transform(xalign=1.0, yalign=1.0, zoom=1.2)
    bk "How could you betray us!"
    scene black with Dissolve(0.8)
    window hide
    show text "{size=56}{color=#ffffff}To be or not to be continued...{/color}{/size}" at Transform(xalign=0.5, yalign=0.5)
    pause 5.0
    hide text
    jump start


label corn_minigame:
    show bg corngame 
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
    call clear
    return

label clear:
    window hide
    scene black with Dissolve(0.6)
    hide screen change_scene
    hide screen bye
    hide screen two_images
