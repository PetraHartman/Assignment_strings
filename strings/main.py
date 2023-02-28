# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# EK final 1988

# Part 1
Scorer_name_0 = "Ruud Gullit"
Scorer_name_1 = "Marco van Basten"
goal_0 = 32 # minutes
goal_1 = 54 # minutes 8 minutes into the second half. (blijkbaar dus minuut 54 ipv 53 volgens check)

# Who scored when?
scorers = Scorer_name_0 + " " + str(goal_0)+ ", " + Scorer_name_1 + " " + str(goal_1)
print (scorers)

# Report in full sentences.
report= Scorer_name_0 + " scored in the " + f'{goal_0}' + "nd minute" +"\n" + Scorer_name_1 + " scored in the " + f'{goal_1}' + "th minute"

print (report)

# Part 2
player = "Ruud Gullit"
first_name = player[player.find ("Ruud"):4] # Ruud
first_name_length = len (first_name) # 4
last_name = player[player.find ("G"):] # Gullit
last_name_len = len (player[player.find ("G"):]) # 6
first_letter = player[player.find ("Ruud"):1] # R
name_short = first_letter + ". " + last_name # R. Gullit


# Chant
player = "Ruud Gullit"
first_name = player [0:4]  # Ruud
first_name_excl = player [0:4] + "! " # Ruud
chant = (first_name_length - 1) * first_name_excl + first_name_excl[0:len (player [0:4]) + 1] #(4-1) * Ruud! + Ruud! = Ruud! Ruud! Ruud! Ruud!

print (chant)

chant_lengt = len (chant) # 23
last_character = chant[(chant_lengt-1)] # 23-1 omdat telling bij 0 begint. uitkomst !
good_chant = last_character != " " # uitkomst True, laatste karakter  "!" is ongelijk aan  " "

print (good_chant)

