import sqlite3
from datetime import datetime

#conexão com o banco
conn = sqlite3.connect("loja.db")
cursor = conn.cursor()

#ddl (criação das tabelas)

cursor.execute("drop table if exists itens_pedido;")
cursor.execute("drop table if exists pedidos;")
cursor.execute("drop table if exists produtos;")
cursor.execute("drop table if exists clientes;")

cursor.execute("""
create table clientes (
    id integer primary key autoincrement,
    nome text not null,
    email text not null unique
);
""")

cursor.execute("""
create table produtos (
    id integer primary key autoincrement,
    nome text not null,
    preco real not null,
    estoque integer not null
);
""")

cursor.execute("""
create table pedidos (
    id integer primary key autoincrement,
    data_compra text not null,
    total real not null,
    id_cliente integer not null,
    foreign key (id_cliente) references clientes(id)
);
""")

cursor.execute("""
create table itens_pedido (
    id integer primary key autoincrement,
    id_pedido integer not null,
    id_produto integer not null,
    quantidade integer not null,
    foreign key (id_pedido) references pedidos(id),
    foreign key (id_produto) references produtos(id)
);
""")

print("tabelas criadas com sucesso!\n")

#CRUD
#inserir clientes
cursor.executemany(
    "insert into clientes (nome, email) values (?, ?)",
    [
        ("joão", "joao@gmail.com"),
        ("maria", "maria@gmail.com"),
        ("ana", "ana@gmail.com")
    ]
)

#inserir produtos
cursor.executemany(
    "insert into produtos (nome, preco, estoque) values (?, ?, ?)",
    [
        ("teclado", 120.00, 10),
        ("mouse", 80.00, 20),
        ("monitor", 850.90, 5)
    ]
)

#recuperar id da maria
cursor.execute("select id from clientes where nome = 'maria'")
id_maria = cursor.fetchone()[0]

#preços atuais
cursor.execute("select preco from produtos where nome = 'teclado'")
preco_teclado = cursor.fetchone()[0]

cursor.execute("select preco from produtos where nome = 'mouse'")
preco_mouse = cursor.fetchone()[0]

#total da compra
total = preco_teclado * 1 + preco_mouse * 2

#criar pedido
cursor.execute(
    "insert into pedidos (data_compra, total, id_cliente) values (?, ?, ?)",
    (datetime.now().isoformat(" "), total, id_maria)
)

id_pedido_maria = cursor.lastrowid

#inserir itens do pedido
cursor.executemany(
    "insert into itens_pedido (id_pedido, id_produto, quantidade) values (?, ?, ?)",
    [
        (id_pedido_maria, 1, 1),
        (id_pedido_maria, 2, 2)
    ]
)

conn.commit()
print("inserções realizadas!\n")

#READ
print("produtos com preço > 100:")
cursor.execute("select nome, preco from produtos where preco > 100")
print(cursor.fetchall(), "\n")

print("pedidos feitos pela maria:")
cursor.execute("""
select c.nome, p.id, p.data_compra
from pedidos p
join clientes c on p.id_cliente = c.id
where c.nome = 'maria'
""")
print(cursor.fetchall(), "\n")

#UPDATE
cursor.execute("update produtos set preco = preco * 1.10 where nome = 'mouse'")
cursor.execute("update produtos set estoque = estoque - 2 where nome = 'mouse'")
conn.commit()
print("updates realizados!\n")

#DELETE
cursor.execute("delete from clientes where nome = 'joão'")
cursor.execute("delete from itens_pedido where id_pedido = ? and id_produto = 1", (id_pedido_maria,))
conn.commit()
print("deletes realizados!\n")

#verificações
print("itens restantes do pedido da maria:")
cursor.execute("""
select p.nome, i.quantidade
from itens_pedido i
join produtos p on p.id = i.id_produto
where i.id_pedido = ?
""", (id_pedido_maria,))
print(cursor.fetchall(), "\n")

print("estoque atualizado:")
cursor.execute("select nome, estoque from produtos")
print(cursor.fetchall(), "\n")

conn.close()
print("Sistema encerrando.")