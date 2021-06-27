import sqlite3
from flask import Flask, jsonify, render_template, url_for, session, escape
from flask import redirect, request


############################
# ABRINDO CONEXÃO COM O DB #
############################

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)
app.secret_key = 'secrekeyssocial'


@app.route("/")


@app.route("/login")
def login():

    if 'cpf' in session:
        return render_template('home.html')
    else:
        return render_template('login.html')
 
# Retornar dados do banco e exibir no template:
# def index():
#    conn = get_db_connection()
#    func = conn.execute('SELECT * FROM `funcionario`').fetchall()
#    conn.close()
#    return render_template('index.html', func=func)


################
# AUTENTICAÇÃO #
################

@app.route('/auth', methods=['POST'])
def auth():

    if request.method == 'POST':

        cpf = request.form['cpf']
        password = request.form['password']

        conn = get_db_connection()
        func = conn.execute(
            'SELECT * FROM `funcionario` WHERE cpf = ? AND senha = ?', (cpf, password,)).fetchone()
        conn.close()

        if (func is None):
            return jsonify({'error': 'Login e/ou senha incorretos'})
        else:
            session['cpf'] = cpf
            return redirect('/home')


# ------------------------------------------------------------------


################
#    LOGOUT    #
################

@app.route("/logout", methods=['GET', 'POST'])
def logout():

    if request.method == 'GET':
        session.clear()
        return redirect(url_for('login'))
    return render_template('login.html')


# ------------------------------------------------------------------


@app.route("/home", methods=['GET', 'POST'])
def home():

    if 'cpf' in session:
        return render_template('home.html')
    else:
        print('Você não está logado!')
        return render_template('login.html')

# ------------------------------------------------------------------


@app.route("/scheduling")
def scheduling():

    if 'cpf' in session:
        return render_template('scheduling.html')
    else:
        return render_template('login.html')

# ------------------------------------------------------------------


@app.route("/contacts")
def contacts():

    if 'cpf' in session:
        return render_template('contacts.html')
    else:
        return render_template('login.html')

# ------------------------------------------------------------------


@app.route("/about")
def about():

    if 'cpf' in session:
        return render_template('about.html')
    else:
        return render_template('login.html')


# ------------------------------------------------------------------


###############
#  ASSISTIDO  #
###############


@app.route("/assistido/add")
def assistido_register():

    if 'cpf' in session:
        return render_template('assistido/register.html', title='Register')
    else:
        return render_template('login.html')


@app.route("/assistido/store", methods=['POST'])
def assistido_store():

    if 'cpf' in session:

        # Salvando os dados de endereço do assistido 

        txtLogradouro = request.form['logradouro']
        txtNumero = request.form['numero']
        txtBairro = request.form['bairro']
        txtMunicipio = request.form['municipio']
        txtCep = request.form['cep']
        txtEstado = request.form['estado']
        
        form_endereco_values = (txtLogradouro, txtNumero, txtBairro, txtMunicipio, txtCep, txtEstado)

        conn = get_db_connection()
        sql = conn.execute("INSERT INTO `endereco` (`logradouro`, `numero`, `bairro`, `municipio`, `cep`, `uf`) VALUES (?, ?, ?, ?, ?, ?)", form_endereco_values)
        conn.commit()
        conn.close()

        # Retornando o endereço cadastrado para pegar o ID 

        conn = get_db_connection()
        sql = conn.execute("SELECT id_cargo FROM `cargo` ORDER BY id_cargo DESC LIMIT 1").fetchone()

        for conteudo in sql:
            fk_endereco = conteudo

        conn.commit()
        conn.close()

        txtNomeMae = request.form['nome_mae']
        txtNome = request.form['nome_assistido']
        txtNomePai = request.form['nome_pai']
        txtNomeResponsavel = request.form['nome_responsavel']
        txtCpf = request.form['cpf']
        txtRg = request.form['rg']
        txtDataNasc = request.form['data_nasc']
        txtIdade = request.form['idade']
        txtSexo = request.form['sexo']
        txtCelular = request.form['celular']
        txtRecado = request.form['recado']
        txtCertidaoNasc = request.form['cert_nasc']
        txtDataCadastro = request.form['data_cad']
        txtHoraCadastro = request.form['hora_cad']

        form_values = (txtNome, txtCertidaoNasc, txtRg, txtCpf, txtDataNasc, txtIdade, txtSexo, txtNomeMae, txtNomePai, txtNomeResponsavel, txtDataCadastro, txtHoraCadastro, txtRecado, txtCelular, fk_endereco)

        conn = get_db_connection()
        sql_assistido = conn.execute("INSERT INTO `assistido` (`nome`, `cert_nasc`, `rg`, `cpf`, `data_nasc`, `idade`, `sexo`, `nome_mae`, `nome_pai`, `nome_responsavel`, `dt_cadastro`, `hr_cadastro`, `telefone_recado`, `telefone1`, `fk_endereco`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", form_values)
        conn.commit()
        conn.close()       


        if sql_assistido is None:
            return jsonify({'error': 'Não foi possível cadastrar o assistido'})
        else:
            return jsonify({'success': 'Assistido cadastrado com sucesso'})

    else:
        session.clear()
        return redirect(url_for('login'))


# ------------------------------------------------------------------


@app.route("/assistido/search")
def assistido_search():

    if 'cpf' in session:
        return render_template('assistido/search.html', title='Search')
    else:
        return render_template('login.html')


# ------------------------------------------------------------------


@app.route("/assistido/search_assistido", methods=['POST', 'GET'])
def search_assistido():    

    if 'cpf' in session:   

        txtCpf = request.form['cpf']

        conn = get_db_connection()
        sql_pesq_assistido = conn.execute('SELECT * FROM `assistido` as a, `endereco` as e WHERE a.fk_endereco = e.id_endereco AND a.cpf = ?', (txtCpf,)).fetchone()
        conn.close()

        if sql_pesq_assistido is not None:
            return jsonify({'data': render_template('/assistido/search_result.html', sql_pesq=sql_pesq_assistido)})
        else:
            return jsonify({'error': 'Nenhum resultado encontrado'})    
    

# ------------------------------------------------------------------


@app.route("/assistido/record")
def assistido_record():

    if 'cpf' in session:
        return render_template('assistido/record.html', title='Medial Record')
    else:
        return render_template('login.html')


# ------------------------------------------------------------------


###############
# FUNCIONÁRIO #
###############


@app.route("/funcionario/add")
def funcionario_add():

    if 'cpf' in session:
        return render_template('funcionario/register.html', title='Register')
    else:
        return render_template('login.html')


# ------------------------------------------------------------------


# -----------------------
# Cadastrar funcionários
# -----------------------

@app.route("/funcionario/store", methods=['POST'])
def func_store():

    if 'cpf' in session:

        # Salvando os dados de endereço do assistido 

        txtLogradouro = request.form['logradouro']
        txtNumero = request.form['numero']
        txtBairro = request.form['bairro']
        txtMunicipio = request.form['municipio']
        txtCep = request.form['cep']
        txtEstado = request.form['estado']
        
        form_endereco_values = (txtLogradouro, txtNumero, txtBairro, txtMunicipio, txtCep, txtEstado)

        conn = get_db_connection()
        sql = conn.execute("INSERT INTO `endereco` (`logradouro`, `numero`, `bairro`, `municipio`, `cep`, `uf`) VALUES (?, ?, ?, ?, ?, ?)", form_endereco_values)
        conn.commit()
        conn.close()

        # Retornando o endereço cadastrado para pegar o ID 

        conn = get_db_connection()
        sql = conn.execute("SELECT id_cargo FROM `cargo` ORDER BY id_cargo DESC LIMIT 1").fetchone()

        for conteudo in sql:
            fk_endereco = conteudo

        conn.commit()
        conn.close()


        nome_func = request.form['nome_func']
        cpf = request.form['cpf']
        rg = request.form['rg']
        data_nasc = request.form['data_nasc']
        idade = request.form['idade']
        sexo = request.form['sexo']
        telefone1 = request.form['telefone1']
        telefone_recado = request.form['telefone_recado']
        fk_cargo = request.form['fk_cargo']
        senha = request.form['senha']

        form_values = (nome_func, cpf, rg, data_nasc, idade, sexo, telefone1, telefone_recado, fk_cargo, senha, fk_endereco)

        conn = get_db_connection()
        sql_func = conn.execute("INSERT INTO `funcionario` (`nome_func`, `cpf`, `rg`, `data_nasc`, `idade`, `sexo`, `telefone1`, `telefone_recado`, `fk_cargo`, `senha`, `fk_endereco`) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", form_values)
        conn.commit()
        conn.close()

        if sql_func is None:
            return jsonify({'error': 'Não foi possível cadastrar o funcionário'})
        else:
            return jsonify({'success': 'Funcionário cadastrado com sucesso'})

    else:
        session.clear()
        return redirect(url_for('login'))


@app.route("/funcionario/search")
def funcionario_search():

    if 'cpf' in session:
        return render_template('funcionario/search.html', title='Search')
    else:
        return render_template('login.html')


# ------------------------------------------------------------------


###############
# AGENDAMENTO #
###############


@app.route("/agendamento/add")
def agendamento_add():

    if 'cpf' in session:
        return render_template('agendamento/register.html', title='Register')
    else:
        return render_template('login.html')


# ------------------------------------------------------------------


@app.route("/agendamento/store", methods=['POST', 'GET'])
def agendamento_store():

    if 'cpf' in session:

        txtId = request.form['fk_assistido']
        txtFkFuncionario = request.form['fk_funcionario']
        txtDataAgendamento = request.form['data_agendamento']
        txtHoraInicio = request.form['hora_inicio']
        txtHoraFim = request.form['hora_fim']
        txtStatus = 'pendente'
        txtObservacoes = request.form['observacoes']
        
        form_agendamento = (txtId, txtFkFuncionario, txtDataAgendamento, txtHoraInicio, txtHoraFim, txtStatus, txtObservacoes)

        conn = get_db_connection()
        sql_agendamento = conn.execute("INSERT INTO `agendamento` (`fk_assistido`, `fk_funcionario`, `data_agendamento`, `hora_inicio`, `hora_fim`, `status`, `observacao`) VALUES (?, ?, ?, ?, ?, ?, ?)", form_agendamento)
        conn.commit()
        conn.close()

        if sql_agendamento is None:
            return jsonify({'error': 'Não foi possível agendar'})
        else:
            return jsonify({'success': 'Agendamento cadastrado com sucesso'})

    else:
        session.clear()
        return redirect(url_for('login'))


# ------------------------------------------------------------------


@app.route("/agendamento/search")
def agendamento_search():

    if 'cpf' in session:
        
        conn = get_db_connection()        
        sql_pesq_agendamento = conn.execute("SELECT ag.data_agendamento, ag.status, assi.nome FROM `agendamento` ag, `assistido` as assi WHERE fk_assistido = id").fetchall()        
        conn.close()        

        if sql_pesq_agendamento is not None:            
            return render_template('/agendamento/search.html', sql_pesq=sql_pesq_agendamento)



# ------------------------------------------------------------------

#  A rota abaixo verifica se o assistido está registrado e também obtém
#  a lista de médicos registrados

@app.route("/agendamento/search_assistido_agendamento", methods=['POST', 'GET'])
def search_assistido_agendamento():    

    if 'cpf' in session:   

        txtCpf = request.form['cpf']
        
        conn = get_db_connection()        
        sql_pesq_assistido = conn.execute('SELECT * FROM `assistido` WHERE cpf = ?', (txtCpf,)).fetchone()        
        conn.close()

        conn2 = get_db_connection()
        sql_pesq_func = conn2.execute('SELECT * FROM `funcionario`, `cargo` WHERE fk_cargo = id_cargo AND fk_cargo = 3 ORDER BY `nome_func`').fetchall()
        conn2.close()
        

        if sql_pesq_assistido is not None:            
            return jsonify({'data': render_template('/agendamento/register_continue.html', sql_pesq=sql_pesq_assistido, sql_pesq_func=sql_pesq_func)})
        else:
            return jsonify({'error': 'Nenhum resultado encontrado'})


# ------------------------------------------------------------------


@app.route("/agendamento/search_agendamento", methods=['POST'])
def search_agendamento():    

    if 'cpf' in session:   

        txtCpf = request.form['cpf']        

        conn = get_db_connection()        
        sql_pesq_assistido = conn.execute('SELECT id FROM `assistido` WHERE cpf = ?', (txtCpf,)).fetchone()        
        conn.close()

        fk_assistido = 0

        if sql_pesq_assistido is not None:
            for a in sql_pesq_assistido:
                fk_assistido = a
        
        conn2 = get_db_connection()        
        sql_pesq_agendamento = conn2.execute('SELECT ag.data_agendamento, ag.status, assi.nome FROM `agendamento` ag, `assistido` as assi WHERE id = fk_assistido AND fk_assistido = ?', (fk_assistido,)).fetchone()        
        conn2.close()        


        if sql_pesq_agendamento is not None and fk_assistido != 0:  
            return jsonify({'success': render_template('/agendamento/search_continue.html', sql_pesq=sql_pesq_agendamento)})
        else:
            return jsonify({'error': 'Nenhum resultado encontrado'})
            


if __name__ == '__main__':
    app.run(debug=True)
