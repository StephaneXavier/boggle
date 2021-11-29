from boggle import Boggle
from flask import Flask, request, redirect, session, render_template, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "abc123"

boggle_game = Boggle()


@app.route('/')
def index():
    """
    from the instance of Boggle(), make the board and set the session['board']
    to be that var. Pass that board onto index.html
    """
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('index.html', board = board)

@app.route('/guess')
def user_guess():
    """
    Receive the axios get parametres for the 'word' query string.
    Set the response the server will return with the Boggle() method 
    of check_valid_word (which returns 'ok',' not-on-board' or 'not-a-word' )
    """
    word = request.args.get('word')
    
    response = boggle_game.check_valid_word(session['board'], word)
    
    return jsonify(response)

@app.route('/score', methods=['POST'])
def save_score():
    """
    
    """
    req = request.get_json()
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print('current request.get_json() is =>',req['score'])
    if not session.get('score'):
        session['score'] = [req['score']]

    else:
        score = session.get('score')
        score.append(req['score'])
        session['score'] = score
     
        
    print('current session["score"] is =>', session['score'] )
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%")
    # import pdb
    # pdb.set_trace()
    return redirect ('/')
    

    
   