import requests
def recipe_search(ingredient):
    app_id = 'ab815412'
    app_key = '4ee517fe7cac370292747def4644b492'
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,app_key))

    data = result.json()
    return data['hits']

def run():
    ingredient = input('Enter an ingredient: ')

    results = recipe_search(ingredient)

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

            with open('recipe', 'w+') as name_list:
                name_list.write(recipe_list)

ingredients_label()

