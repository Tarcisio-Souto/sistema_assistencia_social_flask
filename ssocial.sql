-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 09-Maio-2021 às 20:33
-- Versão do servidor: 10.4.18-MariaDB
-- versão do PHP: 7.4.16

--
-- Estrutura da tabela `endereco`
--

DROP TABLE IF EXISTS endereco;

CREATE TABLE `endereco` (
  `id_endereco` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `logradouro` varchar(100) DEFAULT NULL,
  `numero` varchar(10) DEFAULT NULL,
  `bairro` varchar(100) DEFAULT NULL,
  `municipio` varchar(100) DEFAULT NULL,
  `cep` varchar(45) DEFAULT NULL,
  `uf` varchar(2) DEFAULT NULL
);

-- --------------------------------------------------------

DROP TABLE IF EXISTS assistido;

CREATE TABLE `assistido` (
  `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `cert_nasc` varchar(100) DEFAULT NULL,
  `idade` INTEGER DEFAULT NULL,
  `sexo` CHAR DEFAULT NULL,
  `rg` INTEGER DEFAULT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `data_nasc` date DEFAULT NULL,
  `nome_mae` varchar(100) DEFAULT NULL,
  `nome_pai` varchar(100) DEFAULT NULL,
  `nome_responsavel` varchar(100) DEFAULT NULL,
  `telefone_recado` varchar(45) DEFAULT NULL,
  `telefone1` varchar(45) DEFAULT NULL,
  `dt_cadastro` date DEFAULT NULL,
  `hr_cadastro` time DEFAULT NULL,
  `fk_endereco` INTEGER NOT NULL,
  FOREIGN KEY (`fk_endereco`) REFERENCES `endereco` (`id_endereco`)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela `cargo`
--

DROP TABLE IF EXISTS cargo;

CREATE TABLE `cargo` (
  `id_cargo` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `nome_cargo` varchar(100)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela `funcionario`
--

DROP TABLE IF EXISTS funcionario;

CREATE TABLE `funcionario` (
  `id_funcionario` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `nome_func` varchar(100) DEFAULT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `rg` varchar(7) DEFAULT NULL,
  `data_nasc` date DEFAULT NULL,
  `idade` INTEGER DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL,
  `telefone_recado` varchar(45) DEFAULT NULL,
  `telefone1` varchar(45) DEFAULT NULL,
  `senha` varchar(100),
  `fk_endereco` INTEGER NOT NULL,  
  `fk_cargo` INTEGER NOT NULL,
  FOREIGN KEY (`fk_endereco`) REFERENCES `endereco` (`id_endereco`),
  FOREIGN KEY (`fk_cargo`) REFERENCES `cargo` (`id_cargo`)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela `prontuario`
--

DROP TABLE IF EXISTS prontuario;

CREATE TABLE `prontuario` (
  `id_prontuario` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `fk_assistido` INTEGER NOT NULL,
  FOREIGN KEY (`fk_assistido`) REFERENCES `assistido` (`id_assistido`)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela `anamnese`
--

DROP TABLE IF EXISTS anamnese;

CREATE TABLE `anamnese` (
  `id_anamnese` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `peso` varchar(10),
  `altura` varchar(10),
  `imc` varchar(10),
  `medicamentos` text,
  `observacao` text,
  `quest1` tinyint,
  `quest2` tinyint,
  `quest3` tinyint,
  `quest4` tinyint,
  `quest5` tinyint,
  `quest6` tinyint,
  `quest7` tinyint,
  `quest8` tinyint,
  `quest9` tinyint,
  `quest10` tinyint,
  `fk_prontuario` INTEGER,
  FOREIGN KEY (`fk_prontuario`) REFERENCES `prontuario` (`id_prontuario`)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela `agendamento`
--

DROP TABLE IF EXISTS agendamento;

CREATE TABLE `agendamento` (
  `id_agendamento` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `fk_funcionario` INTEGER NOT NULL,
  `fk_assistido` INTEGER NOT NULL,
  `data_agendamento` date,
  `hora_inicio` TIME,
  `hora_fim` TIME,
  `status` varchar(45) DEFAULT NULL,
  `observacao` TEXT,  
  FOREIGN KEY (`fk_funcionario`) REFERENCES `funcionario` (`id_funcionario`),
  FOREIGN KEY (`fk_assistido`) REFERENCES `assistido` (`id_assistido`)
);

-- --------------------------------------------------------

--
-- Estrutura da tabela `fila_espera`
--

DROP TABLE IF EXISTS fila_espera;

CREATE TABLE `fila_espera` (
  `id_fila` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  `fk_prontuario` INTEGER NOT NULL,
  `data_registro` date,
  `status` varchar(45) DEFAULT NULL,
  `observacao` TEXT,
  FOREIGN KEY (`fk_prontuario`) REFERENCES `prontuario` (`id_prontuario`)
);

