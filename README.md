# Dietdoctor-Scraper

collects all the Recipes(Nutritions, Instructions, Recipes and Ingredients) from dietdoctor.com and exports the result as a json file.
https://www.dietdoctor.com/low-carb/keto/recipes/all

## How to install

`sudo apt install python2.7 python-pip`

`sudo pip install scrapy`

## How to Run

`scrapy crawl fbfs`

results:

{"Breakfast": [

    {
      "Nutrition": {
            "Protein": "7 g", 
            "Fiber": "6 g", 
            "kcal": "170", 
            "Fat": "13 g", 
            "Net carbs": "2 g"
          }, 
     "Instructions": [
            {"step1": "Preheat the oven to 350F (175C). Mix the dry ingredients in a large bowl."}, 
            {"step2": "Bring the water to a boil and add it, the vinegar and egg whites to the bowl, while beating with a hand mixer for about 30 seconds. Don't over mix the dough, the consistency should resemble Play-Doh."}, 
            {"step3": "Moisten hands and make 6 pieces of the dough. Place on a greased baking sheet."}, 
            {"step4": "Bake on lower rack in the oven for 5060 minutes, depending on the size of your bread. They're done when you hear a hollow sound when tapping the bottom of the bun."}, 
            {"step5": "Serve with butter and toppings of your choice."}
          ], 
     "Recipe": "1\u20445 cup almond flour, \u00be tbsp ground psyllium husk powder, 1\u20443 tsp baking powder, 1\u20446 tsp sea salt, 1\u20443 tsp cider vinegar, 1\u20446 cup boiling water, \u00bd egg whites, 1\u20443 tbsp sesame seeds (optional)", 
     "Name": "The keto bread", 
     "Ingredients": [
            {
              "Number": "1\u20445 cup", 
              "Ingredient": "almond flour"
            }, {
              "Number": "\u00be tbsp", 
              "Ingredient": "ground psyllium husk powder"
            }, {
              "Number": "1\u20443 tsp", 
              "Ingredient": "baking powder"
            }, {
              "Number": "1\u20446 tsp", 
              "Ingredient": "sea salt"
            }, {
              "Number": "1\u20443 tsp", 
              "Ingredient": "cider vinegar"
            }, {
              "Number": "1\u20446 cup", 
              "Ingredient": "boiling water"
            }, {
              "Number": "\u00bd", 
              "Ingredient": "egg whites"
            }, {
              "Number": "1\u20443 tbsp", 
              "Ingredient": "sesame seeds (optional)"
            }
        ]
      },  ... }
