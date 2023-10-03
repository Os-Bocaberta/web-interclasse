let team_a_score = document.querySelector('#team-a-score')
let team_b_score = document.querySelector('#team-b-score')
let players_team_a_scores = document.querySelector('#players-team-a-scores')
let players_team_b_scores = document.querySelector('#players-team-b-scores')
let player =  '<svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M6.02166 0C9.31408 0 12 2.68592 12 6.02166C12 9.31408 9.31408 12 6.02166 12C2.68592 12 0 9.31408 0 6.02166C0 2.68592 2.68592 0 6.02166 0ZM3.59567 9.05415L4.72202 7.66787L4.11552 5.71841L2.25271 4.93863L0.433213 6.28159L0.34657 6.19495C0.389892 7.3213 0.736462 8.31769 1.29964 9.18412L1.34296 9.05415H3.59567ZM4.98195 7.84116L3.8556 9.27076L4.54874 11.3935L4.41877 11.4368C5.45848 11.7401 6.54152 11.7401 7.58123 11.4368L7.49459 11.3935L8.18773 9.27076L7.01805 7.84116H4.98195ZM7.27798 7.66787L8.40433 9.05415H10.657L10.7004 9.18412C11.3069 8.31769 11.6534 7.3213 11.6968 6.19495L11.5668 6.28159L9.74729 4.93863L7.9278 5.71841L7.27798 7.66787ZM7.79783 5.41516L9.66065 4.6787L10.3538 2.51264H10.4838C9.83394 1.68953 8.92419 1.03971 7.9278 0.649819L7.97112 0.779783L6.15162 2.12274V4.24549L7.79783 5.41516ZM2.33935 4.6787L4.20217 5.41516L5.84838 4.24549V2.12274L4.02888 0.823105L4.0722 0.649819C3.07581 1.03971 2.16606 1.68953 1.51625 2.51264H1.64621L2.33935 4.6787ZM4.46209 0.563177L4.41877 0.693141L6.02166 1.81949L7.62455 0.693141L7.58123 0.563177C6.54152 0.259928 5.45848 0.259928 4.46209 0.563177ZM10.7004 2.85921H10.5704L9.9639 4.72202L11.5668 5.8917L11.6968 5.80505C11.6534 4.72202 11.3069 3.68231 10.7004 2.85921ZM10.4838 9.53069L10.4404 9.3574H8.44765L7.84116 11.2635L7.97112 11.3502C8.96751 10.9603 9.83394 10.3538 10.4838 9.53069ZM4.0722 11.3502L4.15884 11.2635L3.55235 9.3574H1.60289L1.55957 9.53069C2.20939 10.3538 3.07581 10.9603 4.0722 11.3502ZM0.34657 5.80505L0.433213 5.8917L2.0361 4.72202L1.4296 2.85921H1.29964C0.736462 3.68231 0.389892 4.72202 0.34657 5.80505ZM7.58123 5.67509L6.02166 4.50542L4.41877 5.67509L5.02527 7.53791H6.97473L7.58123 5.67509Z" fill="white"/></svg><h3>player name</h3>'
let team_a_fauls = document.querySelector('#team_a_fauls')
let team_b_fauls = document.querySelector(' #team_b_fauls')
let team_a_blocks = document.querySelector('#team_a_blocks')
let team_b_blocks = document.querySelector('#team_b_blocks')
let team_a_errors = document.querySelector('#team_a_errors')
let team_b_errors = document.querySelector('#team_b_errors')
let match_time = document.querySelector('#match-time')

const socket = new WebSocket(`wss://${window.location.host}/ws/football/`)

socket.onmessage = function(e) {
    //console.log('Server:' + e.data)
    server_data = JSON.parse(e.data)
    
    team_a_score.innerHTML = server_data.team_a_score
    team_b_score.innerHTML = server_data.team_b_score

    team_a_fauls.innerHTML = server_data.team_a_fauls
    team_b_fauls.innerHTML = server_data.team_b_fauls

    team_a_blocks.innerHTML = server_data.team_a_blocks
    team_b_blocks.innerHTML = server_data.team_b_blocks

    team_a_errors.innerHTML = server_data.team_a_errors
    team_b_errors.innerHTML = server_data.team_b_errors
    
    match_time.innerHTML = `${server_data.minutes}'`

    players_team_a_scores.innerHTML = ""
    players_team_b_scores.innerHTML = ""

    server_data.team_a_players_scores.map((item) => {
        players_team_a_scores.innerHTML += `<div class="player__score"><svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg"> <path d="M11.5271 3.66502C11.2315 2.95567 10.7882 2.30542 10.2414 1.75862C9.69458 1.21182 9.04434 0.768473 8.33498 0.472907C7.59606 0.162562 6.81281 0 6 0C5.18719 0 4.40394 0.162562 3.66502 0.472907C2.95567 0.768473 2.30542 1.21182 1.75862 1.75862C1.21182 2.30542 0.768473 2.95567 0.472907 3.66502C0.162562 4.40394 0 5.18719 0 6C0 6.81281 0.162562 7.59606 0.472907 8.33498C0.768473 9.04434 1.21182 9.69458 1.75862 10.2414C2.30542 10.7882 2.95567 11.2315 3.66502 11.5271C4.40394 11.8374 5.18719 12 6 12C6.81281 12 7.59606 11.8374 8.33498 11.5271C9.04434 11.2315 9.69458 10.7882 10.2414 10.2414C10.7882 9.69458 11.2315 9.04434 11.5271 8.33498C11.8374 7.59606 12 6.81281 12 6C12 5.18719 11.8522 4.40394 11.5271 3.66502ZM11.7783 6C11.7783 6.63547 11.6749 7.24138 11.4828 7.81773C10.7143 8.92611 9.73892 9.69458 9.04433 10.1527C8.42365 10.5517 7.92118 10.7734 7.75862 10.8473C7.4335 10.5961 7.13793 10.2562 6.90148 9.8867C7.18227 9.65025 8.20197 8.7931 9.16256 7.66995C9.82759 6.8867 10.3448 6.133 10.6847 5.42365C11.0246 4.72906 11.202 4.07882 11.2167 3.48768C11.5714 4.25616 11.7783 5.09852 11.7783 6ZM10.9507 3.02956C11.1429 4.58128 9.99015 6.32512 8.97044 7.50739C8.03941 8.58621 7.07882 9.42857 6.76847 9.6798C6.57635 9.3399 6.39901 8.98522 6.28079 8.6601C5.89655 7.69951 5.70443 6.78325 5.6601 6.5468C7.03448 5.23153 8.00985 4.07882 8.55665 3.11823C8.98522 2.37931 9.16256 1.75862 9.07389 1.27094C9.05911 1.19704 9.04433 1.12315 9.01478 1.06404C9.81281 1.5665 10.4778 2.24631 10.9507 3.02956ZM8.55665 0.812808C8.63054 0.857143 8.80788 1.00493 8.86699 1.34483C8.89655 1.53695 8.88177 1.75862 8.82266 2.00985C8.3202 1.59606 7.74384 1.24138 7.13793 0.990148C6.59113 0.768473 6 0.62069 5.40887 0.53202C5.02463 0.472906 4.68473 0.458128 4.40394 0.458128C4.9064 0.310345 5.4532 0.236453 6 0.236453C6.91626 0.221675 7.7734 0.44335 8.55665 0.812808ZM3.6798 0.70936C3.79803 0.694581 4.47783 0.62069 5.37931 0.753695C6.28079 0.8867 7.58128 1.25616 8.73399 2.24631C8.6601 2.48276 8.52709 2.74877 8.36453 3.02956C8.26108 3.2069 8.14286 3.38424 8.00985 3.57635C7.0936 3.17734 6.14778 2.89655 5.20197 2.74877C4.4335 2.61576 3.65025 2.57143 2.89655 2.61576C2.06897 2.6601 1.46305 2.7931 1.12315 2.89655C1.74384 1.93596 2.63054 1.16749 3.6798 0.70936ZM0.960591 3.19212C1.13793 3.133 1.84729 2.91133 2.92611 2.85222C4.04926 2.7931 5.82266 2.91133 7.87685 3.78325C7.31527 4.55172 6.53202 5.42365 5.51232 6.39901C4.46305 5.97044 3.51724 5.67488 2.71921 5.54187C2.05419 5.42365 1.49261 5.40887 1.03448 5.49754C0.635468 5.55665 0.384236 5.70443 0.221675 5.83744C0.251232 4.87685 0.517241 3.97537 0.960591 3.19212ZM0.221675 6.16256C0.251232 6.133 0.295567 6.05911 0.384237 6C0.458128 5.94089 0.576355 5.867 0.738916 5.80788C0.724138 6.04434 0.694581 6.48768 0.70936 7.0197C0.724138 7.47783 0.753695 7.89163 0.812808 8.27586C0.842365 8.43842 0.871921 8.60098 0.901478 8.74877C0.502463 7.9803 0.251232 7.0936 0.221675 6.16256ZM1.34483 9.41379L1.37438 9.39901C1.12315 8.83744 0.990148 8.00985 0.960591 7.00493C0.945813 6.41379 0.97537 5.91133 0.990148 5.71921C1.03448 5.70443 1.07882 5.70443 1.12315 5.68966C1.38916 5.64532 1.72906 5.63054 2.18719 5.67488C2.3202 6.84236 2.58621 7.89163 2.94089 8.7931C3.23645 9.5468 3.60591 10.197 4.04926 10.7438C4.41872 11.202 4.75862 11.4975 5.02463 11.6897C3.51724 11.4384 2.20197 10.5961 1.34483 9.41379ZM5.57143 11.7635C5.52709 11.7488 5.37931 11.6749 5.17241 11.5271C4.93596 11.3645 4.59606 11.069 4.21182 10.5961C3.56158 9.78325 2.73399 8.27586 2.42365 5.70443C3.16256 5.80788 4.13793 6.05911 5.43842 6.60591C5.48276 6.85714 5.67488 7.78818 6.05911 8.76355C6.32512 9.42857 6.63547 9.99015 6.99015 10.4187C7.34483 10.8621 7.74384 11.1724 8.17241 11.3498C7.50739 11.6305 6.76847 11.7783 6 11.7783C5.85222 11.7783 5.71921 11.7635 5.57143 11.7635ZM8.48276 11.2167C8.30542 11.1724 8.12808 11.0985 7.96552 10.9951C8.20197 10.8916 8.63054 10.67 9.14778 10.3448C9.60591 10.0493 10.0345 9.72414 10.4187 9.36946C10.67 9.13301 10.9064 8.89655 11.1281 8.64532C10.5665 9.75369 9.62069 10.67 8.48276 11.2167Z" fill="white"/> </svg><h3>${item.player.name} | ${item.player.number}</h3></div>`
    })
    server_data.team_b_players_scores.map((item) => {
        players_team_b_scores.innerHTML += `<div class="player__score player__score__b"><h3>${item.player.name} | ${item.player.number}</h3><svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg"> <path d="M11.5271 3.66502C11.2315 2.95567 10.7882 2.30542 10.2414 1.75862C9.69458 1.21182 9.04434 0.768473 8.33498 0.472907C7.59606 0.162562 6.81281 0 6 0C5.18719 0 4.40394 0.162562 3.66502 0.472907C2.95567 0.768473 2.30542 1.21182 1.75862 1.75862C1.21182 2.30542 0.768473 2.95567 0.472907 3.66502C0.162562 4.40394 0 5.18719 0 6C0 6.81281 0.162562 7.59606 0.472907 8.33498C0.768473 9.04434 1.21182 9.69458 1.75862 10.2414C2.30542 10.7882 2.95567 11.2315 3.66502 11.5271C4.40394 11.8374 5.18719 12 6 12C6.81281 12 7.59606 11.8374 8.33498 11.5271C9.04434 11.2315 9.69458 10.7882 10.2414 10.2414C10.7882 9.69458 11.2315 9.04434 11.5271 8.33498C11.8374 7.59606 12 6.81281 12 6C12 5.18719 11.8522 4.40394 11.5271 3.66502ZM11.7783 6C11.7783 6.63547 11.6749 7.24138 11.4828 7.81773C10.7143 8.92611 9.73892 9.69458 9.04433 10.1527C8.42365 10.5517 7.92118 10.7734 7.75862 10.8473C7.4335 10.5961 7.13793 10.2562 6.90148 9.8867C7.18227 9.65025 8.20197 8.7931 9.16256 7.66995C9.82759 6.8867 10.3448 6.133 10.6847 5.42365C11.0246 4.72906 11.202 4.07882 11.2167 3.48768C11.5714 4.25616 11.7783 5.09852 11.7783 6ZM10.9507 3.02956C11.1429 4.58128 9.99015 6.32512 8.97044 7.50739C8.03941 8.58621 7.07882 9.42857 6.76847 9.6798C6.57635 9.3399 6.39901 8.98522 6.28079 8.6601C5.89655 7.69951 5.70443 6.78325 5.6601 6.5468C7.03448 5.23153 8.00985 4.07882 8.55665 3.11823C8.98522 2.37931 9.16256 1.75862 9.07389 1.27094C9.05911 1.19704 9.04433 1.12315 9.01478 1.06404C9.81281 1.5665 10.4778 2.24631 10.9507 3.02956ZM8.55665 0.812808C8.63054 0.857143 8.80788 1.00493 8.86699 1.34483C8.89655 1.53695 8.88177 1.75862 8.82266 2.00985C8.3202 1.59606 7.74384 1.24138 7.13793 0.990148C6.59113 0.768473 6 0.62069 5.40887 0.53202C5.02463 0.472906 4.68473 0.458128 4.40394 0.458128C4.9064 0.310345 5.4532 0.236453 6 0.236453C6.91626 0.221675 7.7734 0.44335 8.55665 0.812808ZM3.6798 0.70936C3.79803 0.694581 4.47783 0.62069 5.37931 0.753695C6.28079 0.8867 7.58128 1.25616 8.73399 2.24631C8.6601 2.48276 8.52709 2.74877 8.36453 3.02956C8.26108 3.2069 8.14286 3.38424 8.00985 3.57635C7.0936 3.17734 6.14778 2.89655 5.20197 2.74877C4.4335 2.61576 3.65025 2.57143 2.89655 2.61576C2.06897 2.6601 1.46305 2.7931 1.12315 2.89655C1.74384 1.93596 2.63054 1.16749 3.6798 0.70936ZM0.960591 3.19212C1.13793 3.133 1.84729 2.91133 2.92611 2.85222C4.04926 2.7931 5.82266 2.91133 7.87685 3.78325C7.31527 4.55172 6.53202 5.42365 5.51232 6.39901C4.46305 5.97044 3.51724 5.67488 2.71921 5.54187C2.05419 5.42365 1.49261 5.40887 1.03448 5.49754C0.635468 5.55665 0.384236 5.70443 0.221675 5.83744C0.251232 4.87685 0.517241 3.97537 0.960591 3.19212ZM0.221675 6.16256C0.251232 6.133 0.295567 6.05911 0.384237 6C0.458128 5.94089 0.576355 5.867 0.738916 5.80788C0.724138 6.04434 0.694581 6.48768 0.70936 7.0197C0.724138 7.47783 0.753695 7.89163 0.812808 8.27586C0.842365 8.43842 0.871921 8.60098 0.901478 8.74877C0.502463 7.9803 0.251232 7.0936 0.221675 6.16256ZM1.34483 9.41379L1.37438 9.39901C1.12315 8.83744 0.990148 8.00985 0.960591 7.00493C0.945813 6.41379 0.97537 5.91133 0.990148 5.71921C1.03448 5.70443 1.07882 5.70443 1.12315 5.68966C1.38916 5.64532 1.72906 5.63054 2.18719 5.67488C2.3202 6.84236 2.58621 7.89163 2.94089 8.7931C3.23645 9.5468 3.60591 10.197 4.04926 10.7438C4.41872 11.202 4.75862 11.4975 5.02463 11.6897C3.51724 11.4384 2.20197 10.5961 1.34483 9.41379ZM5.57143 11.7635C5.52709 11.7488 5.37931 11.6749 5.17241 11.5271C4.93596 11.3645 4.59606 11.069 4.21182 10.5961C3.56158 9.78325 2.73399 8.27586 2.42365 5.70443C3.16256 5.80788 4.13793 6.05911 5.43842 6.60591C5.48276 6.85714 5.67488 7.78818 6.05911 8.76355C6.32512 9.42857 6.63547 9.99015 6.99015 10.4187C7.34483 10.8621 7.74384 11.1724 8.17241 11.3498C7.50739 11.6305 6.76847 11.7783 6 11.7783C5.85222 11.7783 5.71921 11.7635 5.57143 11.7635ZM8.48276 11.2167C8.30542 11.1724 8.12808 11.0985 7.96552 10.9951C8.20197 10.8916 8.63054 10.67 9.14778 10.3448C9.60591 10.0493 10.0345 9.72414 10.4187 9.36946C10.67 9.13301 10.9064 8.89655 11.1281 8.64532C10.5665 9.75369 9.62069 10.67 8.48276 11.2167Z" fill="white"/> </svg></div>`
    })
}

socket.onopen = function(e) {
    socket.send(JSON.stringify({
        'message': 'Hello from client'
    }))
}