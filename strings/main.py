# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# EK final 1988

# Part 1
scorer_name_0 = "Ruud Gullit"
scorer_name_1 = "Marco van Basten"
goal_0 = 32 # minutes
goal_1 = 54 # minutes 8 minutes into the second half. (blijkbaar dus minuut 54 ipv 53 volgens check)

# Who scored when?
scorers = scorer_name_0 + " " + str(goal_0)+ ", " + scorer_name_1 + " " + str(goal_1)
print (scorers)

# Report in full sentences.
report = f"{scorer_name_0} scored in the {goal_0}nd minute\n{scorer_name_1} scored in the {goal_1}th minute"
print (report)


# Part 2
player = "Ruud Gullit"
index_space= player.find(" ")
first_name = player[:index_space] # Ruud
first_name_length = len (first_name) # 4
last_name = player[index_space+1:] # Gullit
last_name_len = len (last_name) # 6
first_letter = first_name[:1] # R
name_short = first_letter + ". " + last_name # R. Gullit


# Chant
first_name_exclamation = first_name + "! " # Ruud
chant = (first_name_length - 1) * (first_name + "! ") + first_name + "!"
print (chant)

chant_lengt = len (chant) # 23
last_character = chant[(chant_lengt-1)] # 23-1 omdat telling bij 0 begint. uitkomst !
good_chant = last_character != " " # uitkomst True, laatste karakter  "!" is ongelijk aan  " "

print (good_chant)

