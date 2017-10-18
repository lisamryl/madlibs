"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Prompts for madlib entries or says goodbye."""

    response = request.args.get("play-game")
    player = request.args.get("player")

    if response == 'no':
        return render_template("goodbye.html", name=player)
    else:
        return render_template("game.html", name=player)


@app.route('/madlib')
def show_madlib():
    """Shows user their madlib."""

    person = request.args.get("name")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adj = request.args.get("adj")
    list_of_items = request.args.getlist("items")

    if len(list_of_items) > 2:
        item_list = list_of_items[0:-1].join(", ") + "and " + list_of_items[-1]

    return render_template("madlib.html",
                           person=person,
                           color=color,
                           noun=noun,
                           adj=adj,
                           items=item_list)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)