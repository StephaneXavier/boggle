let SCORE = 0

// class BoggleGame(){
//     constructor(words_played){
//         this.words_played = words_played

//     }
// }

async function checkUserGuess(e) {
    e.preventDefault()
    let $userGuess = $('#user-guess')
    let resp = await axios.get(
        'http://127.0.0.1:5000/guess',
        {
            params: { word: $userGuess.val() }
        },
    )
    console.log(resp.data)
    update_score(resp, $userGuess.val())
    $('#score-tally').text(`Current score is: ${SCORE}`)

    $('p').text(`Word is ${resp.data}`)
    $userGuess.val('')
}

$('button').on('click', checkUserGuess)

function update_score(resp, $userGuess) {
    if (resp.data === 'ok') {
        SCORE += $userGuess.length
    }
}

setTimeout(async function () {
    resp = await axios.post(
        'http://127.0.0.1:5000/score',
        {
            score: SCORE
        }
    )

    alert('Time is up!')
    $('form').remove()
}, 6000)