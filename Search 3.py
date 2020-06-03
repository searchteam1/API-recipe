import requests

def recipe_search(ingredient):
    app_id = '93319808'
    app_key = '2b68fa0e50ee968894fb3a1bd2eda770    '
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,app_key))
    data = result.json()
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')
    meal = input('Is this for: \n 1. Breakfast \n 2. Lunch \n 3. Dinner ')

    if meal == '1':
        mealType = "Breakfast"

    elif meal == '2':
        mealType = "Lunch"

    else:
        mealType = "Dinner"

    results = recipe_search(ingredient) + recipe_search(mealType)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print()
run()
def ingredients_label():
    ingredient = input('Choose a recipe:  ')
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        if recipe['label'] == ingredient:
            print(recipe['ingredientLines'])
            list_ingredients = recipe['ingredientLines']
            with open('recipe', 'r') as name_list:
                recipe_list = name_list.read()
                recipe_list = recipe_list + str(list_ingredients) + '\n'
            # with open('recipe', 'w+') as name_list:y
        totalcalories = recipe['calories'] #pulls calories info to variable totalcalories
        roundedcalories = round(totalcalories, 2) #rounds calories into 2 decimal case
        print(recipe['label']) #displays recipe label
        print(recipe['image']) #displays recipe image link
        print("Calories/Total energy in Kcal: ", roundedcalories) #prints the rounded calories
        print()
        #prints the result into recipe.txt file
        with open('recipe.txt', 'w') as recipe_file:
            recipe_file.write("result found")
            print()
ingredients_label()