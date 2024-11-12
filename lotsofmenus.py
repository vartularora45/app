from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from databasesetup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Menu for Urban Burger
restaurant1 = Restaurant(name="Urban Burger")
session.add(restaurant1)
session.commit()

menu_item_1 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                       price="$7.50", course="Entree", restaurant=restaurant1)
session.add(menu_item_1)
session.commit()

menu_item_2 = MenuItem(name="French Fries", description="with garlic and parmesan",
                       price="$2.99", course="Appetizer", restaurant=restaurant1)
session.add(menu_item_2)
session.commit()

menu_item_3 = MenuItem(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                       price="$5.50", course="Entree", restaurant=restaurant1)
session.add(menu_item_3)
session.commit()

menu_item_4 = MenuItem(name="Chocolate Cake", description="fresh baked and served with ice cream",
                       price="$3.99", course="Dessert", restaurant=restaurant1)
session.add(menu_item_4)
session.commit()

# Menu for Super Stir Fry
restaurant2 = Restaurant(name="Super Stir Fry")
session.add(restaurant2)
session.commit()

menu_item_5 = MenuItem(name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                       price="$7.99", course="Entree", restaurant=restaurant2)
session.add(menu_item_5)
session.commit()

menu_item_6 = MenuItem(name="Peking Duck", description="A famous duck dish from Beijing with thin, crisp skin",
                       price="$25", course="Entree", restaurant=restaurant2)
session.add(menu_item_6)
session.commit()

# Menu for Panda Garden
restaurant3 = Restaurant(name="Panda Garden")
session.add(restaurant3)
session.commit()

menu_item_7 = MenuItem(name="Pho", description="Vietnamese noodle soup with herbs and meat",
                       price="$8.99", course="Entree", restaurant=restaurant3)
session.add(menu_item_7)
session.commit()

menu_item_8 = MenuItem(name="Chinese Dumplings", description="Minced meat and vegetables wrapped in dough skin",
                       price="$6.99", course="Appetizer", restaurant=restaurant3)
session.add(menu_item_8)
session.commit()

# Menu for Thyme for That Vegetarian Cuisine
restaurant4 = Restaurant(name="Thyme for That Vegetarian Cuisine")
session.add(restaurant4)
session.commit()

menu_item_9 = MenuItem(name="Tres Leches Cake", description="Sponge cake soaked in sweet milk and topped with whipped cream",
                       price="$2.99", course="Dessert", restaurant=restaurant4)
session.add(menu_item_9)
session.commit()

menu_item_10 = MenuItem(name="Mushroom Risotto", description="Portabello mushrooms in a creamy risotto",
                        price="$5.99", course="Entree", restaurant=restaurant4)
session.add(menu_item_10)
session.commit()

# Menu for Tony's Bistro
restaurant5 = Restaurant(name="Tony's Bistro")
session.add(restaurant5)
session.commit()

menu_item_11 = MenuItem(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish stacked into a tower",
                        price="$13.95", course="Entree", restaurant=restaurant5)
session.add(menu_item_11)
session.commit()

menu_item_12 = MenuItem(name="Mom's Spaghetti", description="Spaghetti with incredible tomato sauce made by mom",
                        price="$6.95", course="Entree", restaurant=restaurant5)
session.add(menu_item_12)
session.commit()

# Menu for Auntie Ann's
restaurant6 = Restaurant(name="Auntie Ann's Diner")
session.add(restaurant6)
session.commit()

menu_item_13 = MenuItem(name="Chicken Fried Steak", description="Battered sirloin steak fried with cream gravy",
                        price="$8.99", course="Entree", restaurant=restaurant6)
session.add(menu_item_13)
session.commit()

menu_item_14 = MenuItem(name="Boysenberry Sorbet", description="Ripe berries turned into frozen, seedless sorbet",
                        price="$2.99", course="Dessert", restaurant=restaurant6)
session.add(menu_item_14)
session.commit()

# Menu for Cocina Y Amor
restaurant7 = Restaurant(name="Cocina Y Amor")
session.add(restaurant7)
session.commit()

menu_item_15 = MenuItem(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                        price="$5.95", course="Entree", restaurant=restaurant7)
session.add(menu_item_15)
session.commit()

menu_item_16 = MenuItem(name="Cachapa", description="Corn-based Venezuelan pancake stuffed with cheese",
                        price="$7.99", course="Entree", restaurant=restaurant7)
session.add(menu_item_16)
session.commit()

# Final Print Statement
print("Added menu items successfully!")
