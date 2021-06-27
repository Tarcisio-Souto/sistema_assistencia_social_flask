import sqlite3

connection = sqlite3.connect('database.db')

with open('ssocial.sql', encoding="utf-8") as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO `cargo` (`nome_cargo`) VALUES ('Assistente Social'),('Recepcionista'), ('Médico')")
cur.execute("INSERT INTO `endereco` (`logradouro`, `numero`, `bairro`, `municipio`, `cep`, `uf`) VALUES ('Av. Fernando Ferrari', '2115', 'Goiabeiras', 'Vitória' , '29075-905', 'ES')")
cur.execute("INSERT INTO `funcionario` (`nome_func`, `cpf`, `rg`, `data_nasc`, `idade`, `sexo`,  `telefone1`, `telefone_recado`, `fk_cargo`, `senha`, `fk_endereco`) VALUES ('admin', '999.999.999-00', '0000000', '1993-02-26', '28', 'm', '995901992', '33229096', '1', 'admin@2021', '1')")

connection.commit()
connection.close()