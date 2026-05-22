def get_questions():
    return {

        # Vehicles
        "vehicle": "Is it a vehicle?",
        "four_wheels": "Does it have four wheels?",
        "two_wheels": "Does it have two wheels?",
        "engine_powered": "Is it engine powered?",
        "pedal_powered": "Is it powered by pedals?",
        "public_transport": "Is it used for public transport?",
        "road_vehicle": "Is it used on roads?",
        "flying": "Can it fly?",
        "water_vehicle": "Does it move on water?",
        "fast": "Is it fast?",
        "slow": "Is it slow?",
        "eco_friendly": "Is it eco-friendly?",

        # Electronics / Appliances
        "electronic": "Is it an electronic device?",
        "electric": "Does it use electricity?",
        "battery_powered": "Is it battery powered?",
        "portable": "Is it portable?",
        "screen": "Does it have a screen?",
        "remote_possible": "Does it use a remote control?",
        "cooling": "Is it used for cooling?",
        "heating": "Is it used for heating?",
        "alarm_sound": "Does it make a sound or alarm?",
        "kitchen_appliance": "Is it a kitchen appliance?",
        "music_related": "Is it used to play or make music?",
        "computing_device": "Is it a computing device like a phone or computer?",
        "camera": "Does it capture images or videos?",

        # Furniture
        "furniture": "Is it a piece of furniture?",
        "seating": "Is it used for sitting?",
        "sleep": "Is it used for sleeping?",
        "flat_surface": "Does it have a flat surface?",
        "storage": "Is it used for storage?",
        "wooden": "Is it made of wood?",
        "legs": "Does it have legs?",
        "indoor_use": "Is it used indoors?",
        "outdoor_use": "Is it used outdoors?",

        # Stationery / Office Items
        "stationery": "Is it a stationery item?",
        "writing_tool": "Is it used for writing?",
        "paper": "Is it made of paper?",
        "pages": "Does it have pages?",
        "reading": "Is it used for reading?",
        "educational": "Is it used for education?",
        "office_use": "Is it commonly used in an office?",

        # Kitchen / Household Items
        "kitchen_tool": "Is it used in the kitchen?",
        "container": "Is it used to hold or store things?",
        "liquid_holder": "Does it hold liquid?",
        "reusable": "Can it be reused?",
        "metal_or_plastic": "Is it made of metal or plastic?",
        "cooking_device": "Is it used for cooking?",
        "utensil": "Is it a utensil or cutlery?",
        "drinkware": "Is it used for drinking?",
        "cleaning_tool": "Is it used for cleaning?",

        # Clothes / Accessories
        "clothing": "Is it an item of clothing?",
        "wearable": "Is it worn on the body?",
        "accessory": "Is it a personal accessory?",
        "fabric": "Is it made of fabric?",
        "footwear": "Is it footwear?",
        "leather": "Is it made of leather?",
        "fashion_item": "Is it a fashion-related item?",

        # Plants / Natural
        "plant": "Is it a plant?",
        "flower": "Is it a flower?",
        "tree_product": "Does it come from a tree?",
        "natural": "Is it naturally occurring?",

        # Decorative / Home Items
        "decorative": "Is it used for decoration?",
        "home_item": "Is it commonly found at home?",
        "light_source": "Does it produce light?",
        "fragile": "Is it fragile or breakable?",
        "ornamental": "Is it ornamental?",
        "indoor_decor": "Is it used for indoor decoration?",

        # Tools / Mechanical
        "tool": "Is it a tool?",
        "cutting_tool": "Is it used for cutting?",
        "handheld": "Is it handheld?",
        "metal": "Is it made of metal?",
        "mechanical": "Does it have mechanical parts?",
        "power_tool": "Is it a power tool?",
        "industrial_use": "Is it used in industries or construction?",

        # Places / Buildings
        "place": "Is it a place?",
        "building": "Is it a building or structure?",
        "home": "Is it a type of home or house?",
        "school": "Is it a school or educational institution?",
        "hospital": "Is it a hospital or medical facility?",
        "temple": "Is it a temple or place of worship?",
        "park": "Is it a park or recreational area?",
        "office": "Is it an office or workspace?",
        "restaurant": "Is it a restaurant or café?",
        "market": "Is it a market or shop?",
        "city_structure": "Is it something found in a city?",

        # Miscellaneous
        "toy": "Is it a toy or plaything?",
        "music_item": "Is it a musical instrument?",
        "game": "Is it used for playing games?",
        "educational_use": "Is it used for learning?",
        "personal_item": "Is it a personal item?",
        "daily_use": "Is it something used daily?",
        "common_item": "Is it a common household item?",
        "upholstered": "Is it covered with padding and fabric or leather?",
        "backrest": "Does it have a support for the back?",

        # FOOD SYSTEM (from second list)

        # Food categories
        "food": "Is it food or edible?",
        "fruit": "Is it a fruit?",
        "vegetable": "Is it a vegetable?",
        "nut": "Is it a nut?",
        "grain": "Is it a grain?",
        "spice": "Is it a spice?",
        "herb": "Is it an herb?",
        "fungus": "Is it a type of mushroom or fungus?",
        "dairy": "Is it a dairy product?",
        "beverage": "Is it a beverage/drink?",
        "sweet_item": "Is it a sweet or dessert?",
        "snack": "Is it a snack or ready-to-eat food?",

        # Origin
        "plant_based": "Is it plant-based?",
        "animal_based": "Is it animal-based?",

        # State / preparation
        "raw": "Is it commonly eaten raw?",
        "cooked": "Is it commonly eaten cooked?",
        "fresh": "Is it normally used fresh?",
        "dry": "Is it dry?",
        "powder": "Is it in powdered form?",
        "liquid": "Is it in liquid form?",
        "thick": "Is it thick in texture?",
        "served_hot_or_cold": "Can it be served hot or cold?",

        # Taste / flavor
        "sweet": "Does it taste sweet?",
        "sour_taste": "Does it taste sour?",
        "spicy": "Is it spicy?",
        "aromatic": "Does it have a strong aroma?",
        "strong_flavor": "Does it have a strong flavor?",
        "tangy": "Is it tangy?",
        "bitter_taste": "Is it bitter?",

        # Texture
        "soft": "Is it soft?",
        "hard": "Is it hard?",
        "crunchy": "Is it crunchy?",
        "juicy": "Is it juicy?",
        "creamy": "Is it creamy?",

        # Shape / size / colors
        "round": "Is it round?",
        "small": "Is it small in size?",
        "large": "Is it large in size?",
        "white": "Is it white in color?",
        "yellow": "Is it yellow in color?",
        "brown": "Is it brown in color?",
        "green": "Is it green in color?",
        "red": "Is it red in color?",
        "orange": "Is it orange in color?",
        "purple": "Is it purple in color?",
        "black": "Is it black in color?",

        # Subcategories
        "tropical": "Is it tropical?",
        "leafy_green": "Is it a leafy green?",
        "root_vegetable": "Is it a root vegetable?",
        "dessert": "Is it a dessert item?",
        "snack_item": "Is it commonly eaten as a snack?",

        # Usage
        "used_in_cooking": "Is it commonly used in cooking?",
        "used_in_sweets": "Is it used in sweets or desserts?",
        "used_in_salads": "Is it used in salads?",
        "garnish": "Is it used as a garnish?",
        "drink": "Is it consumed as a drink?",
        "kitchen_use": "Is it commonly found in kitchens?",

        # Special
        "expensive": "Is it considered expensive?",
        "rare": "Is it rare?",
    }
