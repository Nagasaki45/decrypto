function generateCode() {
    var code = _.sample([1,2,3,4], 3);
    setCode(code);
}

function setCode(code) {
    for(idx = 0; idx < 3; idx++) {
        $('#code' + idx).text(code[idx]);
    }
    $('#codeModal').modal('show');
}

function setWords(words) {
    for(idx = 0; idx < 4; idx++) {
        $('#word' + idx).text(words[idx]);
    }
}

function newTeam() {
    var newTeamData;
    $.ajax({
        url: "new-team",
        async: false,
        success: function(data) {
            newTeamData = data;
        }
    });
    setWords(newTeamData["words"]);
    window.location.hash = newTeamData["team"];
}

function openTeam(team) {
    var words;
    $.ajax({
        url: "get-team",
        data: {team: team},
        async: false,
        success: function(data) {
            words = data["words"];
        }
    });
    setWords(words);
}

function initialize() {
    var team = window.location.hash;

    if (team) {
        openTeam(team.replace("#", ""));
    } else {
        newTeam();
    }
}

$(document).ready(function() {
    initialize();
});
