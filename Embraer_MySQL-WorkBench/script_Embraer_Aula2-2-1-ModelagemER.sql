-- script_Embraer_MySQLWorkBrench_LogicalModel_Aula2-2-1-ModelagemER_Mod01FundBD


-- criar Empregados 1
create Empregados(
empregados_id INT,
nome, sobrenome VARCHAR(45),
e-mail varchar(45),
data_admissão DATE(80),
salario DECIMAL(9),
departamentos_departamentos_id INT,
cargos_cargo_id INT
);

-- criar Departamentos

create Departamentos(
departamentos_id int,
departamento_nome varchar(),
localidades_idlocalidades int
);

-- criar Cargos
create Cargos(
cargo_id INT,
cargo_nome VARCHAR(55);
);

-- criar Cargo_histórico
create cargo_histórico(
cargo_histórico_id INT,
data_inicio VARCHAR(),
data_fim VARCHAR(),
cargos_cargo_id INT,
empregados_empregados_id INT
);

-- criar Localidades
create Localidades(
localidades_id INT,
estado VARCHAR(30),
endereco VARCHAR(4000),
cidade VARCHAR(100)
);

-- criar Países
create Paises(
paises_id INT,
pais_nome VARCHAR(45),
regioes_regioes_id INT
);
