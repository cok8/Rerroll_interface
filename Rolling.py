import numpy as np


"The probabilities of every tier you can roll for each level"
p1 = [1,0,0,0,0]
p2 = [1,0,0,0,0]
p3 = [0.75,0.25,0,0,0]
p4 = [0.55,0.3,0.15,0,0]
p5 = [0.4,0.35,0.2,0.05,0]
p6 = [0.25,0.35,0.3,0.1,0]
p7 = [0.19,0.3,0.35,0.15,0.01]
p8 = [0.14,0.2,0.35,0.25,0.06]
p9 = [0.10,0.15,0.3,0.3,0.15]

level = 1
probability = [p1,p2,p3,p4,p5,p6,p7,p8,p9]
choice = [1,2,3,4,5]

"Set of pokemons in the respective tier"
tier1 = ["Weedle", "Pidgeotto", "Nidoran m", "Nidoran f", "Poliwag"]
tier2 = ["Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Machop"]
tier3 = ["Pikachu", "Abra", "Shellder", "Dratini", "Vulpix"]
tier4 = ["Venonat", "Tentacool", "Pontya", "Seel", "Mankey"]
tier5 = ["Moltres", "Zapdos", "Articuno", "Mewtwo", "Mew"]

tier = [tier1, tier2, tier3, tier4, tier5]

while True:
    action = input("Pick an action, r or d")
    if action == "r":  # press r to roll
        p = probability[level - 1]
        result = np.random.choice(choice, 5, p = p)
        print("Current Level: " + str(level))
        pokemonlist = []
        for i in result:
            pokemon = np.random.choice(tier[i-1])
            pokemonlist.append(pokemon)
        print(result)
        print(pokemonlist)

    if action == "d": # press d to level  up
        if level < 9:
            print("Level up!")
            level += 1
            print("Current Level: " + str(level))
        else:
            print("Level Maxed") # prevent level pass through lv 9 which cause errors


