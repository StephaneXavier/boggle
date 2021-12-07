class BoggleGame {
    constructor() {
        this.SCORE = 0
        this.PLAYED_WORDS = []
        this.timer = setTimeout(this.timer.bind(this), 60000)
        $('button').on('click', this.checkUserGuess.bind(this))

    }

    update_score(resp, $userGuess) {
        if (resp.data === 'ok') {
            this.SCORE += $userGuess.length
        }
    }

    async checkUserGuess(e) {

        e.preventDefault()
        const $userGuess = $('#user-guess')
        const guessLower = $userGuess.val().toLowerCase()


        if (this.PLAYED_WORDS.includes(guessLower)) {
            alert('Word already played!')
            $userGuess.val('')
        } else {

            let resp = await axios.get(
                'http://127.0.0.1:5000/guess',
                {
                    params: { word: $userGuess.val() }
                })


            this.update_score(resp, $userGuess.val())
            $('#score-tally').text(`Current score is: ${this.SCORE}`)

            $('p').text(`Word is ${resp.data}`)
            this.PLAYED_WORDS.push($userGuess.val().toLowerCase())

            $userGuess.val('')
        }
    }


    async timer() {

        const resp = await axios.post(
            'http://127.0.0.1:5000/score',
            {
                score: this.SCORE
            }
        )

        alert('Time is up!')
        $('form').remove()

        const respData = resp.data
        const gamesPlayed = respData.length
        const topScore = Math.max.apply(Math, respData)
        $('#score-tally').text(`games played: ${gamesPlayed}, top score: ${topScore}`)
    }

}




new BoggleGame()






