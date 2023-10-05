let team_a_score = document.querySelector('#team-a-score')
let team_b_score = document.querySelector('#team-b-score')

const socket = new WebSocket(`wss://${window.location.host}/ws/football/`)

socket.onmessage = function(e) {
    //console.log('Server:' + e.data)
    server_data = JSON.parse(e.data)
    
    team_a_score.innerHTML = server_data.team_a_score
    team_b_score.innerHTML = server_data.team_b_score
}

socket.onopen = function(e) {
    socket.send(JSON.stringify({
        'message': 'Hello from client'
    }))
}