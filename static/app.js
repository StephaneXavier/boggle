let SCORE = 0
let PLAYED_WORDS = []
/** 
 Capture the user guess with jQuery. Use axios to send a GET request ( query string info, i.e. ?word=$userGuess.val() )
 to the server located at /guess. The server will respond with a string indicating whether or not it is a valid word.

*/
async function checkUserGuess(e) {

    e.preventDefault()
    const $userGuess = $('#user-guess')
    const guessLower = $userGuess.val().toLowerCase()

    if (PLAYED_WORDS.includes(guessLower)) {
        alert('Word already played!')
        $userGuess.val('')
    } else {
        let resp = await axios.get(
            'http://127.0.0.1:5000/guess',
            {
                params: { word: $userGuess.val() }
            })


        update_score(resp, $userGuess.val())
        $('#score-tally').text(`Current score is: ${SCORE}`)

        $('p').text(`Word is ${resp.data}`)
        PLAYED_WORDS.push($userGuess.val().toLowerCase())

        $userGuess.val('')
    }
}

$('button').on('click', checkUserGuess)





/*
Update the SCORE var for the current game if word is valid.
*/
function update_score(resp, $userGuess) {
    if (resp.data === 'ok') {
        SCORE += $userGuess.length
    }
}


/*
After x amount of time, send a POST request to /server with the final score for this game (this will be added to session['score'] as an array of scores).
The SCORE var is send in the body of the POST request. You will receive as an answer, an array of all previous score as resp.data
Display this info
*/
setTimeout(async function () {
    resp = await axios.post(
        'http://127.0.0.1:5000/score',
        {
            score: SCORE
        }
    )

    alert('Time is up!')
    $('form').remove()

    const respData = resp.data
    const gamesPlayed = respData.length
    const topScore = Math.max.apply(Math, respData)
    $('#score-tally').text(`games played: ${gamesPlayed}, top score: ${topScore}`)


}, 60000)