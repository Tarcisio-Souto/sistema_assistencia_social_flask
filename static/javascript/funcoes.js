if (window.history.replaceState) {
    window.history.replaceState(null, null, window.location.href);
}


$(document).ready(function () {

    $("#txtCpf").mask("000.000.000-00");
    $('#txtCelular').mask('(00) 00000-0000');
    $('#txtRecado').mask('(00) 0000-0000');
    $('#txtCep').mask('00000-000');

});

function calculaIdade() {

    var data_nasc = $('#txtDataNasc').val()
    var idade = 0

    var data_atual = new Date();

    var ano_atual = data_atual.getFullYear();
    var mes_atual = data_atual.getMonth();
    var dia_atual = data_atual.getDay() - 1;

    if (data_nasc != '') {

        data_nasc = data_nasc.split('-');

        ano = data_nasc[0];
        mes = data_nasc[1];
        dia = data_nasc[2];

        idade = ano_atual - ano;

        if (mes <= mes_atual && dia >= dia_atual) {
            $('#txtIdade').val(idade);
        } else {
            $('#txtIdade').val(idade - 1);
        }

    }

}