from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def register():
    return render_template('signup.html')

@app.route('/snake')
def snake():
    return render_template('snake.html')

@app.route('/tictactoe')
def tictactoe():
    return render_template('tictactoe.html')

@app.route('/flappy-bird')
def flappybird():
    return render_template('flappy-bird.html')

@app.route('/wordle')
def wordle():
    return render_template('wordle.html')

@app.route('/twozerofoureight')
def twozerofoureight():
    return render_template('twozerofoureight.html')

@app.route('/pingpong')
def pingpong():
    return render_template('pingpong.html')

@app.route('/dino-game')
def dino():
    return render_template('dino-game.html')

@app.route('/puzzle')
def puzzle():
    return render_template('puzzle.html')

@app.route('/slide-puzzle')
def slidepuzzle():
    return render_template('slide-puzzle.html')

@app.route('/space-invaders')
def spaceinvaders():
    return render_template('space-invaders.html')

@app.route('/blackjack')
def blackjack():
    return render_template('blackjack.html')

@app.route('/candy-crush')
def candycrush():
    return render_template('candy-crush.html')

@app.route('/minesweeper')
def minesweeper():
    return render_template('minesweeper.html')

@app.route('/sudoku')
def sudoku():
    return render_template('sudoku.html')

@app.route('/rockpaperscissors')
def rockpaperscissors():
    return render_template('rockpaperscissors.html')

@app.route('/whackamole')
def whackamole():
    return render_template('whackamole.html')

@app.route('/doodle-jump')
def doodlejump():
    return render_template('doodle-jump.html')

@app.route('/connect-four')
def connectfour():
    return render_template('connect-four.html')

@app.route('/hangman')
def hangman():
    return render_template('hangman.html')

@app.route('/memory-cards')
def memorycards():
    return render_template('memory-cards.html')

@app.route('/hoverthreed')
def hoverthreed():
    return render_template('hoverthreed.html')

if __name__ == '__main__':
    app.run(debug=True)