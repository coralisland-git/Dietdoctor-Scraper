# Dietdoctor-Scraper

collects all the Recipes(Nutritions, Instructions, Recipes and Ingredients) from dietdoctor.com and exports the result as a json file.
https://www.dietdoctor.com/low-carb/keto/recipes/all

## How to install

`sudo apt install python2.7 python-pip`

`sudo pip install scrapy`

## How to Run

`scrapy crawl fbfs`

results:

{"Breakfast": [{"Nutrition": {"Protein": "", "Fiber": "", "kcal": "", "Fat": "", "Net carbs": ""}, "Instructions": [{"step1": "One way of varying your olive oil is to use different herbs, lemon zest, or perhaps garlic or chili for flavoring. Use organic products when available."}, {"step1": "Wash carefully and peel/cut them the way you like."}, {"step1": "Add flavoring to a dry, clean small glass jar/bottle or a jar with a lid and pour in extra virgin olive oil. Bundle and tie the herbs together, so that it will be easier to get them out. To prevent mold from growing, be sure the oil covers the flavoring."}, {"step1": "Prepare fresh and use right away. If you are saving any leftovers, refrigerate the oil and use within a week. Flavored oils can be enjoyed as a dressing on top of your meal or used for cooking."}], "Recipe": " olive oil,  flavoring of your choice (see our suggestions for inspiration)", "Name": "Flavored olive oil", "Ingredients": [{"Number": "", "Ingredient": "olive oil"}, {"Number": "", "Ingredient": "flavoring of your choice (see our suggestions for inspiration)"}]} ... }
