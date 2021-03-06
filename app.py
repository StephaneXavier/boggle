from boggle import Boggle
from flask import Flask, request, redirect, session, render_template, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"

boggle_game = Boggle()


@app.route('/')
def index():
    """
    from the instance of Boggle(), make the board and set the session['board']
    to be that board. Pass that board into index.html
    """
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('index.html', board = board)

@app.route('/guess')
def user_guess():
    """
    Receive the axios GET request parametres (query string) for the 'word' query string (line 16 of app.js params {word:...}).
    Set the response the server will return with the Boggle() method 
    of check_valid_word (which returns 'ok',' not-on-board' or 'not-a-word' )
    """
    word = request.args.get('word')
    
    response = boggle_game.check_valid_word(session['board'], word)
    
    return jsonify(response)

@app.route('/score', methods=['POST'])
def save_score():
    """
    Receive the body of the POST request sent by axios and parse out the data.
    If session['score'] doesn't exist, create it and set the first elem to be the posted data.
    Else, append it to the session['score'] list. Return this list of scores as a response
    """
    req = request.get_json()
    
    if not session.get('score'):
        session['score'] = [req['score']]

    else:
        score = session.get('score')
        score.append(req['score'])
        session['score'] = score
     
    response = session['score']   
    # import pdb
    # pdb.set_trace()
    return jsonify(response)