pasta = ("Pasta arrabita","Italian",40, "medium")
biryani = ("Chicken biryani","Indian",60,"Hard")
print("Recipe 1:",pasta)
print("name:", pasta[0])
print("cusine:", pasta[1])
print("difficulty:", pasta[-1])

all_recipies = (pasta,biryani)
print("\nFirst recipe name:", all_recipies[0][0])
print("Second recipe time:", all_recipies[1][2], "mins")
print("pasta details (sliced)",pasta[1:3])

print("\nPasta recipe details:")
for detail in pasta:
    print(" -",detail)

pasta_ingredients = {"toamto", "garlic", "olive oil", "chilli", "pasta", "garlic"}
biryani_ingredients = {"rice","chicken", "garlic", "onion", "tomato", "spices"}
print("\nPasta ingredients", pasta_ingredients)
print("Biryani ingredients:", biryani_ingredients)
print("Total pasta ingredients", len(pasta_ingredients))

pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chilli")
print("\nUpdated pasta ingredients:", pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll ingredients (union):", all_ingredients)
print("common ingredients (intersection):", common)
print("Only in pasta(difference):", only_pasta)
print("not shared(sym. difference):", unique_to_each)
