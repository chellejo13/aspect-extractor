"""
This dictionary classifies all verbs in the corpus according to their Vendler classification (accomplishment,
achievement, activity, state, or a mixture of those depending on sentences contexts). A lot of these are accompanied by
linguistic examples that determine their classification(s).
"""

classified_verbs = {
    "abandon": "activity/achievement",  # He abandoned her for two years (act); He abandoned the ship (ach)
    "absorb": "accomplishment",  # The sponge absorbed the water in two minutes (acc)
    "abuse": "activity",  # He abused her for three years (act)
    "accept": "achievement",  # He accepted the offer (ach)
    "accuse": "activity",  # He accused her of cheating for two years (act)
    "ache": "state",  # His legs ached for a week (act)
    "acknowledge": "achievement",  # He acknowledged her presence (ach)
    "activate": "achievement/accomplishment",
    # He activated the program in two minutes (acc); He activated the program (ach)
    "add": "activity/accomplishment",
    # He added names to the list for twenty minutes (act); He added a cherry to his milkshake (ach)
    "address": "activity/achievement",
    # He addressed the question for a few minutes (act); He addressed the girl with a smile (ach)
    "adjust": "activity/achievement/accomplishment",
    # She adjusted her skirt for two minutes (act); She adjusted the price (ach); She adjusted the table's location for twenty minutes (acc)
    "admire": "activity/state",  # He admired her artwork for twenty minutes (act); I admire your work ethic (state)
    "admit": "achievement",  # He admitted to lying (ach)
    "adopt": "achievement",  # She adopted a cat (ach)
    "advertise": "activity",  # He advertised his shop on live TV for five minutes (act)
    "advise": "activity",  # The counselor advised students for an hour (act)
    "affect": "activity",  # The incident affected his family for years (act);
    "afford": "accomplishment",  # acc
    "age": "accomplishment",  # Her parents aged a lot in only two years (acc)
    "aggravate": "accomplishment",  # He aggravated the man in two minutes (acc)
    "aim": "activity",
    # She aimed her gun at the target for a minute before shooting (act); I aimed to finish the project for two years (act)
    "allow": "activity/accomplishment",
    # Her dad allowed this behavior for a week before telling her to stop (act); He allowed me back into his home in a month (acc)
    "amaze": "activity/achievement/accomplishment",
    # She amazed the judges for three minutes (act); She amazed the judges instantly (ach); She amazed the judges in only three minutes (acc)
    "amuse": "activity",  # Her antics amused her parents for the whole night (act)
    "animate": "activity",  # They animated the film for three years before releasing it (act)
    "announce": "achievement",  # They announced their engagement (ach)
    "annoy": "activity",  # My brother annoyed me for twenty years (act)
    "apologize": "activity/achievement",  # She apologized for half an hour (act); She apologized (ach)
    "apply": "activity/accomplishment",
    # She applied herself to her craft for six years (act); She applied for the job in ten minutes (acc)
    "appreciate": "state",  # I appreciate your honesty ; *I am appreciating your honesty (state)
    "approach": "activity",  # She approached him for what felt like hours before facing him (act)
    "approve": "achievement/accomplishment/state",
    # My application was approved immediately (ach); My application was approved within a week (acc); I approve of this message; *I am approving of this message (state)
    "arch": "activity/achievement",
    # The cat arched its back in fear for a few seconds (act); The cat arched its back instantly (ach)
    "argue": "activity",  # We argued about it for an hour (act)
    "arrange": "activity/accomplishment",
    # She arranged the flowers for twenty minutes (act); She arranged the bouquet in twenty minutes (acc)
    "arrest": "achievement/accomplishment",
    # The police arrested the suspect in an hour (acc); The police immediately arrested the suspect (ach)
    "ask": "activity/accomplishment",
    # She asked him questions for an hour (act); She asked him all of her questions in an hour (acc)
    "assess": "activity/accomplishment",
    # He assessed the situation for a while (act); He assessed the situation in twenty minutes (acc)
    "assume": "activity/achievement",  # I assumed the worst for a short while (act); I assumed it was over (ach)
    "assure": "activity",  # I assured him that he was safe until he calmed down (act)
    "attack": "activity/achievement/accomplishment",
    # The burglar attacked the man for five minutes before fleeing (act); She attacked my lifestyle, my family, and my character in only a minute (acc); He attacked (ach);
    "attempt": "activity/achievement",
    # He attempted the stunt for a bit before filming (act); He immediately attempted the stunt (ach)
    "attract": "accomplishment",
    # They attracted glares in only minutes (acc); His scent attracted looks for a while (activity)
    "avoid": "activity",  # We avoided each other for a few months (act);
    "awaken": "achievement",  # He awakened (ach)
    "award": "achievement",  # I awarded her with a trophy (ach)
    "achieve": "accomplishment",  # I achieved my goal in only six months (acc)
    "agree": "activity",  # I agreed with him for a while (act)
    "appear": "activity/state",
    # He appeared for a second (act); He appears to be happy; He is appearing to be happy (state)
    "arrive": "achievement",  # He arrived home (ach)
    "assemble": "accomplishment",  # He assembled the model in twenty minutes (acc)
    "attach": "accomplishment",  # He attached the thing to the other thing in x minutes (acc)

    "babble": "activity",  # She babbled at her dad for a bit (act)
    "babysit": "activity",  # I babysat my niece for seven hours (act)
    "back": "activity",  # he backed up for a while (act)
    "bail": "achievement",  # I bailed my mom out of jail (ach)
    "bait": "activity/accomplishment",  # he baited her for years (act); he baited the fishing pole in ten seconds (acc)
    "ban": "activity",  # They banned me from the local pub for six weeks (act)
    "bandage": "accomplishment",  # I bandaged my brother's arm up in a few minutes (acc)
    "banish": "activity",  # They banished me from the kingdom for six weeks (act)
    "bargain": "activity",  # I bargained with him for a whole week (act)
    "barrel": "activity",  # He barreled down the hill for a minute (act)
    "base": "achievement",  # I based the book on my own life (ach)
    "bash": "activity",  # He bashed his head into the wall for a while (act)
    "bathe": "accomplishment",  # I bathed myself for a bit (act); I bathed myself in fifteen minutes (acc)
    "battle": "activity",  # I battled my opponent for six hours (act);
    "bawl": "activity",  # I bawled for six minutes (act)
    "beam": "activity",  # The girl beamed at me for a second (act);
    "beat": "activity/accomplishment",
    # He beat his opponent in thirty seconds (acc); He beat up the teddy bear for five minutes (act)
    "beckon": "accomplishment",  # He beckoned the girl over
    "become": "achievement/accomplishment",  # He became angry in twenty seconds (acc); He became a god instantly (ach);
    "beep": "activity",  # She beeped her horn at them for a good twelve seconds (act);
    "befriend": "accomplishment",  # He befriended his neighbor in only a day (acc)
    "beg": "activity",  # I begged him to stay for the last thirty minutes (act)
    "begin": "achievement",  # He began a journey (ach)
    "behave": "activity",  # He behaved in a silly manner for the whole day (act)
    "belch": "achievement",  # She belched (ach)
    "believe": "activity/state",  # I believed in you for three years (act); *I am believing in you (state)
    "bemoan": "activity",  # She bemoaned the x for a while (Act)
    "bend": "achievement/accomplishment",  # He bent the paper in half (ach)
    "bet": "achievement",  # He bet his life on it (ach)
    "bike": "activity/accomplishment",
    # He biked around the park for a little bit (act); He biked to school in fifteen minutes (acc)
    "bitch": "activity",  # She bitched about it for a while (act); he managed to bend the metal in twelve minutes (acc)
    "blab": "activity",  # She blabbed about it for a while (act)
    "bleed": "activity/accomplishment",  # She bled for a while (act); She bled out in fifteen minutes (acc)
    "bless": "activity/accomplishment/achievement",
    # He blessed her soul for a while/in a second/instantaneously?? (act/ach/acc)
    "blind": "activity/achievement",  # He blinded her with a blindfold for a few minutes (act); He blinded her (ach)
    "blink": "achievement",  # He blinked (ach)
    "bloom": "achievement/accomplishment",  # The flower bloomed in two days (acc); the flower bloomed (ach)
    "blow": "activity/achievement",  # The wind blew for an hour (act); He blew the candle out (ach)
    "blush": "activity",  # She blushed for a little bit
    "boast": "activity",  # He boasted about his accomplishments for ten minutes (act)
    "bolt": "achievement",  # He bolted the door to the wall in only a few minutes (acc);
    "bomb": "achievement",  # they bombed the town (ach); they bombed the whole town in twenty minutes (acc)
    "bond": "activity",  # We bonded over our common interests for an hour (act)
    "boop": "achievement",  # He booped her nose (ach)
    "border": "activity/state",  # the country borders the ocean; the country is bordering the ocean (act/state)
    "borrow": "activity",  # he borrowed the book for a few days (act)
    "boss": "activity",  # he bossed her around all day (act)
    "bother": "activity",  # he bothered her all day (act)
    "box": "activity",  # they boxed for an hour (act)
    "brag": "activity",  # he bragged all day (act)
    "braid": "accomplishment",  # She braided her hair in ten minutes (Acc)
    "brake": "achievement",  # he braked (ach)
    "branch": "activity",  # he branched out for a bit (act)
    "break": "achievement",  # he broke the vase (ach)
    "breakdance": "activity",  # they breakdanced for a bit (act)
    "breathe": "activity",  # He breathed deep for three seconds (act)
    "bribe": "achievement",  # he bribed her (ach)
    "bridge": "achievement",  # the walkway bridged the gardens (ach)
    "brighten": "achievement",  # His face brightened (ach);
    "bring": "achievement",  # He brought her (ach)
    "bruise": "achievement",  # She bruised her leg (ach)
    "buck": "achievement",  # He bucked forward (ach)
    "buckle": "achievement",  # He buckled his seatbelt (ach)
    "bud": "activity/achievement",  # The flower budded
    "budge": "achievement",  # the rock budged (ach)
    "bug": "activity",  # He bugged me all day (act)
    "bulge": "activity/accomplishment/state",  #
    "bully": "activity",  # He bullied her for years (act)
    "bunch": "achievement",  # she bunched the flowers together (ach)
    "bundle": "achievement",  # They bundled the games (ach)
    "burp": "activity/achievement",  # he burped (ach); He burped for a few minutes (act)
    "burst": "achievement",  # the bubble burst (ach)
    "bust": "achievement",  # they busted through the door (ach)
    "butter": "accomplishment",  # He buttered the bread in ten seconds (acc)
    "buy": "achievement/accomplishment",  # he bought the book (acc)
    "buzz": "activity",  # the bee buzzed around for a bit (act)
    "bag": "accomplishment",  # He bagged the goods in ten minutes (acc)
    "bake": "accomplishment",  # He baked a cake in ten minutes (acc)
    "balance": "activity",  # he balanced the ball on his finger for a few minutes (act);
    "balloon": "activity",  # the pants ballooned for x minutes (Act)
    "bang": "achievement",  # He banged his head on the door (ach)
    "bark": "activity",  # He barked at the dog for five minutes (act)
    "be": "state",  # he was sad; *he is being sad (state)
    "bear": "activity",  # he bore the pain for hours (act)
    "belong": "state",  # It belonged to the sister; *It is belonging to the sister (state)
    "bite": "achievement",  # He bit me (ach)
    "blame": "achievement",  # He blamed the mistake on her (ach)
    "blast": "activity/achievement",  # He blasted the ac for hours (act); The cannon blasted (ach)
    "board": "achievement/accomplishment",  # He boarded the plane (ach); He boarded up the door in ten minutes (act)
    "bob": "activity",  # The bottle bobbed in the water for a while (act)
    "boil": "activity",  # He boiled the water for a while (act)
    "book": "achievement",  # He booked a flight (ach)
    "bounce": "activity/accomplishment",  # The ball bounced for a while (act)
    "bowl": "activity",  # he bowled for a while (act)
    "brand": "achievement",  # They branded the cow (ach)
    "brown": "activity/accomplishment",
    # He browned the meat for two minutes (act); The meat browned in two minutes (acc)
    "brush": "activity/accomplishment",  # He brushed all her hair in/for five minutes (act/acc)
    "build": "activity/accomplishment",  # He built him up for years (act); built his house in ten years (acc)
    "bump": "achievement",  # he bumped into her (ach)
    "burn": "achievement/accomplishment",  # he burned the food in ten seconds (acc); he burned his finger (ach)
    "bury": "activity/accomplishment",  # He buried the treasure for/in five minutes (act/acc)
    "button": "accomplishment",  # He buttoned up his shirt in a second (accomplishment)

    "cackle": "activity",  # She cackled for thirty minutes (act)
    "calibrate": "accomplishment",  # She calibrated her controller in two minutes (acc)
    "calm": "activity/accomplishment",
    # He calmed her down in ten minutes (acc); The waves calmed for a few minutes (act)
    "camouflage": "accomplishment",  # he camouflaged himself in two minutes (Acc)
    "camp": "activity",  # they camped for a few days (act)
    "campaign": "activity",  # she campaigned for the entire time (act)
    "capitalize": "activity",  # He capitalized on this moment for the next week (act)
    "capture": "achievement/accomplishment",  # He captured the bug in two minutes (acc); He captured a photo (ach)
    "cash": "accomplishment",  # they cashed her check in five minutes (acc)
    "cashier": "activity",  # He cashiered for his whole shift (act);
    "cast": "achievement/accomplishment",  # He cast a spell on her (ach); He cast his vote in twenty minutes (acc)
    "catalog": "activity/accomplishment",  # He cataloged the records for/in five minutes (act/acc);
    "catch": "achievement",  # He caught her (ach)
    "cause": "achievement",  # the storm caused a landslide (ach)
    "celebrate": "activity",  # she celebrated for days (act)
    "challenge": "achievement",  # he challenged her to a duel (ach)
    "chant": "activity",  # he chanted a prayer for a few days (act)
    "charm": "activity/accomplishment",  # he charmed her for some time (act); he charmed her in two days (acc)
    "chase": "activity/accomplishment",  # he chased her for a while (act); he chased her out in five minutes (acc)
    "cheat": "activity",  # he cheated on the test for the whole time (act)
    "check": "activity/achievement",  # he checked on her (ach); he checked on her for a bit (act)
    "cheer": "activity/accomplishment",  # he cheered her on for a while (act); he cheered up in no time (acc)
    "chill": "activity",  # he chilled out for a while (act)
    "chirp": "activity",  # the bird chirped for a while (act)
    "choke": "activity",  # he choked on something for a few minutes (act)
    "chomp": "achievement",  # he chomped on the wire (ach)
    "choose": "achievement",  # he chose an option (ach)
    "chop": "activity/accomplishment",  # he chopped the onions for/in five minutes (act/acc)
    "chuckle": "activity",  # he chuckled for a little bit (act)
    "churn": "activity",  # he churned butter for a bit (act)
    "circle": "activity/achievement",  # he circled the area for a bit (act); he circled the answer (ach)
    "clack": "achievement",  # he clacked his heels (ach)
    "claim": "activity/achievement",  # he claimed that he was innocent for hours (act); he claimed his reward (ach)
    "clang": "achievement",  # he clanged the bell (ach)
    "clank": "achievement",  # the pots clanked (ach)
    "clap": "activity/achievement",  # he clapped for a minute (act); he clapped (ach)
    "clean": "activity/accomplishment",  # he cleaned the apartment for/in an hour (act/acc)
    "clear": "accomplishment",  # he cleared his desk for/in an hour (act/acc)
    "click": "achievement",  # he clicked on the link (ach)
    "climb": "activity/accomplishment",  # he climbed the mountain for/in an hour (act/acc)
    "cling": "activity",  # he clung to his mom for a while
    "clip": "accomplishment",  # he clipped his nails in six minutes (acc)
    "clog": "achievement",  # he clogged the toilet (ach)
    "cluck": "achievement",  # he clucked at her (ach)
    "coax": "accomplishment",  # he coaxed her into joining in three minutes (acc)
    "collapse": "achievement",  # he collapsed (ach)
    "collect": "activity",  # he collected rent for weeks (act)
    "color": "activity",  # he colored the picture for a bit (act)
    "command": "achievement",  # he commanded her to stop (ach)
    "comment": "activity",  # he commented on her weight for years (act)
    "commit": "accomplishment",  # he committed a crime in ten minutes (acc)
    "compare": "activity",  # he compared himself to her all the time (act)
    "complain": "activity",  # he complained about her all the time (act)
    "complicate": "accomplishment",  # he complicated the process in six minutes (acc)
    "compress": "accomplishment",  # he compressed the file in six minutes (Acc)
    "compromise": "accomplishment",  # they reached a compromise in six minutes (acc)
    "conceive": "accomplishment",  # they conceived their child in six minutes (acc)
    "concentrate": "activity",  # they concentrated on work for an hour (act)
    "concern": "activity",  # this concerned him for years (act)
    "condense": "activity/accomplishment",  # he condensed the work in/for ten minutes (act/acc)
    "condition": "activity/accomplishment",  # he conditioned her for/in two years (act/acc)
    "confer": "accomplishment",  # they conferred about it for a while (act)
    "confess": "accomplishment",  # she confessed to her guilt in ten minutes (Acc)
    "confirm": "achievement",  # he confirmed his attendance (ach)
    "confuse": "achievement",  # he confused her for someone else (ach)
    "congratulate": "achievement",  # he congratulated her (ach)
    "connect": "accomplishment",  # he connected with her in two minutes (Acc)
    "consider": "activity",  # she considered her options for a while (Act)
    "consist": "achievement",  # the meal consisted of x, y, z (ach)
    "consult": "activity",  # he consulted a therapist for years (acT)
    "consume": "activity",  # he consumed alcohol all night (act)
    "contemplate": "activity",  # she contemplated it all night (act)
    "contest": "achievement",  # he contested the charges (ach)
    "contribute": "activity",  # he contributed to the project for a while (act)
    "control": "activity",  # he controlled the situation for a while (act)
    "convince": "accomplishment",  # he convinced her of his innocence in two hours (Acc)
    "coo": "activity/achievement",  # the baby cooed (act/ach)
    "cook": "accomplishment",  # she cooked a meal in one hour (acc)
    "cooperate": "activity",  # they cooperated for a while (act)
    "coordinate": "activity/accomplishment",  # she coordinated an attack in/for three months (acc/act)
    "corner": "activity",  # he cornered her for a few minutes (act)
    "counsel": "activity",  # he counseled her for years (act)
    "crack": "achievement",  # he cracked the egg (ach);
    "crackle": "activity",  # the fire crackled for a while (act)
    "cram": "activity",  # he crammed for the whole night (act)
    "cramp": "activity",  # his legs cramped for hours (act)
    "crawl": "activity",  # he crawled around for hours (act)
    "creep": "activity/achievement",  # he crept around for a while (act)
    "cremate": "accomplishment",  # they cremated her in two minutes (acc)
    "crinkle": "accomplishment",  # acc
    "crisscross": "achievement",  # she crisscrossed her legs (ach)
    "croak": "achievement",  # the frog croaked (ach)
    "crop": "accomplishment",  # he cropped the shirt in twelve minutes (acc)
    "crouch": "activity",  # she crouched for a moment (Act)
    "crown": "achievement",  # she crowned him (ach)
    "crucify": "achievement",  # she crucified him (ach)
    "cruise": "activity",  # they cruised for hours (act)
    "crumble": "accomplishment",  # the building crumbled in fifteen minutes (acc)
    "crunch": "achievement",  # ach
    "crush": "achievement",  # he crushed the bottle (ach)
    "cry": "activity",  # he cried all night (act)
    "cue": "achievement",  # he cued her to come in (ach)
    "cuff": "achievement",  # he cuffed her (ach)
    "cure": "accomplishment",  # he cured her in ten days (acc)
    "curse": "achievement",  # he cursed her (ach)
    "curtsy": "achievement",  # She curtsied (ach)
    "curve": "activity",  # act
    "cage": "achievement",  # he caged the pet (ach)
    "call": "activity",  # she called him for three hours (act)
    "cancel": "achievement",  # he canceled his plans (ach)
    "cap": "achievement",  # He capped the pen (ach)
    "care": "activity/state",  # He cared for her for years (act); I care about you; *I am caring about you (state)
    "carry": "activity",  # He carried the bag for five days (Act)
    "carve": "accomplishment",  # he carved the pumpkin in twenty minutes (acc)
    "chain": "accomplishment",  # He chained the dog to the fence in ten seconds (acc)
    "change": "achievement/accomplishment",  # He changed the song (ach); he changed his clothes in five seconds (acc)
    "charge": "activity/achievement",  # he charged his phone for five minutes (act); he charged at her (ach);
    "chew": "activity/accomplishment",
    # she chewed on the bar for five minutes (act); she chewed up x in x minutes (acc)
    "chug": "accomplishment",  # he chugged the beer in six seconds (acc)
    "clobber": "achievement",  # he clobbered her (ach)
    "close": "achievement",  # he closed the door (ach)
    "clothe": "accomplishment",  # he clothed himself in six minutes (acc)
    "clutch": "activity/achievement",  # she clutched her pearls (ach)
    "coach": "activity",  # he coached her for years (act)
    "comb": "activity",  # he combed her hair for a while (act)
    "come": "achievement",  # he came home (ach)
    "complete": "accomplishment",  # she completed her assignment in an hour (acc)
    "conduct": "activity",  # he conducted the ensemble for years (act)
    "construct": "accomplishment",  # he constructed the building in ten days (Acc)
    "contain": "achievement/accomplishment",  # the boxes contain drugs (ach); he contained the fire in five days (acc)
    "continue": "activity",  # he continued to play for years (act)
    "cool": "accomplishment",  # he cooled her down in five minutes (acc)
    "correct": "achievement",  # he corrected her posture (ach)
    "cost": "achievement",  # it costed twelve dollars (ach)
    "cough": "achievement",  # he coughed (ach)
    "count": "activity/accomplishment",  # he counted all the cards for/in twelve minutes (act/acc)
    "cover": "activity/achievement/accomplishment",
    # he covered the topic for/in a week (act/acc); he covered himself (ach)
    "crash": "achievement",  # he crashed his car (ach);
    "create": "accomplishment",  # he created an avatar in six minutes (acc)
    "cross": "achievement",  # he crossed the street (ach)
    "crowd": "activity",  # they crowded around him for a bit (Act)
    "cuddle": "activity",  # they cuddled for hours (Act)
    "curl": "activity/accomplishment",  # she curled her hair in/for twenty minutes (act/acc)
    "cut": "achievement/accomplishment",  # he cut the cake (ach)

    "damage": "achievement/accomplishment",
    # The crash damaged both vehicles instantly (ach); He damaged his vocal cords in only a few minutes (acc)
    "dangle": "activity",  # She dangled the key above her head for a minute (act)
    "dash": "activity/accomplishment",
    # We dashed down the street for a few minutes (act); We dashed through the crowd in a few minutes (acc)
    "dawn": "achievement",  # It dawned on him (ach)
    "deactivate": "achievement/accomplishment",
    # She deactivated her phone in one minute (acc); She deactivated her phone (ach)
    "deal": "accomplishment",  # The dealer dealt the hand in only a few seconds (acc)
    "debate": "activity",  # They debated for hours (act)
    "deceive": "activity/achievement/accomplishment",
    # She deceived him for years (act); In two minutes, she deceived him (acc); She instantly deceived him (ach)
    "declare": "achievement",  # The congressman declared his resignation (ach)
    "decorate": "activity/accomplishment",
    # She decorated the cake for four hours (act); She decorated the cake in four hours (acc)
    "dedicate": "achievement",  # She dedicated the song to a friend (ach)
    "defeat": "accomplishment/achievement",
    # She defeated the boss in thirty minutes (acc); She defeated him instantly (ach)
    "defend": "activity/achievement",  # He defended his post for two hours (act);
    "define": "activity/accomplishment",
    # She defined the rules for a while (act); She defined all the terms in a few minutes (acc)
    "deflate": "accomplishment",  # The balloon deflated in a minute (acc)
    "defrost": "activity/accomplishment",
    # I defrosted the meat for a few hours (act); The meat defrosted in a few hours (acc)
    "dehydrate": "activity/accomplishment",
    # I dehydrated some fruit for a few hours (act); The fruit dehydrated in a few hours (acc)
    "delete": "achievement/accomplishment",
    # She deleted all her photos in two minutes (acc); She deleted her account instantly (ach)
    "deliver": "accomplishment",  # They delivered the food in twenty minutes (acc)
    "demand": "activity",  # She demanded to be compensated for twenty minutes (act)
    "demonstrate": "activity/accomplishment",
    # She demonstrated her knowledge for twenty minutes (act); She demonstrated her knowledge in twenty minutes (acc)
    "deny": "activity/achievement/accomplishment",
    # She denied any involvement for twenty minutes (act); She denied the request in twenty minutes (acc); She denied the request instantly (ach)
    "descend": "activity",  # He descended the stairs for two minutes (act)
    "describe": "activity/accomplishment",
    # She described her work for a few minutes (act); She described her role in two minutes (acc)
    "deserve": "state",  # She deserves something nice; * She is deserving something nice (state)
    "destroy": "accomplishment",  # He destroyed the vase in two seconds (acc);
    "detach": "accomplishment",  # He detached the hook from the string in one minute (acc)
    "determine": "achievement/accomplishment",
    # He determined the result in one minute (acc); He determined the result instantly
    "devastate": "activity",  # The news devastated her family for years (act)
    "devote": "act",  # He devoted himself to his religion for years (act)
    "diet": "activity",  # They dieted for only a week (act)
    "differ": "state",  # I differ from him; *I am differing from him (state)
    "digest": "accomplishment",  # She digested her food in one hour (accomplishment)
    "dillydally": "activity",  # She dillydallied on her phone for the whole time (act)
    "dilute": "activity/accomplishment",
    # He diluted the solution with water for twelve minutes; He diluted the solution with water in twelve minutes (acc)
    "dip": "activity",  # He dipped his finger into the pool for a second (act)
    "direct": "activity",  # She directed the band for a few years (act)
    "disagree": "activity",  # They disagreed on that topic for a few years (act)
    "disconnect": "achievement",  # She disconnected the cord from the TV (ach)
    "discourage": "activity",  # He discouraged her from seeing him for a while (act)
    "discuss": "activity",  # They discussed the issue for a while (act)
    "disguise": "accomplishment",  # He disguised himself in two seconds (acc);
    "disgust": "activity",  # The smell disgusted her for years (act)
    "dislike": "state",  # She dislikes that song; *She is disliking that song (state)
    "dismiss": "achievement",  # He dismissed the class (ach)
    "disobey": "activity",  # She disobeyed her mother for years (act)
    "disperse": "achievement",  # The department dispersed decisions all at once (ach)
    "dispute": "activity",  # They disputed over the charges for a week (act)
    "disrupt": "activity",  # She disrupted the class for six minutes (act)
    "dissolve": "accomplishment",  # The tablet dissolved in six minutes (acc)
    "distract": "activity",  # She distracted him for a few minutes (act)
    "ditch": "activity",  # He ditched class for a few weeks (act)
    "dive": "achievement",  # She dove into the pool (ach)
    "divide": "accomplishment",  # She divided them all up in six minutes (acc)
    "divorce": "achievement",  # They divorced (ach)
    "divvy": "activity/accomplishment",  # She divvied them all up in six minutes (acc)
    "dock": "accomplishment",  # They docked the boat in a few minutes (acc)
    "dodge": "achievement",  # She dodged the bullet instantly (ach)
    "don": "accomplishment",  # He donned his uniform in a few minutes (acc)
    "donate": "achievement/accomplishment",  # She donated food (in six minutes) (ach/acc)
    "dot": "activity",  # Wet spots of rain dotted his shirt for a few minutes (act)
    "drain": "accomplishment",  # She drained the tub in a few minutes (acc)
    "drape": "accomplishment",  # He draped the cape over his chair (acc)
    "drench": "activity/accomplishment",  # The rain drenched his back for/in twenty minutes (act/acc)
    "drift": "activity",  # The boat drifted away for a few minutes (act)
    "drizzle": "activity",  # She drizzled some syrup over his pancakes for a second (act)
    "drug": "achievement",  # He drugged the girl (ach)
    "drum": "activity",  # He drummed for a whole hour (act)
    "duck": "achievement",  # He ducked under the table (ach)
    "dye": "activity/accomplishment",  # He dyed all her hair for/in two hours (act/acc)
    "dance": "activity",  # they danced for the whole night (act)
    "decide": "achievement",  # they decided where to go (ach)
    "depend": "activity",  # I depended on my mom for years (act)
    "design": "activity/accomplishment",  # I designed this layout for/in ten days (act/acc)
    "desire": "state",  # I desired a new pen; *I am desiring a new pen (state)
    "develop": "accomplishment",  # He developed the game in ten days (acc)
    "dial": "achievement",  # he dialed the number (ach)
    "die": "achievement",  # he died (ach)
    "dig": "activity/accomplishment",  # he dug a hole for/in six hours (act/acc)
    "dim": "achievement",  # he dimmed the lights (ach)
    "dine": "activity",  # they dined for hours (activity)
    "dirty": "accomplishment",  # she dirtied the dish in five minutes (acc)
    "disappear": "achievement",  # she disappeared (ach)
    "disappoint": "activity",  # she disappointed him for years (act)
    "discover": "achievement",  # he discovered the truth (ach)
    "disturb": "activity",  # he disturbed her for years (act)
    "do": "activity",  # he did things for x time (act)
    "drag": "activity",  # he dragged the shovel around for x time (act)
    "draw": "activity/accomplishment",  # he drew a picture of her for/in x time (act/acc)
    "dream": "activity/state",  # he dreamed for five hours (act)
    "dress": "accomplishment",  # she dressed herself in seven minutes (Acc)
    "dribble": "activity",  # he dribbled the ball around for x time (act)
    "drill": "accomplishment",  # he drilled all the screws in in x time (acc)
    "drink": "activity/accomplishment",  # he drank a glass of water for/in x time (act/acc)
    "drip": "activity",  # the water dripped for a while (act)
    "drive": "activity/accomplishment",  # he drove around/home for/in x time (act/acc)
    "drool": "activity",  # he drooled all night (act)
    "drop": "achievement",  # he dropped the ball (ach)
    "drown": "accomplishment",  # he drowned in five minutes (acc)
    "dry": "accomplishment",  # he dried off in five minutes (acc)
    "dump": "achievement",  # he dumped water into the lake (ach)
    "dunk": "achievement",  # he dunked the cookie in some milk (ach)
    "dust": "activity/accomplishment",  # he dusted the shelf off for/in x time (act/acc)

    "earn": "achievement",  # he earned his allowance (ach)
    "ease": "activity/accomplishment",  # she eased his pain for/in a few hours (act/acc)
    "echo": "activity",  # he echoed her sentiments for a few minutes (act)
    "edit": "activity",  # he edited his video for hours (act)
    "educate": "accomplishment",  # he educated her on history in/for three months (act/acc)
    "elaborate": "activity",  # he elaborated for hours (act)
    "electrocute": "achievement",  # she electrocuted herself (Ach)
    "eliminate": "accomplishment",  # he eliminated his competition in three weeks (acc)
    "embarrass": "activity/accomplishment",  # he embarrassed his sister for/in weeks (act/acc)
    "encourage": "activity",  # he encouraged her for a while (act)
    "end": "achievement",  # he ended the game (ach)
    "engrave": "accomplishment",  # he engraved the stone in ten minutes (acc)
    "enhance": "accomplishment",  # he enhanced the image
    "enjoy": "activity/state",  # He enjoyed his toys for a while (act)
    "erase": "accomplishment",  # he erased the drawing in three seconds (acc)
    "erupt": "activity/achievement",  # the volcano erupted for a few minutes (act); it erupted into flames (ach)
    "escape": "accomplishment",  # he escaped the room in five minutes (acc);
    "escort": "activity/accomplishment",
    # he escorted her around the town for five minutes (act) He escorted her to her room in five minutes (acc)
    "evaluate": "activity",  # He evaluated her for the day (act)
    "evaporate": "accomplishment",  # the water evaporated in three hours (acc)
    "examine": "activity",  # he examined her for a while (act)
    "exasperate": "activity",  # he exasperated me all day (act)
    "exchange": "activity/achievement",  # he exchanged pleasantries with her (act/ach)
    "exclaim": "achievement",  # he exclaimed (ach)
    "exert": "activity",  # he exerted his energy all day (act)
    "exhaust": "activity",  # he exhausted himself all day (act)
    "exit": "achievement",  # he exited the building (ach)
    "expect": "activity/state",  # he expects more; *he is expecting more (state)
    "explain": "activity/accomplishment",
    # he explained himself for a while (act); he explained the issue in ten minutes (acc)
    "explore": "activity/accomplishment",  # he explored the town for/in the day (act/acc)
    "expose": "achievement",  # he exposed the lie (ach)
    "express": "activity",  # he expressed remorse for a while (act)
    "extend": "achievement",  # he extended his arm (ach)
    "eat": "activity/accomplishment",  # he ate for a while (act); he ate a burger in five minutes (acc)
    "empty": "accomplishment",  # he emptied the can in two seconds (acc)
    "enlarge": "achievement",  # he enlarged the image (ach)
    "enter": "achievement",  # he entered the store (ach)
    "excite": "achievement/accomplishment",  # he excited her (ach); he excited him in two minutes (Acc)
    "excuse": "achievement",  # he excused himself (ach)
    "exercise": "activity",  # he exercised for a few minutes (act)
    "exist": "activity",  # it existed for a few years (act)
    "explode": "achievement",  # it exploded (ach)

    "fabricate": "accomplishment",  # he fabricated a story in six minutes (acc)
    "face": "activity",  # he faced her for five minutes (act)
    "fade": "accomplishment",  # the figure faded into the distance in six seconds (acc)
    "faint": "achievement",  # he fainted (ach)
    "fake": "achievement",  # he faked excitement
    "fan": "activity",  # she fanned the flames for five minutes (act)
    "fare": "activity",  # he fared well for a bit (act)
    "fart": "achievement",  # he farted (ach)
    "fascinate": "activity",  # he fascinated her for a while (act)
    "fast": "activity",  # he fasted for a week (act)
    "fatten": "accomplishment",  # he fattened up in a few months (acc)
    "favor": "achievement",  # he favored his dad (ach)
    "fawn": "activity",  # he fawned over her for hours (act)
    "fear": "activity/state",  # he feared for her life; *I am fearing for my life (state)
    "feature": "state",  # the game featured a lot;
    "feel": "activity/state",  # he felt nice; *I am feeling nice (state)
    "fell": "achievement",  # he fell down the stairs (ach)
    "ferment": "activity",  # she fermented the cabbage for a few months (act)
    "fertilize": "accomplishment",  # they fertilized the plants in six minutes (Acc)
    "fetch": "achievement",  # he fetched a bottle (ach)
    "fib": "activity",  # he fibbed for a week (act)
    "fiddle": "activity",  # he fiddled with it for a while (Act)
    "finish": "accomplishment",  # he finished the puzzle in a week (Acc)
    "fish": "activity",  # he fished for an hour (act)
    "fit": "accomplishment",  # acc
    "fix": "accomplishment",  # he fixed the car in five minutes (acc)
    "fizz": "activity",  # the soda fizzed for a while (act)
    "flag": "achievement",  # he flagged a car down (ach)
    "flap": "activity",  # he flapped his wings for a while (Act)
    "flatten": "achievement",  # he flattened the dough (ach
    "flatter": "accomplishment",  # he flattered her in a few moments (acc)
    "flavor": "achievement",  # he flavored the sauce (ach)
    "flick": "achievement",  # he flicked her forehead (ach)
    "fling": "achievement",  # he flung a towel over his shoulder (ach)
    "flip": "achievement",  # he flipped over (ach)
    "flirt": "activity",  # he flirted with her for a while (act)
    "flitter": "activity",  # act
    "float": "activity",  # he floated in the ocean for a while (act)
    "flood": "accomplishment",  # the river flooded in ten minutes (Acc)
    "flop": "activity",  # the fish flopped around for a bit (Act)
    "floss": "activity",  # he flossed his teeth for a bit (Act)
    "flow": "activity",  # the water flowed down the river for a moment (act)
    "fluff": "activity",  # he fluffed his pillow for a second (act)
    "flunk": "achievement",  # he flunked his classes (ach)
    "flush": "achievement",  # he flushed the toilet (ach)
    "fly": "activity/accomplishment",
    # he flew the plane for five hours (act); he flew to california in five hours (acc)
    "focus": "activity",  # he focused on work for hours (act)
    "force": "achievement",  # he forced me to get out (ach)
    "forget": "activity/achievement/state",
    # he forgot to call her back for a week (act); he forgot all his lines in five minutes (acc); he forgot to pay his rent (ach)
    "forgive": "achievement",  # he forgave her (ach)
    "form": "accomplishment",  # they formed a bond in two days (acc)
    "frame": "achievement/accomplishment",  # he framed the guy (ach); he framed the photo in five minutes (acc)
    "free": "accomplishment",  # he freed the bug from the cage in five seconds (acc)
    "freshen": "accomplishment",  # he freshened up for a few minutes (acc)
    "frost": "accomplishment",  # he frosted the cake for five minutes (Acc)
    "frown": "achievement",  # he frowned (Ach)
    "frustrate": "activity",  # he frustrated her all day (act)
    "fund": "activity/accomplishment",  # he funded the project for/in many years (act/acc)
    "fuss": "activity",  # he fussed over her all day (act)
    "fail": "achievement",  # he failed the test (ach);
    "fall": "achievement",  # he fell down (ach)
    "fasten": "achievement",  # he fastened his seatbelt (ach)
    "feed": "achievement",  # he fed his cat (ach)
    "fight": "activity",  # he fought with her for hours (act)
    "figure": "achievement/accomplishment",
    # he figured that it would take a while (ach); he figured it out in ten minutes (Acc)
    "fill": "accomplishment",  # he filled the glass in two seconds (acc)
    "find": "achievement",  # he found a sticker (ach)
    "flash": "achievement",  # he flashed his high beams at her (ach)
    "fold": "accomplishment",  # he folded his clothes for/in ten minutes (act/acc)
    "follow": "activity",  # he followed her for five minutes (act)
    "fool": "activity",  # he fooled her for years (act)
    "forbid": "activity",  # he forbade her from leaving for years (act)
    "freeze": "achievement/accomplishment",  # he froze in place (ach); the meat froze in six hours (acc)
    "frighten": "achievement",  # he frightened her (ach)

    "gain": "accomplishment",  # I gained a new friend in one hour (acc)
    "gallop": "activity/accomplishment",  # I galloped for a while (act); He galloped home in six minutes (acc)
    "gargle": "activity",  # He gargled water for six seconds (act)
    "gas": "accomplishment",  # They gassed the car in a few minutes (Acc)
    "gasp": "activity/achievement",  # He gasped for air for a while (act); he gasped in shock (ach)
    "gather": "activity/accomplishment",  # he gathered the materials for/in ten minutes (act/acc)
    "gaze": "activity",  # I gazed at her for a while (act)
    "gear": "accomplishment",  # He geared up for his journey
    "generalize": "activity",  # act
    "get": "achievement",  # he got a new dog (ach)
    "giggle": "activity",  # We giggled for so long (act)
    "glance": "achievement",  # he glanced at her (ach)
    "glide": "activity/accomplishment",  # we glided away for/in six hours (act/acc)
    "glisten": "activity",  # The rock glistened for a while (act)
    "gloop": "achievement",  # He glooped something onto her plate (ach)
    "glow": "activity",  # The phone glowed for five minutes (act)
    "glug": "activity",  # The water glugged for a few moments (act)
    "gnaw": "activity",  # He gnawed at the cages of his enclosure for six hours (act)
    "gobble": "accomplishment",  # She gobbled everything up in five minutes (acc)
    "goof": "activity",  # He goofed off for the whole day (act)
    "grace": "achievement/accomplishment",  # She graced me with her presence (ach/acc)
    "grasp": "activity/achievement",  # He grasped at straws for ten minutes (act); He grasped her hand (ach)
    "grease": "accomplishment",  # He greased the whole pan for/in a moment (act/acc)
    "greet": "achievement",  # he greeted his mom (ach)
    "grill": "activity/accomplishment",  # he grilled the meat for/in six hours (act/acc)
    "grin": "activity",  # He grinned at her for two minutes (act)
    "grind": "activity/accomplishment",  # He ground the coffee beans for/in five minutes (act/acc)
    "gross": "activity/accomplishment",
    # He grossed fifty million yen in ten weeks (acc); He grossed her out for so long (act)
    "ground": "activity/accomplishment",
    # He ground the coffee for a few minutes (act); He ground all the coffee in ten minutes (acc)
    "group": "accomplishment",  # He grouped them all by hair color in ten minutes (acc)
    "grow": "activity/accomplishment",
    # The tree grew for ten years (act); The tree grew so tall in only three years (acc)
    "grumble": "activity",  # He grumbled about the food for ten minutes (act)
    "guard": "activity",  # he guarded the post for an hour (act)
    "guide": "accomplishment",
    # he guided them around town for an hour (act); he guided them to their hotel in twenty minutes (acc)
    "gulp": "achievement",  # She gulped in fear (ach)
    "gurgle": "activity",  # His stomach gurgled for a second (act)
    "gush": "activity",
    # He gushed about her achievements for a while (act); Blood gushed out of his wound for a few minutes (act)
    "give": "activity/achievement",  # He gave them a show for five minutes (act); He gave her a gift (ach)
    "glue": "accomplishment",  # He glued the pieces together in six minutes (acc)
    "go": "activity",  # We went to the party for five minutes (act)
    "grab": "achievement",  # He grabbed his hand (ach)
    "growl": "activity",
    # My stomach growled for a minute straight (act); My dog growled at the squirrel for a second (act)
    "guess": "achievement",  # He guessed the answer correctly (ach)

    "halt": "achievement",  # The bus halted at the stop sign (ach)
    "handle": "accomplishment",  # He handled the situation
    "happen": "accomplishment",  # acc
    "harp": "activity",  # He harped on about it for ten minutes (act)
    "haunt": "activity",  # The vision haunted him for years (act)
    "head": "achievement",  # I headed to school (ach)
    "heal": "accomplishment",  # His wound healed in ten days (acc)
    "heat": "activity/accomplishment",
    # He heated up his lunch for a few minutes (act); They heated the entire house up in thirty minutes (acc)
    "heave": "achievement",  # ach
    "herd": "activity/accomplishment",
    # The dog herded the sheep towards the barn for a few minutes (act); The dog herded all the sheep into the barn in five minutes (acc)
    "hibernate": "activity",  # The bear hibernated in a cave for a few months (act)
    "hiccup": "activity",  # The baby hiccuped for five minutes (acc)
    "hike": "activity/accomplishment",
    # I hiked around the mountain for a few days (act); He hiked the entire park in six days (acc)
    "hoe": "activity",  # He hoed the soil for a while (act)
    "hog": "activity",  # He hogged the blanket all night (act);
    "hoist": "accomplishment",  # He hoisted the baby onto the counter (acc)
    "holler": "activity",  # She hollered and hooted for a good five minutes (act)
    "honk": "activity",  # I honked my horn at him for at least ten seconds (act)
    "hoot": "activity",  # She hooted and hollered for a good five minutes (act)
    "hop": "activity/accomplishment",
    # The bunny hopped around for a bit (act); The bunny hopped home in six minutes (acc)
    "hope": "activity/state",
    # She hoped for his return for years (act); I hope he comes back; *I am hoping he comes back (state)
    "horrify": "achievement",  # His tattoo horrified her (ach)
    "hose": "activity",  # She hosed her car down for five minutes (act)
    "howl": "activity",  # The dog howled at the moon all night (act)
    "huff": "activity",  # He huffed and puffed at the door all night (act)
    "hurl": "achievement",  # He hurled the ball at her face (ach)
    "hush": "achievement",  # The crowd hushed as the lights dimmed (ach)
    "hypnotize": "accomplishment",  # She hypnotized the man in two minutes (acc)
    "hand": "achievement/accomplishment",  # He handed me the key (ach); He handed her the
    "hang": "activity/achievement",
    # He hung from the monkey bars for two minutes (act); He hung his keys on the hook (ach)
    "harvest": "accomplishment",  # She harvested all the fruit in an hour (acc)
    "hatch": "achievement/accomplishment",  # He hatched a plan in six minutes (acc);
    "hate": "activity/state",  # I hated this game for years (act); I hate this game; *I am hating this game (state)
    "have": "activity/state",  # I had this game for years (act); I have this game; *I am having this game (state)
    "hear": "achievement",  # He heard his name (ach);
    "help": "activity/achievement",  # He helped her out for a while (act); He helped her up (ach)
    "hide": "activity/achievement/accomplishment",
    # He hid under the covers for five minutes (act); He hid his embarrassment (ach); He completely hid his mess in a few minutes (acc)
    "hit": "achievement",  # He hit the ball with the bat (ach)
    "hold": "activity/state",
    # She held him to a high standard for years (act); She held the baby for twenty minutes (act);
    "hook": "achievement",  # He hooked his arm around her neck (ach)
    "hug": "activity",  # She hugged her for five minutes (act);
    "hum": "activity",  # He hummed a tune for a little while (act);
    "hunt": "activity",  # He hunted deer for years (act)
    "hurry": "achievement",  # He hurried home (ach)
    "hurt": "achievement",  # He hurt his arm (ach)

    "ignore": "activity",  # I ignored the signs for a while (act)
    "imitate": "activity",  # He imitated a bird call for a bit (act)
    "impress": "accomplishment",  # I impressed him with my skills in only two minutes (acc)
    "incapacitate": "accomplishment",  # She incapacitated them all in two minutes (acc)
    "increase": "achievement",  # he increased the difficulty (ach)
    "indent": "achievement",  # She indented the paragraph (ach)
    "indicate": "achievement",  # He indicated that he was unhappy (ach)
    "induce": "accomplishment",  # She induced labor in ten minutes (acc)
    "infect": "achievement",  # She infected him instantly (ach)
    "inform": "activity/accomplishment",  # She informed me of her feelings in/for three minutes (act/acc)
    "inhale": "activity",  # he inhaled for three seconds (act);
    "injure": "achievement",  # He injured his foot (ach)
    "instigate": "accomplishment",  # he instigated a reign of terror
    "instruct": "activity",  # She instructed them on their roles for twenty minutes (act)
    "intend": "activity/state",
    # I intended on doing it for a few years (act); I intend to play the flute; *I am intending to play the flute (state)
    "intensify": "activity",  # The music intensified for a few measures (act)
    "interact": "activity",  # I interacted with him for an hour (act)
    "intercept": "achievement/accomplishment",
    # I intercepted the ball (ach); They intercepted the operation in twenty minutes (acc)
    "interest": "activity",  # The thought of it interested her for a bit (act)
    "interfere": "activity",  # I interfered with their ploy for the entire time (act)
    "interject": "achievement",  # he interjected (ach)
    "interpret": "activity",  # he interpreted the results for a few minutes (act)
    "interrupt": "activity/achievement",
    # He interrupted their conversation for ten minutes (act); He interrupted the game (ach)
    "interview": "activity",  # He interviewed her for five minutes (act)
    "intimate": "activity",  # He intimated that he would not be coming (act)
    "intrigue": "act",  # The thought intrigued him for a while (act)
    "introduce": "achievement",  # He introduced his mom to him (ach)
    "invade": "state",  # He invaded my space (ach)
    "invent": "accomplishment",  # He invented the device in a night (acc)
    "invest": "accomplishment",  # She invested in her future for years (act)
    "investigate": "activity",  # He investigated the issue for a few weeks (act);
    "involve": "activity",  # He involved himself with them for a year (act)
    "itch": "activity",  # The bump itched for a long time (act)
    "identify": "achievement",  # He identified the girl as his daughter (ach)
    "imagine": "activity",  # She imagined their future together for a bit (act)
    "include": "achievement",  # She included him in the conversation (ach)
    "inherit": "achievement/accomplishment",
    # She inherited her mother's freckles (ach); her grandmother's heirlooms in a day (acc)
    "insist": "activity",  # She insisted on staying for so long (act)
    "invite": "achievement",  # SHe invited her sister to the party (ach)
    "iron": "accomplishment",  # He ironed his shirt in ten minutes (acc)

    "jab": "achievement",  # He jabbed his fork into the food (ach)
    "jam": "activity/achievement",  # We jammed together for five hours (act); He jammed his foot into the wall (ach)
    "jerk": "achievement",  # He jerked his arm away from them (ach)
    "jiggle": "activity",  # The jello jiggled for a little as he moved it onto the plate (act)
    "join": "achievement",  # We joined the club (ach)
    "judge": "activity",  # He judged them for years (act)
    "jog": "activity/accomplishment",  # We jogged around the park (act); We jogged home in ten minutes (acc)
    "joke": "activity",  # We joked around for hours (act)
    "juggle": "activity",  # He juggled the fruits for five minutes (act)
    "jump": "activity",  # We jumped for five minutes (act)

    "keel": "achievement",  # He keeled over (ach)
    "kidnap": "accomplishment",  # He kidnapped her in ten minutes (acc)
    "knead": "activity",  # The cat kneaded the pillow for ten minutes (act)
    "keep": "activity/state",
    # He kept a diary for ten years (act); I keep losing the game ; *I am keeping losing the game (state)
    "kick": "achievement",  # He kicked the ball for a while (act)
    "kid": "activity",  # act
    "kill": "achievement/accomplishment",  # He killed him in ten minutes (acc); He killed him (ach)
    "kiss": "activity/achievement",  # They kissed for ten seconds (act); He kissed her once (ach)
    "kneel": "activity",  # She kneeled down for a bit (act)
    "knit": "activity/accomplishment",
    # She knitted a sweater for three days (act); She knitted a sweater for him in three days (acc)
    "knock": "activity/achievement",
    # He knocked on the door for eight seconds (act); He knocked the glass off the table (ach)
    "knot": "accomplishment",  # He knotted the ropes together in three minutes (acc)
    "know": "state",  # I know my rights; *I am knowing my rights (state)

    "label": "achievement",  # he labeled the box (ach)
    "land": "achievement",  # he landed the plane (ach)
    "lap": "activity/accomplishment",  # he lapped up the water for/in six minutes (act/acc)
    "lasso": "achievement",  # he lassoed something (ach)
    "laugh": "activity",  # he laughed for hours (act)
    "launch": "achievement",  # he launched the rocket (ach)
    "lay": "activity",  # he laid down for hours (act)
    "lead": "activity",  # he led them through the town for hours (Act)
    "leak": "activity",  # the water leaked for a while (act)
    "leap": "achievement",  # he leaped into her arms (ach)
    "learn": "accomplishment",  # he learned to read in ten months (acc)
    "leave": "accomplishment",  # he left for a few week (act)
    "lend": "activity",  # he lent a hand to her for a while (Act)
    "let": "activity",  # he let him in for five weeks (act)
    "liberate": "achievement",  # he liberated them (Ach)
    "lick": "activity",  # he licked the lollipop for x time (act)
    "lie": "activity",  # he lied for years (act)
    "lift": "activity/achievement",  # he lifted weights for hours (act); he lifted her (ach)
    "lighten": "accomplishment",  # he lightened up in time (Acc)
    "limit": "activity",  # he limited his caffeine intake for a week (act)
    "limp": "activity",  # he limped for a week (Act)
    "linger": "activity",  # he lingered there for a while (act)
    "link": "accomplishment",  # acc
    "list": "activity/accomplishment",  # he listed his qualms for/in a while (act/acc)
    "live": "activity",  # he lived there for years (act)
    "load": "activity/accomplishment",  # he loaded the truck for/in five minutes (act/ach)
    "loan": "activity",  # he loaned her his book for five years (act)
    "locate": "achievement",  # he located the missing piece (ach)
    "log": "activity",  # he logged his notes in the book for a while (act)
    "loop": "activity",  # act
    "loosen": "achievement",  # he loosened his tie (ach)
    "lose": "achievement",  # he lost the game (ach)
    "love": "activity/state",  # he loves it; *he is loving it (act/state)
    "lower": "achievement",  # he lowered the box (ach)
    "lug": "activity/accomplishment",  # he lugged the box into the house for/in ten minutes (activity/accomplishment)
    "lump": "accomplishment",  # he lumped them in with everyone else in x minutes (acc)
    "lurch": "achievement",  # he lurched forward (ach)
    "lack": "activity",  # I lacked empathy for a while (act)
    "last": "activity",  # the game lasted for five hours (act)
    "lean": "activity",  # I leaned against the pole for a while (act)
    "light": "achievement",  # I lit the candle (ach)
    "like": "state",  # I like to play; *I am liking to play (state)
    "listen": "activity",  # He listened to her for a while (act)
    "look": "activity/state",
    # He looked for her for a while (act); He looks like a dog; *He is looking like a dog (state)
    "lock": "achievement",  # He locked the door (ach)

    "magnetize": "achievement",  # (ach)
    "magnify": "achievement",  # she magnified the lens (achievement)
    "mail": "achievement",  # he mailed her a letter (ach)
    "maintain": "activity",  # he maintained a calm demeanor for a while (act)
    "make": "accomplishment",  # he made a cake in ten hours (acc)
    "mangle": "accomplishment",  # he mangled the corpse for x hours (acc)
    "marry": "accomplishment",  # he married her in x hours (acc)
    "master": "accomplishment",  # he mastered the craft in x hours (acc)
    "match": "achievement",  # he matched with her (ach)
    "mate": "activity",  # he mated with her for x time (act)
    "mature": "accomplishment",  # he matured  in x years (acc)
    "mean": "activity/state",  # he meant well for x years (act); *I am meaning well (state)
    "measure": "accomplishment",  # I measured the door in x minutes (acc)
    "meet": "activity",  # I met the doctor for x time (act)
    "memorize": "accomplishment",  # I memorized the poem in x time (acc)
    "mend": "accomplishment",  # I mended the stitch in x time (acc)
    "mention": "achievement",  # I mentioned the issue to him (ach)
    "mesmerize": "activity/accomplishment",  # I mesmerized him for/in x time (act/acc)
    "message": "achievement",  # I messaged him (ach)
    "mind": "activity",  # I minded my business for x time (act);
    "mirror": "activity",  # I mirrored his movements for x time (act)
    "misbehave": "activity",  # I misbehaved for x time (act)
    "misinform": "activity",  # He misinformed me for x time (act)
    "misname": "achievement",  # He misnamed him (ach)
    "miss": "activity/state",  # he missed her for a long time (act); *I am missing her
    "misstate": "achievement",  # He misstated his claim (ach)
    "mistake": "achievement",  # he mistook her for someone else (ach)
    "misunderstand": "activity",  # he misunderstood me for years (act)
    "mock": "activity",  # he mocked me all day (Act)
    "model": "activity",  # he modeled for the whole day (Act)
    "mop": "activity/accomplishment",  # he mopped the whole floor for/in x time (act/acc)
    "mow": "activity/accomplishment",  # she mowed the whole lawn for/in x time (act/acc)
    "mug": "accomplishment",  # he mugged her in x time (acc)
    "mumble": "activity",  # he mumbled all day (act)
    "munch": "activity",  # he munched on snacks all day (act)
    "mush": "activity",  # he mushed his food all day (act)
    "mutter": "activity",  # he muttered all day (act)
    "manage": "accomplishment",  # he managed to leave in ten minutes (acc)
    "manufacture": "accomplishment",  # he manufactured the product in ten years (Acc)
    "march": "activity",  # he marched all day (act)
    "mash": "accomplishment",  # he mashed the potatoes in x time (acc)
    "melt": "accomplishment",  # he melted the cheese in x time (acc)
    "mess": "activity/achievement",  # he messed around all day (act); he messed up the routine (ach)
    "milk": "activity",  # he milked the cow for a few minutes (act)
    "mix": "activity/accomplishment",  # he mixed the batter for a few seconds (act)
    "move": "activity/accomplishment",  # he moved around all day (act)/ me moved into a new house in ten hours (acc)
    "murder": "achievement",  # he murdered him (ach)

    "nail": "achievement",  # She nailed the
    "name": "achievement",  # He named her (ach)
    "nap": "activity",  # He napped for an hour (act)
    "narrow": "activity",  # She narrowed down her choices in a
    "need": "state",  # I need a new charger; *I am needing a new charger (state)
    "negotiate": "activity",  # He negotiated with her for the entire night (act)
    "nibble": "activity",  # He nibbled the cheese for twenty minutes (act)
    "nip": "achievement",  # He nipped it in the bud (ach)
    "nod": "activity/achievement",  # He nodded at her for a while (act)
    "note": "achievement",  # He noted the change in his file (ach)
    "notice": "achievement",  # He noticed the change (ach)
    "nudge": "activity",  # He nudged her with his elbow for a little while (act)

    "obsess": "activity",  # she obsessed over them for years (act)
    "obey": "activity",  # She obeyed the rules for a long time (act)
    "oblige": "activity",  # He obliged
    "observe": "activity",  # He observed her movements for a bit (act)
    "occupy": "activity",  # He occupied the room for twenty minutes (act)
    "occur": "achievement",  # The event occurred last Monday (ach)
    "offer": "achievement",  # He offered to take her home (ach)
    "oink": "achievement",  # He oinked at her (ach)
    "open": "achievement/accomplishment",  # He opened his eyes (ach); He opened the present in a few minutes (acc)
    "operate": "activity",  # He operated the machine for twenty minutes (act);
    "oppose": "activity",  # She opposed his policies for three years (act)
    "oppress": "activity",  # They oppressed the group for three years (act)
    "order": "activity/accomplishment",
    # They ordered the pizza in 2 minutes (acc); She ordered him around for all his life (act)
    "organize": "accomplishment",  # He organized a vigil in six minutes (acc)
    "overcome": "accomplishment",  # she overcame her fears in six minutes (acc)
    "overcook": "accomplishment",  # she overcooked the meat in six minutes (Acc)
    "overdo": "achievement",  # she overdid it (ach)
    "overeat": "achievement",  # she overate (ach)
    "overflow": "activity",  # the bathtub overflowed for a while (activity)
    "overhear": "achievement",  # he overheard her (ach)
    "overlap": "achievement",  # their schedules overlapped (ach)
    "overload": "accomplishment",  # acc
    "overwhelm": "accomplishment",  # he overwhelmed her in six minutes (Acc)
    "owe": "activity",  # he owed money for six years (act)
    "own": "activity",  # He owned a car for five years (act)

    "package": "activity/accomplishment",  # he packaged the gifts for/in an hour (act/Acc)
    "paddle": "activity",  # he paddled around for a while (act)
    "paint": "activity/accomplishment",  # he painted the ima ge for/in ten hours (act/acc)
    "pair": "achievement",  # he paired up with someone (ach)
    "panic": "achievement",  # he panicked (ach)
    "pant": "activity",  # he panted for a while (act)
    "parade": "activity",  # he paraded it around all day (act)
    "paralyze": "achievement",  # he paralyzed her (ach)
    "pardon": "achievement",  # he pardoned him (ach)
    "part": "achievement",  # he parted his hair (ach)
    "party": "activity",  # he partied all night (act)
    "pass": "achievement",  # he passed her a spoon (ach)
    "paste": "achievement",  # he pasted the sticker on his hand (ach)
    "patch": "accomplishment",  # he patched up the rip in minutes (acc)
    "pause": "achievement",  # he paused (ach)
    "peak": "achievement",  # he peaked in high school (ach)
    "peck": "activity",  # he pecked at the stump for a while (act)
    "pedal": "activity",  # he pedaled for a while (act)
    "pee": "achievement",  # he peed (ach)
    "peek": "activity",  # he peeked outside for a moment (act)
    "peel": "activity/achievement",  # he peeled the banana for a while (Act); he peeled the sticker off (ach)
    "penalize": "achievement",  # he penalized her (ach)
    "penetrate": "achievement",  # the sword penetrated his stomach (ach)
    "perch": "activity",  # he perched on the ledge for a while (act)
    "perfect": "accomplishment",  # he perfected his craft in a month (acc)
    "perm": " accomplishment",  # she permed his hair in three hours (Acc)
    "persuade": "accomplishment",  # she persuaded him in three hours (acc)
    "pet": "activity",  # I pet him for a while (act)
    "petition": "achievement",  # I petitioned (ach)
    "phone": "activity",  # I phoned my mom for an hour (act)
    "pick": "achievement",  # I picked up the phone (ach)
    "pile": "activity",  # he piled the papers up for a bit (Act)
    "pitch": "achievement",  # he pitched the ball to her (ach)
    "pity": "activity",  # he pitied her for years (act)
    "place": "achievement",  # he placed the pan on the table (ach)
    "plan": "activity",  # he planned for years (act)
    "plate": "accomplishments",  # he plated the dinner in a few minutes (acc)
    "plead": "activity",  # he pleaded for a while (act)
    "please": "activity",  # They pleased him for a while (act)
    "pledge": "achievement",  # He pledged to follow the rules (ach)
    "plop": "achievement",  # he plopped on the floor (ach)
    "plot": "activity",  # he plotted for a while (act)
    "plug": "achievement",  # he plugged the device in (ach)
    "plunge": "achievement",  # he plunged into the water (ach)
    "poach": "accomplishment",  # they poached their staff in a week (acc)
    "poison": "achievement",  # he poisoned her (ach)
    "poke": "achievement",  # he poked (ach)
    "police": "activity",  # they policed the area for years (acT)
    "polish": "activity/accomplishment",  # he polished the whole table for/in x time (act/acc)
    "poll": "accomplishment",  # he polled them
    "poo": "achievement",  # he pooed (ach)
    "poop": "achievement",  # he pooped (ach)
    "pop": "achievement",  # the balloon popped (ach)
    "pose": "achievement",  # he posed (ach)
    "pounce": "achievement",  # he pounced on the bird (ach)
    "pound": "activity",  # he pounded the pavement for x time (act)
    "pour": "activity",  # he poured the water into the glass for x time (act)
    "pout": "achievement",  # she pouted (ach)
    "powder": "activity",  # he powdered his nose for a while (act)
    "power": "accomplishment",  # he powered the device in x time (acc)
    "praise": "activity",  # he praised her for a while (act)
    "prance": "activity",  # he pranced around for a while (act)
    "pray": "activity",  # he prayed for my downfall for a long time (Act)
    "predict": "accomplishment",  # he predicted the outcome in six minutes (Acc)
    "pressure": "activity",  # he pressured her for a long time (act)
    "presume": "state",  # state
    "prick": "achievement",  # She pricked her finger (ach)
    "prime": "activity",  # she primed him for a while (act)
    "program": "accomplishment",  # he programmed the software in x time (acc)
    "progress": "activity",  # he progressed for a long time (act)
    "prohibit": "activity",  # he prohibited them for years (act)
    "promise": "achievement",  # he promised (ach)
    "pronounce": "achievement",  # she pronounced his name wrong (ach)
    "propel": "activity",  # he propelled forward for a while (Act)
    "protect": "activity",  # he protected them for a long time (act)
    "protest": "activity",  # he protested this for a while (act)
    "prove": "accomplishment",  # he proved them wrong in x time (Acc)
    "provide": "accomplishment",  # he provided them with a
    "pry": "activity",  # he pried for a while (Act)
    "publicize": "accomplishment",  # he publicized the news in x time (acc)
    "publish": "accomplishment",  # he published the news in x time (Acc)
    "pucker": "achievement",  # he puckered his lips (ach)
    "puke": "activity",  # he puked for a while (act)
    "puree": "accomplishment",  # he pureed the fruit in a few minute (acc)
    "purr": "activity",  # he purred for a few minutes (act)
    "pack": "accomplishment",  # he packed a bag in x time (acc)
    "park": "achievement",  # he parked his car (ach)
    "pat": "activity",  # he patted himself dry for a bit (act)
    "pay": "activity/achievement",  # he paid her for three years (act)
    "peep": "achievement",  # he peeped (Ach)
    "perk": "state",  # he perked up at the sight of him (achievement)
    "perform": "activity",  # she performed for x time (act)
    "pin": "achievement",  # she pinned the tail (ach)
    "pinch": "achievement",  # she pinched herself (ach)
    "plant": "activity/accomplishment",  # she planted trees for/in x time (act/acc)
    "play": "activity",  # he played for hours (act)
    "point": "achievement",  # he pointed at me (ach)
    "possess": "activity",  # he possessed a warrant for x time (activity)
    "practice": "activity",  # he practiced for x time (act)
    "prefer": "state",  # he prefers x; *I am preferring x (state)
    "prepare": "activity/accomplishment",  # he prepared for/in x time (act/acc)
    "press": "achievement",  # he pressed the button (ach)
    "pretend": "activity/state",  # he pretended for a long time (act)
    "print": "accomplishment",  # he printed the story in x time (acc)
    "pull": "accomplishment",  # she pulled him out in x time (acc)
    "pump": "activity",  # he pumped gas for x time (act)
    "punch": "achievement",  # he punched her (ach)
    "punish": "achievement",  # he punished her (ach)
    "push": "achievement",  # he pushed her (ach)
    "put": "achievement",  # he put it on a plate (ach)

    "quack": "achievement",  # he quacked at her (ach)
    "qualify": "activity",  # he qualified for it for years (act)
    "quarter": "accomplishment",  # he quartered the cake in six minutes (acc)
    "question": "activity",  # he questioned her for hours (Act)
    "quiet": "accomplishment",  # he quieted her in six minutes (Acc)
    "quit": "achievement",  # he quit his job (ach)
    "quote": "achievement",  # he quoted the book (ach)

    "race": "activity",  # act
    "raid": "activity",  # act
    "rain": "activity",  # act
    "raise": "activity",  # act
    "rake": "activity/accomplishment",  # act/acc
    "ram": "achievement",  # ach
    "ramble": "activity",  # act
    "rate": "achievement",  # ach
    "rationalize": "activity",  # act
    "rave": "activity",  # act
    "reach": "achievement",  # ach
    "react": "achievement",  # ach
    "read": "activity",  # act
    "readjust": "accomplishment",  # acc
    "rearrange": "accomplishment",  # acc
    "reason": "activity",  # act
    "rebuild": "accomplishment",  # acc
    "recall": "achievement",  # ach
    "receive": "achievement",  # ach
    "recharge": "accomplishment",  # acc
    "reckon": "activity",  # act
    "recommend": "achievement",  # ach
    "reconstruct": "accomplishment",  # acc
    "record": "activity",  # act
    "recover": "accomplishment",  # acc
    "redirect": "achievement",  # ach
    "rediscover": "accomplishment",  # acc
    "redo": "accomplishment",  # acc
    "reel": "activity",  # act
    "refer": "achievement",  # ach
    "reflect": "activity",  # act
    "refresh": "accomplishment",  # acc
    "refuse": "achievement",  # ach
    "register": "accomplishment",  # acc
    "regret": "activity/state",  # act
    "regroup": "accomplishment",  # acc
    "reject": "achievement",  # ach
    "relate": "activity",  # act
    "relax": "activity",  # act
    "release": "achievement",  # ach
    "rely": "activity",  # act
    "remain": "activity",  # act
    "remember": "activity",  # act
    "remind": "achievement",  # ach
    "remove": "accomplishment",  # acc
    "renew": "accomplishment",  # acc
    "renovate": "activity/accomplishment",  # act/acc
    "rent": "activity",  # act
    "repay": "accomplishment",  # acc
    "repeat": "activity",  # act
    "repel": "achievement",  # ach
    "replace": "accomplishment",  # acc
    "replay": "achievement",  # ach
    "reply": "achievement",  # ach
    "report": "achievement",  # ach
    "repot": "accomplishment",  # acc
    "represent": "activity",  # act
    "require": "state",  # activity
    "rescue": "accomplishment",  # acc
    "resign": "achievement",  # ach
    "resist": "activity",  # act
    "resolve": "accomplishment",  # acc
    "respond": "achievement",  # ach
    "restrain": "activity",  # act
    "retake": "accomplishment",  # acc
    "retell": "accomplishment",  # acc
    "retreat": "activity/accomplishment",  # act/acc
    "retrieve": "accomplishment",  # acc
    "revel": "activity",  # act
    "revolt": "activity",  # act
    "rewind": "activity",  # act
    "rewrite": "activity/accomplishment",  # act/acc
    "rhyme": "activity",  # act
    "rid": "accomplishment",  # acc
    "ride": "activity",  # act
    "ring": "achievement",  # ach
    "rinse": "activity/accomplishment",  # act/acc
    "rip": "achievement",  # ach
    "ripen": "accomplishment",  # acc
    "risk": "activity",  # act
    "roar": "achievement",  # ach
    "roast": "accomplishment",  # acc
    "rope": "accomplishment",  # acc
    "rot": "accomplishment",  # acc
    "rouse": "accomplishment",  # acc
    "rove": "activity",  # act
    "rule": "activity",  # act
    "rush": "activity",  # act
    "rust": "accomplishment",  # acc
    "rustle": "activity",  # act
    "realize": "achievement",  # ach
    "recognize": "achievement",  # ach
    "recuperate": "accomplishment",  # acc
    "reheat": "accomplishment",  # acc
    "remodel": "accomplishment",  # ac
    "repair": "accomplishment",  # acc
    "resemble": "activity/state",  # act
    "rest": "activity",  # act
    "retire": "accomplishment",  # acc
    "reverse": "activity/achievement",  # act/ach
    "rise": "achievement/accomplishment",  # ach/acc
    "rock": "activity",  # act
    "roll": "activity",  # act
    "row": "activity",  # act
    "rub": "activity",  # act
    "ruin": "accomplishment",  # acc
    "run": "activity",  # act

    "salute": "achievement",  # ach
    "sample": "activity",  # She sampled the product for a week (act)
    "sashay": "activity",  # act
    "satisfy": "accomplishment",  # I satisfied my craving for ice cream in three minutes (acc)
    "save": "activity/achievement",  # I saved him (ach); I saved the leftovers for a few days (act)
    "say": "activity",  # She said her piece for a whole hour (act)
    "scald": "achievement",  # ach
    "scatter": "activity/accomplishment",
    # She scattered the seeds for an hour (act); She scattered all the seeds in an hour (acc)
    "scold": "activity",  # He scolded her for an hour (act)
    "scooch": "achievement",  # He scooched over (ach)
    "scoop": "achievement",  # I scooped some ice cream for myself (ach)
    "scoot": "achievement",  # I scooted over (ach)
    "scramble": "activity/accomplishment",
    # He scrambled the tiles for a bit (act); He scrambled the tiles in a minute (accomplishment)
    "scrap": "achievement",  # He scrapped the idea (ach)
    "scratch": "activity/achievement",  # I scratched my back for a little bit (act); The cat scratched me (ach)
    "scream": "activity",  # I screamed at her for three hours (act);
    "screech": "achievement",  # He screeched at the top of his lungs for five seconds (act)
    "scrub": "activity",  # He scrubbed the floors for about an hour (act)
    "scrunch": "activity",  # He scrunched his nose in disgust for a second (act)
    "scurry": "activity",  # She scurried around for a while (act)
    "scuttle": "activity",  # He scuttled around for a bit (act)
    "search": "activity",  # He searched for his phone for hours (act)
    "season": "accomplishment",  # He seasoned the chicken in ten minutes (acc)
    "section": "activity/accomplishment",
    # She sectioned her hair for a few minutes (act); She sectioned all of her hair in ten minutes (acc)
    "sense": "activity",  # She sensed his presence for a moment (act)
    "separate": "activity/accomplishment",
    # He separated her from him in a second (acc); He separated them for a while (act)
    "sever": "accomplishment",  # acc
    "shame": "activity",  # He shamed her for ten minutes (act)
    "shampoo": "activity/accomplishment",  # She shampooed her hair for/in five minutes (act/acc);
    "shatter": "achievement",  # The glass shattered (ach)
    "shed": "activity/accomplishment",  # act/acc
    "shift": "activity",  # act
    "shiver": "activity",  # He shivered all night (act)
    "shock": "achievement",  # He shocked her (ach)
    "shoulder": "activity",  # he shouldered the burden for years (act)
    "shred": "accomplishment",  # They shredded the paper in two
    "shriek": "achievement",  # She shrieked
    "shrink": "achievement/accomplishment",  # The clothes shrank in twenty minutes (acc)
    "shrivel": "accomplishment",  # The flower shriveled up in x minutes (acc)
    "shrug": "achievement",  # She shrugged" (ach)
    "shuffle": "activity",  # She shuffled around for a few minutes (act)
    "shush": "accomplishment",  # acc
    "sift": "activity",  # act
    "sigh": "achievement",  # ach
    "sin": "achievement",  # he sinned (ach)
    "sing": "activity",  # she sang for a while (act)
    "single": "achievement",  # he singled her out (ach)
    "sip": "activity/achievement",  # he sipped on his coffee for twenty minutes (act); he sipped his tea (ach)
    "sire": "accomplishment",  # he sired three girls in two years (acc)
    "sit": "activity",  # he sat there for ten minutes (act)
    "size": "accomplishment",  # acc
    "ski": "activity",  # he skied all morning (act)
    "skim": "activity/accomplishment",  # he skimmed through the whole book for/in five hours (act/acc)
    "slack": "activity",  # he slacked off all day (act)
    "slam": "achievement",  # he slammed the door (ach)
    "slap": "achievement",  # he slapped her (ach)
    "slash": "achievement/accomplishment",  # he slashed her tire (ach); he slashed all her tires in ten minutes (acc)
    "sled": "activity",  # act
    "sleepwalk": "activity",  # act
    "slice": "accomplishment",  # acc
    "slink": "activity",  # act
    "slither": "activity",  # act
    "slouch": "activity",  # act
    "smear": "activity",  # act
    "smirk": "achievement",  # ach
    "smother": "accomplishment",  # act
    "smush": "achievement",  # ach
    "snack": "activity",  # act
    "snarl": "activity",  # act
    "snatch": "achievement",  # ach
    "sneer": "activity",  # act
    "sniffle": "activity",  # act
    "snip": "activity",  # act
    "snoop": "activity",  # act
    "snore": "activity",  # act
    "snort": "achievement",  # ach
    "snuggle": "activity",  # act
    "soak": "activity",  # act
    "soar": "activity",  # act
    "sob": "activity",  # act
    "solicit": "activity",  # act
    "soothe": "accomplishment",  # acc
    "sop": "activity",  # act
    "sort": "activity/accomplishment",  # act/acc
    "sow": "accomplishment",  # acc
    "spackle": "accomplishment",  # acc
    "sparkle": "activity",  # act
    "specialize": "activity",  # act
    "specify": "achievement",  # ach
    "speed": "activity",  # act
    "spike": "achievement",  # ach
    "spin": "activity",  # act
    "splinter": "achievement",  # ach
    "spoil": "accomplishment",  # acc
    "sponge": "activity",  # act
    "spook": "accomplishment",  # acc
    "spoon": "accomplishment",  # acc
    "spout": "activity",  # act
    "sprawl": "activity",  # act
    "spray": "activity/accomplishment",  # act/acc
    "spring": "activity",  # act
    "sprinkle": "activity",  # act
    "sputter": "activity",  # act
    "squawk": "activity",  # act
    "squint": "activity",  # act
    "squirt": "activity",  # act
    "stab": "achievement",  # he stabbed her (ach)
    "stack": "activity",  # act
    "stagger": "activity",  # act
    "stalk": "activity",  # he stalked her for years (act)
    "stall": "activity",  # she stalled for a while (act)
    "staple": "achievement/accomplishment",
    # He stapled the papers together (ach); He stapled all the papers in x minutes (acc)
    "stare": "activity",  # he stared at her for six minutes (act)
    "startle": "achievement",  # She startled him (ach)
    "stash": "achievement",  # He stashed the money in his pocket (ach)
    "state": "accomplishment",  # He stated his feelings in a few minutes (acc)
    "steady": "accomplishment",  # He steadied the glass (acc)
    "steam": "activity",  # He steamed the clothes for a bit (act); He steamed all the clothes in x minutes (acc)
    "steer": "activity",  # He steered the around for a while (act)
    "stem": "achievement",  # The problem stemmed from x (ach)
    "stencil": "activity/accomplishment",  # He stenciled the tattoo for a bit
    "stew": "activity",  # he stewed the potatoes for ten minutes (act)
    "sting": "achievement",  # the bee stung him (ach)
    "stink": "activity",  # the garbage stunk for a while (act)
    "stitch": "accomplishment",  # he stitched the fabrics together in x minutes (acc)
    "stomp": "activity/achievement",  # He stomped his foot on the ground (ach); He stomped home (act)
    "stoop": "activity",  # He stooped down to her level for a while (act)
    "store": "activity",  # He stored them in the closet for years (act)
    "strain": "activity",  # act
    "stress": "activity/accomplishment",
    # He stressed his sister out in a few seconds (acc); He stressed out about it for hours (act)
    "strip": "accomplishment",  # She stripped the paint from the wall in x minutes (acc)
    "strive": "activity",  # He strove to be better for years (act)
    "stroll": "activity/accomplishment",
    # he strolled around the park for a while (act); He strolled home in ten minutes (acc)
    "structure": "accomplishment",  # He structured his day around the tour (acc)
    "struggle": "activity",  # He struggled for a while (act)
    "stuff": "accomplishment",  # He stuffed all his clothes into the bag in six minutes (acc)
    "stumble": "achievement",  # He stumbled over (ach)
    "stump": "activity",  # The problem stumped him for a while (act)
    "stun": "achievement",  # He stunned her (ach)
    "stutter": "activity",  # He stuttered for a bit (act)
    "style": "accomplishment",  # She styled the woman in ten minutes (acc)
    "subject": "activity",  # He subjected her to torture for years (act)
    "submit": "achievement",  # He submitted his thesis (ach)
    "substitute": "activity",  # act
    "subtract": "accomplishment",  # She subtracted
    "suck": "activity",  # act
    "suffer": "activity",  # act
    "suffocate": "accomplishment",  # acc
    "suggest": "achievement",  # ach
    "suit": "activity",  # act
    "sunburn": "accomplishment",  # acc
    "supervise": "activity",  # act
    "supplement": "activity",  # act
    "support": "activity",  # act
    "surprise": "achievement",  # ach
    "surround": "accomplishment",  # acc
    "survey": "activity",  # act
    "survive": "activity",  # act
    "suspect": "activity",  # act
    "suspend": "activity",  # act
    "swat": "achievement",  # ach
    "sway": "activity",  # act
    "swear": "achievement",  # ach
    "sweat": "activity",  # act
    "sweeten": "accomplishment",  # acc
    "swipe": "achievement",  # ach
    "swirl": "activity",  # act
    "swish": "activity",  # act
    "switch": "accomplishment",  # acc
    "swoop": "achievement",  # ach
    "sail": "activity/accomplishment",  # act/acc
    "scare": "achievement",  # ach
    "score": "achievement",  # ach
    "scrape": "achievement",  # ach
    "screw": "activity",  # act
    "scribble": "activity",  # act
    "sculpt": "activity/accomplishment",  # act/acc
    "seal": "accomplishment",  # acc
    "see": "achievement",  # ach
    "seek": "activity",  # act
    "seem": "state",  # state
    "sell": "accomplishment",  # acc
    "send": "achievement",  # ach
    "serve": "achievement",  # achievement
    "set": "achievement/accomplishment",  # ach/acc
    "settle": "accomplishment",  # acc
    "sew": "activity",  # act
    "shake": "activity",  # act
    "shape": "activity/accomplishment",  # act/acc
    "share": "activity/accomplishment",  # act/acc
    "sharpen": "activity/accomplishment",  # act/acc
    "shave": "activity",  # acc
    "shine": "activity/accomplishment",  # act/acc
    "ship": "accomplishment",  # acc
    "shoot": "achievement",  # ach
    "shop": "activity",  # act
    "shout": "activity",  # act
    "shove": "achievement",  # ach
    "shovel": "activity/accomplishment",  # act/acc
    "show": "activity",  # act
    "shut": "achievement",  # ach
    "sink": "activity/accomplishment",  # act/acc
    "skip": "activity/achievement",  # act/ach
    "skate": "activity",  # act
    "sleep": "activity",  # act
    "slide": "activity",  # act
    "slip": "achievement",  # ach
    "smack": "achievement",  # ach
    "smash": "achievement",  # ach
    "smell": "activity/state",  # activity/state
    "smile": "activity",  # act
    "smoke": "activity",  # act
    "smooth": "activity/accomplishment",  # act/acc
    "snap": "achievement",  # ach
    "sneak": "activity",  # act
    "sneeze": "achievement",  # ach
    "sniff": "activity",  # act
    "snow": "activity",  # act
    "snowball": "activity",  # act
    "solve": "accomplishment",  # acc
    "sound": "accomplishment/state",  # acc/state
    "spank": "achievement",  # ach
    "speak": "activity",  # act
    "spell": "accomplishment",  # acc
    "spend": "accomplishment",  # acc
    "spill": "achievement",  # ach
    "spit": "achievement",  # ach
    "splash": "achievement",  # ach
    "split": "accomplishment",  # acc
    "spot": "achievement",  # ach
    "spread": "achievement",  # ach
    "spy": "activity",  # act
    "squash": "squash",  # ach
    "squeak": "achievement",  # ach
    "squeal": "achievement",  # ach
    "squeeze": "activity",  # act
    "squish": "achievement",  # ach
    "stain": "achievement",  # ach
    "stamp": "achievement",  # ach
    "stand": "activity/achievement",  # act/ach
    "start": "achievement",  # ach
    "starve": "activity",  # act
    "stay": "activity",  # act
    "steal": "accomplishment",  # acc
    "step": "achievement",  # ach
    "stick": "activity/achievement",  # act/ach
    "stir": "activity",  # act
    "stop": "achievement",  # ach
    "straighten": "accomplishment",  # acc
    "stretch": "activity",  # act
    "strike": "achievement",  # ach
    "study": "activity",  # act
    "suppose": "state",  # state
    "swallow": "achievement",  # ach
    "sweep": "activity/accomplishment",  # act/acc
    "swim": "activity/accomplishment",  # acc/act
    "swing": "activity",  # act

    "tag": "achievement",  # ach
    "take": "achievement",  # he took a photo (ach);
    "tap": "activity",  # she tapped her foot for an hour (act)
    "taperecord": "activity",  # he taperecorded her for an hour (act)
    "taste": "achievement",  # he tasted the broth (ach)
    "tattoo": "activity/accomplishment",  # he tattooed her back for/in an hour (act/acc)
    "tax": "activity",  # act
    "teeter": "activity",  # the ball teetered for a while (act)
    "teethe": "activity",  # she teethed for a long time (act)
    "tell": "activity",  # he told her his feelings for a while (act)
    "tempt": "activity",  # he tempted her for years (act)
    "tend": "activity",  # he tended to her wounds for a while (act)
    "terrify": "achievement",  # he terrified her (ach)
    "terrorize": "activity",  # he terrorized her for years (act)
    "test": "activity",  # he tested her for an hour (act)
    "thaw": "activity/accomplishment",  # the meat thawed for/in an hour (act)
    "think": "activity",  # (act)
    "thud": "achievement",  # (ach)
    "thump": "achievement",  # (ach)
    "tick": "activity",  # the clock ticked for x time (act)
    "tidy": "activity/accomplishment",  # (act/acc)
    "tile": "activity/accomplishment",  # (act/acc)
    "tilt": "achievement",  # (ach)
    "time": "activity",  # (act)
    "tingle": "activity",  # (act)
    "tinkle": "activity",  # (act)
    "tiptoe": "activity",  # (act)
    "toast": "achievement",  # (ach)
    "tone": "accomplishment",  # (acc)
    "toot": "achievement",  # (ach)
    "topple": "accomplishment",  # (Acc)
    "torture": "activity",  # (act)
    "toss": "achievement",  # (ach)
    "total": "achievement",  # (ach)
    "tow": "accomplishment",  # (acc)
    "trace": "activity",  # (act)
    "track": "activity",  # (act)
    "trail": "activity",  # (act)
    "transcribe": "activity/accomplishment",  # (act/acc)
    "transfer": "achievement",  # (ach)
    "transform": "accomplishment",  # (acc)
    "translate": "activity/accomplishment",  # (Act/acc)
    "transmit": "activity",  # (act)
    "trap": "accomplishment",  # acc
    "treat": "achievement",  # ach
    "trigger": "achievement",  # ach
    "triple": "achievement",  # achievement
    "trot": "activity/accomplishment",  # act/acc
    "trust": "activity/state",  # I trusted you for years (act); I trust you; *I am trusting you (state)
    "tuck": "achievement",  # she tucked him into bed (ach)
    "tug": "activity",  # he tugged at the rope for hours (act)
    "tune": "activity/accomplishment",  # he tuned the violin for/in a minute (act/acc)
    "tunnel": "accomplishment",  # acc
    "twirl": "activity",  # he twirled around for hours (act)
    "talk": "activity",  # he talked to her for hours (act)
    "tangle": "accomplishment",  # he tangled the cords up in five minutes (acc)
    "tape": "activity",  # he taped her for a while (act)
    "teach": "activity/accomplishment",  # he taught her Spanish for/in six years (act/acc)
    "tear": "achievement",  # she tore a ligament (ach);
    "tease": "activity",  # he teased her all day (act)
    "thank": "achievement",  # he thanked her (ach)
    "threaten": "activity/achievement",  # he threatened her for years (act/ach)
    "thrill": "achievement",  # the movie thrilled her (ach)
    "throw": "achievement",  # he threw the ball (ach)
    "tickle": "activity",  # he tickled her for hours (act)
    "tie": "accomplishment",  # he tied her shoes in six seconds (acc)
    "tighten": "achievement",  # he tightened the lid (ach)
    "tip": "achievement",  # he tipped her (ach)
    "tire": "accomplishment",  # he tired her out in five minutes (acc)
    "top": "accomplishment",  # acc
    "touch": "achievement",  # he touched the floor (ach)
    "trade": "ach",  # he traded cards with her (ach)
    "train": "activity",  # he trained for years (act)
    "trick": "achievement",  # he tricked her (ach)
    "trip": "achievement",  # he tripped over a rock (ach)
    "try": "activity",  # he tried for many years (act)
    "tumble": "achievement",  # he tumbled down the stairs (ach)
    "turn": "achievement",  # he turned around (ach)
    "twinkle": "achievement",  # his eyes twinkled (ach)
    "twist": "achievement",  # she twisted the cap off (ach)
    "type": "activity/accomplishment",  # he typed a letter for/in five minutes (act/acc)

    "unbuckle": "achievement",  # He unbuckled his seatbelt (ach)
    "unbutton": "achievement/accomplishment",  # He unbuttoned his shirt in a minute (acc)
    "uncover": "accomplishment",  # He uncovered the secret in ten minutes (acc)
    "uncross": "achievement",  # She uncrossed her legs (ach)
    "underestimate": "activity",  # He underestimated his power for years (act)
    "underline": "accomplishment",  # He underlined the word in two seconds (acc)
    "understand": "accomplishment",  # He understood the assigment in a few minutes (acc)
    "undo": "accomplishment",  # He undid the knot in ten seconds (acc)
    "undress": "accomplishment",  # She undressed in five minutes (acc)
    "unhook": "achievement",  # he unhooked the towel from the door knob (ach)
    "unite": "accomplishment",  # they united the couple in marriage (acc)
    "unload": "accomplishment",  # He unloaded the truck in five minutes (acc)
    "unlock": "achievement",  # he unlocked the door (ach)
    "unpack": "activity",  # He unpacked his bag in two minutes (acc)
    "unplug": "achievement",  # She unplugged the tv (ach)
    "unscrew": "accomplishment",  # He unscrewed the screw for a few seconds (acc)
    "untie": "accomplishment",  # She untied her shoes in a few seconds (acc)
    "unwind": "activity/accomplishment",  # He unwound the cord in ten seconds (acc)
    "unwrap": "accomplishment",  # She unwrapped the present in ten seconds (acc)
    "unzip": "accomplishment",  # She unzipped her dress in a second (acc)
    "upgrade": "accomplishment",  # She upgraded her phone in a day (acc)
    "upset": "accomplishment",  # He upset her in two minutes (Acc)
    "urge": "activity",  # He urged her to play with him for years (act)
    "urinate": "activity",  # He urinated for a few minutes (act)
    "utter": "achievement",  # she uttered a response (ach)
    "untangle": "accomplishment",  # she untangled her wires in a few minutes (acc)
    "use": "activity/accomplishment",  # she used up her allowance in a day (acc); She used it for years (act)

    "vacuum": "activity/accomplishment",
    # He vacuumed for a few minutes (act); He vacuumed the floors in thirty minutes (acc)
    "vanish": "achievement",  # He vanished into thin air (ach)
    "vanquish": "accomplishment",  # He vanquished the beast in twenty minutes (acc)
    "verbalize": "activity/accomplishment",
    # He verbalized his feelings for a few minutes (act); He verbalized his feelings in two minutes (acc)
    "videotape": "activity",  # He videotaped his sister for a few minutes (act)
    "visualize": "activity",  # He visualized her for a few minutes (act)
    "visit": "activity",  # He visited his mom for a few days (act)
    "voice": "activity;accomplishment",
    # He voiced his opinion for a few minutes (act); He voiced all of his thoughts in a minute (acc)
    "volunteer": "activity",  # He volunteered at the shelter for three years (act)
    "vomit": "activity",  # He vomited for a solid minute (activity)
    "vote": "achievement",  # I voted for him (ach)
    "vow": "achievement",  # I vowed to protect him (ach)

    "waddle": "activity/accomplishment",  # he waddled for a while (act); he waddled home in five minutes (acc)
    "wade": "activity",  # He waded out for a while (act)
    "wag": "activity",  # He wagged his tail for so long (act)
    "wail": "activity",  # He wailed for a while (act)
    "wallop": "accomplishment",  # He walloped he
    "wander": "activity/accomplishment",  # he wandered for a while (act); he wandered home in five minutes (acc)
    "warn": "activity",  # He warned him about it for five minutes (act)
    "waste": "activity",  # He wasted his time for seven minutes
    "water": "activity/accomplishment",
    # She watered the flowers for a bit (act); she watered all the flowers in six minutes (acc)
    "weaken": "accomplishment",  # His powered weakened in a few months (acc)
    "weed": "activity",  # She weeded the garden for a while (act)
    "weep": "activity",  # She wept for a while (act)
    "weigh": "activity",  # She weighed herself for a minute (act)
    "whack": "accomplishment",  # He whacked his brother
    "wheeze": "activity",  # he wheezed for a while (act)
    "whimper": "activity",  # she whimpered for a while (act)
    "whine": "activity",  # she whined about the issue for so long (act)
    "whisk": "activity",  # she whisked the batter for a few minutes (act)
    "whisper": "activity",  # she whispered to him for a few moments (act)
    "wilt": "accomplishment",  # the flowers wilted in only a week (acc)
    "wink": "activity",  # She winked at him for a few minutes (act)
    "wire": "accomplishment",  # He wired the tv to the console in a few minutes (acc)
    "wither": "accomplishment",  # the plant withered in only a few days (acc)
    "wobble": "activity",  # The table wobbled for a second (act)
    "worry": "activity",  # She worried about him for a long time (act)
    "wound": "achievement",  # He wounded his arm
    "wrestle": "activity",  # He wrestled with his brother for a few minutes (act)
    "wriggle": "activity/accomplishment",
    # He wriggled around for a few seconds (act); He wriggled out of the hole in two seconds (acc)
    "wrinkle": "accomplishment",  # She wrinkled her clothes
    "wait": "activity",  # I waited for six hours (act);
    "wake": "achievement",  # I woke my brother up (ach)
    "walk": "activity/accomplishment",  # I walked to the store for/in six minutes (act/acc)
    "want": "state",  # She wants to go home; *She is wanting to go home (state)
    "warm": "activity/accomplishment",  # He warmed the bottle for six minutes
    "wash": "activity/accomplishment",  # She washed her car for/in an hour (act/acc)
    "watch": "activity",  # She watched him play for three hours (act)
    "wave": "activity",  # He waved at her for a second (act)
    "wear": "activity",  # She wore a cape for a few minutes (act)
    "whirl": "activity",  # The merry-go-round whirled for a few minutes (act)
    "whistle": "activity",  # She whistled for a few minutes (act)
    "wiggle": "activity/accomplishment",
    # She wiggled around for a few minutes (act); She wiggled out of his arms in a few seconds (acc)
    "win": "achievement",  # She won the race (ach)
    "wind": "activity/accomplishment",  # He wound the clock for/in a few minutes (act/acc)
    "wipe": "activity/accomplishment",
    # She wiped the table for a few minutes (act); She wiped the table clean in two seconds (acc);
    "wish": "activity",  # I wished for good health for years (act)
    "wonder": "activity",  # I wondered where he was for years (act)
    "work": "activity",  # He worked the for eight years (act)
    "wrap": "accomplishment",  # She wrapped her hair with a towel in seconds (acc)
    "wreck": "achievement/accomplishment",  # The blast wrecked 100 houses in seconds (acc/ach)
    "write": "activity/accomplishment",  # She wrote a poem for/in three minutes (act/acc)

    "yank": "achievement",  # She yanked the candy from his hands (ach)
    "yawn": "activity",  # She yawned for a moment (act)
    "yearn": "activity",  # He yearned for her for years (act)
    "yell": "activity",  # She yelled at him for hours (act)

    "zap": "achievement",  # ach
    "zip": "accomplishment",  # acc
    "zoom": "activity",  # act
}