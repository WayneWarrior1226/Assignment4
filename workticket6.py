import random
rand = "2"
roulette = ["0","00","RED 1","RED 3","RED 5","RED 7","RED 9","RED 12","RED 14","RED 16","RED 18","RED 19","RED 21","RED 23","RED 25","RED 27","RED 30","RED 32","RED 34","RED 36", "BLACK 2","BLACK 4","BLACK 6","BLACK 8","BLACK 10","BLACK 11","BLACK 13","BLACK 15","BLACK 17","BLACK 20","BLACK 22","BLACK 24","BLACK 26","BLACK 28","BLACK 29","BLACK 31","BLACK 33","BLACK 35"]
print("The possible slots are :", roulette)
while rand != "0":
    rand = input("Enter 1 if you would like to randomly select a slot. enter 0 to exit")
    if rand == "1":
        random_index = random.randrange(len(roulette))
        print("random selected element is",roulette[random_index])

        LOG = []
        LOG.append(roulette[random_index])
        print (LOG)
    
