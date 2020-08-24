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
