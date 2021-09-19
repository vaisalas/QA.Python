

#Assigning 2 variables and storing the data.
devs_money = 100
dev_can_play_smash = False 


#Here we a starting an if statement with the conditional being, if devs_money is bigger than 10 and if dev_can_play_smash is True.
if devs_money > 10 and dev_can_play_smash:
    print("Dev enters a smash tournament")    

#Here we add an elif statement, so that if the previous conditional is False
elif devs_money < 10 and dev_can_play_smash:
    print("Dev is too poor to enter")

else:
    print("Dev just can't play smash")



