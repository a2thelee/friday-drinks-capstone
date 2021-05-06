from flask.cli import AppGroup
from .users import seed_users, undo_users
from .drinks import seed_drinks, undo_drinks
from .ingredients import seed_ingredients, undo_ingredients
from .drinkIngredients import seed_drink_ingredients, undo_drink_ingredients
from .favoriteDrinks import seed_favorite_drinks, undo_favorite_drinks

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_drinks()
    seed_ingredients()
    seed_drink_ingredients()
    seed_favorite_drinks()
    # Add other seed functions here

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_drinks()
    undo_ingredients()
    undo_drink_ingredients()
    undo_favorite_drinks()
    # Add other undo functions here
