

from itertools import count


favorites = ["Creme Brulee", "Apple Pie", "Churros", "Tiramisu", "Chocolate Cake"]


for dessert in favorites:
    print("One of my favorite desserts is", dessert)



count = 0

while count < len(favorites):
    print("One of my favorite desserts is", favorites[count])
    count += 1    