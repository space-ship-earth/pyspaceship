
GOALS_BY_CATEGORY = {
  "diet": {
    "icon": None,
    "title": "Plant-Rich Diet",
    "description": "Change your diet, change the world",
    "goals": [
      {
        "name": "Go Vegan",
        "short_description": "Avoid all animal products",
        "description": "Animal products are bad. Don't eat them.",
      },
      {
        "name": "Go Vegetarian",
        "short_description": "Avoid all animal products",
        "description": "Animal products are bad. Don't eat them.",
      },
      {
        "name": "Avoid Beef",
        "short_description": "Avoid all animal products",
        "description": "Animal products are bad. Don't eat them.",
      },
    ],
  },
  "transportation": {
    "icon": None,
    "title": "Transportation",
    "description": "Save energy by changing how you travel",
    "goals": [
      {
        "name": "Bike to work",
        "short_description": "Ride your bike to work or school",
        "description": "You should be biking more. Good for you and good for the planet.",
      },
    ],
  },
  "education": {
    "icon": None,
    "title": "Education",
    "description": "Learn more about the science and policy of climate change",
    "goals": [
      {
        "name": "Read a book",
        "short_description": "Become educated about climate change",
        "description": "This is your chance. You've always wanted to read.",
      },
    ],
  },
}

# let goals know their category
for category, cinfo in GOALS_BY_CATEGORY.items():
  for goal in cinfo['goals']:
    goal['category'] = category
