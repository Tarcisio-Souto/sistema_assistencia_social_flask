/* ---------------------------------------------------
    Login
----------------------------------------------------- */

function setLogin() {

    var txtCpf = $('#txtCpf').val();
    var txtPassword = $('#txtPassword').val();

    var inputs = document.getElementsByClassName('required_login');
    var len = inputs.length;
    var valid = true;
    for (var i = 0; i < len; i++) {
        if (!inputs[i].value) {
            valid = false;
            inputs[i].style.border = '1px solid';
            inputs[i].style.borderColor = 'red';
        } else {
            inputs[i].style.border = 'none';
        }
    }
    if (valid) {

        $.ajax({
            data: {                
                cpf: txtCpf,
                password: txtPassword
            },
            type: 'POST',
            url: '/auth'

        })
            .done(function (data) {

                if (data.error) {
                    $('#errorAlertLogin').text(data.error).show();
                } else {
                    window.location = "/home";
                }

            });

        setTimeout(function () {
            $('#errorAlertLogin').hide();
        }, 2500);

    }


}


/* ---------------------------------------------------
    Cadastro de Funcionário
----------------------------------------------------- */

function cadFunc() {

    var txtNome = $('#txtNome').val();
    var txtdataNasc = $('#txtDataNasc').val();
    var txtIdade = $('#txtIdade').val();
    var txtCPF = $('#txtCpf').val();
    var txtRg = $('#txtRg').val();
    var txtSexo = $('#selectSexo').val();
    var txtCelular = $('#txtCelular').val();
    var txtRecado = $('#txtRecado').val();
    var txtCargo = $('#selectCargo').val();
    var txtSenha = $('#txtSenha').val();
    var txtLogradouro = $('#txtLogradouro').val();
    var txtNumero = $('#txtNumero').val();
    var txtBairro = $('#txtBairro').val();
    var txtMunicipio = $('#txtMunicipio').val();
    var txtCep = $('#txtCep').val();
    var txtEstado = $('#txtEstado').val();


    /* O Trecho abaixo verifica se os inputs com a classe "required_func" estão preenchidos */

    var inputs = document.getElementsByClassName('required_func');
    var len = inputs.length;
    var valid = true;
    for (var i = 0; i < len; i++) {
        if (!inputs[i].value) {
            valid = false;
            inputs[i].style.border = '1px solid';
            inputs[i].style.borderColor = 'red';
        } else {
            inputs[i].style.border = 'none';
        }
    }
    if (valid) {

        $.ajax({
            data: {
                nome_func: txtNome,
                cpf: txtCPF,
                rg: txtRg,
                data_nasc: txtdataNasc,
                idade: txtIdade,
                sexo: txtSexo,
                telefone1: txtCelular,
                telefone_recado: txtRecado,
                fk_cargo: txtCargo,
                senha: txtSenha,
                logradouro: txtLogradouro,
                numero: txtNumero,
                bairro: txtBairro,
                municipio: txtMunicipio,
                cep: txtCep,
                estado: txtEstado,
            },
            type: 'POST',
            url: '/funcionario/store'

        })
            .done(function (data) {

                if (data.error) {
                    $('#errorAlert').text(data.error).show();
                    $('#successAlert').hide();
                } else {
                    $('#successAlert').text(data.success).show();
                    $('#errorAlert').hide();
                }

            });

        /* Função para subir a tela após a tentativa de cadastro */

        $('html, body').animate({ scrollTop: 0 }, 1200);
        event.stopPropagation();

        /* Função para esconder as mensagens do cadastro após 2.5s */

        setTimeout(function () {
            $('#successAlert').hide();
        }, 2500);

        setTimeout(function () {
            $('#errorAlert').hide();
        }, 2500);

        /* Função para resetar os inputs do formulário após o cadastro */

        $('#form_cad_func').each (function(){
            this.reset();
        });

    }

}

/* ---------------------------------------------------
    Cadastro de Assistido
----------------------------------------------------- */

function cadAssistido() {


    var txtNome = $('#txtNome').val();
    var txtNomeMae = $('#txtNomeMae').val();
    var txtNomePai = $('#txtNomePai').val();
    var txtNomeResponsavel = $('#txtNomeResponsavel').val();
    var txtCpf = $('#txtCpf').val();
    var txtRg = $('#txtRg').val();
    var txtDataNasc = $('#txtDataNasc').val();
    var txtIdade = $('#txtIdade').val();
    var txtSexo = $('#selectSexo').val();
    var txtCelular = $('#txtCelular').val();
    var txtRecado = $('#txtRecado').val();
    var txtCertidaoNasc = $('#txtCertidaoNasc').val();
    var txtLogradouro = $('#txtLogradouro').val();
    var txtNumero = $('#txtNumero').val();
    var txtBairro = $('#txtBairro').val();
    var txtMunicipio = $('#txtMunicipio').val();
    var txtCep = $('#txtCep').val();
    var txtEstado = $('#txtEstado').val();
    var txtDataCadastro = $('#txtDataCadastro').val();
    var txtHoraCadastro = $('#txtHoraCadastro').val();
    

    /* O Trecho abaixo verifica se os inputs com a classe "required_func" estão preenchidos */


    var inputs = document.getElementsByClassName('required_assistido');
    var len = inputs.length;
    var valid = true;
    for (var i = 0; i < len; i++) {
        if (!inputs[i].value) {
            valid = false;
            inputs[i].style.border = '1px solid';
            inputs[i].style.borderColor = 'red';
        } else {
            inputs[i].style.border = 'none';
        }
    }
    if (valid) {

        $.ajax({
            data: {                
                nome_assistido: txtNome,
                nome_mae: txtNomeMae,
                nome_pai: txtNomePai,
                nome_responsavel: txtNomeResponsavel,
                cpf: txtCpf,
                rg: txtRg,
                data_nasc: txtDataNasc,
                idade: txtIdade,
                sexo: txtSexo,
                celular: txtCelular,
                recado: txtRecado,
                cert_nasc: txtCertidaoNasc,
                logradouro: txtLogradouro,
                numero: txtNumero,
                bairro: txtBairro,
                municipio: txtMunicipio,
                cep: txtCep,
                estado: txtEstado,
                data_cad: txtDataCadastro,
                hora_cad: txtHoraCadastro
            },
            type: 'POST',
            url: '/assistido/store'

        })
            .done(function (data) {

                if (data.error) {
                    $('#errorAlertAssistido').text(data.error).show();
                    $('#successAlertAssistido').hide();
                } else {
                    $('#successAlertAssistido').text(data.success).show();
                    $('#errorAlertAssistido').hide();
                }

            });

        /* Função para subir a tela após a tentativa de cadastro */

        $('html, body').animate({ scrollTop: 0 }, 1200);
        event.stopPropagation();

        /* Função para esconder as mensagens do cadastro após 2.5s */

        setTimeout(function () {
            $('#successAlertAssistido').hide();
        }, 2500);

        setTimeout(function () {
            $('#errorAlertAssistido').hide();
        }, 2500);

        /* Função para resetar os inputs do formulário após o cadastro */

        $('#form_cad_assistido').each (function(){
            this.reset();
        });

    }

}

/* ---------------------------------------------------
    Pesquisa de Assistido
----------------------------------------------------- */


function pesqAssistido() {
    

    if ($('#txtCpf').val() == '') {
        $('#txtCpf').css('border','1px solid');
        $('#txtCpf').css('borderColor','red'); 

    } else {

        var txtCpf = $('#txtCpf').val();       

        $.ajax({
            data: { 
                cpf: txtCpf
            },
            type: 'POST',
            url: '/assistido/search_assistido',
            success: function(resp) {  
                $('div#response').css('display', 'block');           
                $('div#response').html(resp.data);                
                //$('div#response').append(resp.data);
            }
        })          
            .done(function (data) {

                if (data.error) {
                    $('div#response').css('display', 'none');
                    $('#errorAlertAssistido').text(data.error).show();
                }

            });

        setTimeout(function () {
            $('#errorAlertAssistido').hide();
        }, 2500);

    }

}


/* ---------------------------------------------------
    Agendamentos
----------------------------------------------------- */

/* Este método retornará o assistido caso ele exista nos registros */

function pesqAssistidoAgendamento() {
    

    if ($('#txtCpf').val() == '') {
        $('#txtCpf').css('border','1px solid');
        $('#txtCpf').css('borderColor','red'); 

    } else {

        var txtCpf = $('#txtCpf').val();
        
        $.ajax({
            data: { 
                cpf: txtCpf
            },
            type: 'POST',
            url: '/agendamento/search_assistido_agendamento',
            success: function(resp) {  
                $('div#response').css('display', 'block');           
                $('div#response').html(resp.data);   
            }
        })          
            .done(function (data) {

                if (data.error) {
                    $('div#response').css('display', 'none');
                    $('#errorAlertAssistido').text(data.error).show();
                }

            });

        setTimeout(function () {
            $('#errorAlertAssistido').hide();
        }, 2500);

    }

}


function cadAgendamento() {

    var txtId = $('#txtId').val();
    var txtFkFuncionario = $('#selectMedico').val();   
    var txtDataAgendamento = $('#txtDataAgendamento').val();
    var txtHoraInicio = $('#txtHoraInicio').val();
    var txtHoraFim = $('#txtHoraFim').val(); 
    var txtObservacoes = $('#txtObservacoes').val(); 


    /* O Trecho abaixo verifica se os inputs com a classe "required_agendamento" estão preenchidos */


    var inputs = document.getElementsByClassName('required_agendamento');
    var len = inputs.length;
    var valid = true;
    for (var i = 0; i < len; i++) {
        if (!inputs[i].value) {
            valid = false;
            inputs[i].style.border = '1px solid';
            inputs[i].style.borderColor = 'red';
        } else {
            inputs[i].style.border = 'none';
        }
    }
    if (valid) {

        $.ajax({
            data: {    
                fk_assistido: txtId,  
                fk_funcionario: txtFkFuncionario,
                data_agendamento: txtDataAgendamento,
                hora_inicio: txtHoraInicio,
                hora_fim: txtHoraFim,
                observacoes: txtObservacoes                
            },
            type: 'POST',
            url: '/agendamento/store',
        })
            .done(function (data) {

                if (data) {
                    $('div#response').css('display', 'none'); 
                    $('#successAlertAssistido').text(data.success).show();
                } 

            });

        /* Função para esconder as mensagens do cadastro após 2.5s */

        setTimeout(function () {
            $('#successAlertAssistido').hide();
        }, 2500);


    }

}

/* Este método retornará os agendamentos caso o assistido exista nos registros */

function pesqAgendamento() {
    

    if ($('#txtCpf').val() == '') {
        $('#txtCpf').css('border','1px solid');
        $('#txtCpf').css('borderColor','red'); 

    } else {

        var txtCpf = $('#txtCpf').val();
        
        $.ajax({
            data: { 
                cpf: txtCpf
            },
            type: 'POST',
            url: '/agendamento/search_agendamento',
            success: function(resp) {  
                $('div#todos_agendamentos').css('display', 'none');
                $('div#response').css('display', 'block');    
                $('div#response').html(resp.success);   
            }
        })          
            .done(function (data) {

                if (data.error) {                    
                    $('div#todos_agendamentos').css('display', 'none');
                    $('div#response').css('display', 'none');
                    $('#errorAlertAssistido').text(data.error).show();
                }

            });

        setTimeout(function () {
            $('#errorAlertAssistido').hide();
        }, 2500);

    }

}