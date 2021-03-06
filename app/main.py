import flask
import json
from utils.game_state import GameState
from snakes import get_snake

app = flask.Flask(__name__)


@app.route('/<snake_name>/')
def index(snake_name):
    return """
        <a href="https://github.com/sendwithus/battlesnake-python">
            battlesnake-python
        </a>
    """


@app.route('/<snake_name>/start', methods=['GET', 'POST'])
def start(snake_name):
    snake = get_snake(snake_name)

    return json.dumps({
        'name': snake.name(),
        'color': snake.color(),
        'head_url': snake.head_url(),
        'taunt': snake.taunt()
    })


@app.route('/<snake_name>/move', methods=['GET', 'POST'])
def move(snake_name):
    snake = get_snake(snake_name)
    data = flask.request.json
    gamestate = GameState(data)
    move = snake.move(gamestate)

    return json.dumps({
        "move": move.direction()
    })


@app.route('/<snake_name>/end', methods=['GET', 'POST'])
def end(snake_name):
    snake = get_snake(snake_name)
    snake.end()
    return json.dumps({})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
