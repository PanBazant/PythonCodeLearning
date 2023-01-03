enemies = 1
def increase_enemies():
    global enemies
    enemies +=1
    print(f"enemies inside function: {enemies}")
    
print(f"enemies outside function: {enemies}")
increase_enemies()
