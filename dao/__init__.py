import psycopg2
#objeto de acesso aos dados
def conectardb():

    con = psycopg2.connect(
        #host='localhost',
        #database = '3anoifpb',
        #user = 'postgres',
        #password = '12345'

        host = 'dpg-cu798q23esus73fhp800-a.oregon-postgres.render.com',
        database = 'projetodaminhavida',
        user = 'projetodaminhavida_user',
        password = 'KQnjL1KdQ0Zsx2rn75FKcf4FAh7WVSt5'
    )
    return con


def login(user,senha):
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT  nome, matricula from usuarios where matricula='{user}' and senha='{senha}'  "
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida

def inserir_user(nome, login, senha):

    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"INSERT INTO usuario (nome, login, senha) VALUES ('{nome}','{login}','{senha}')"
        cur.execute(sql)

    except psycopg2.IntegrityError:
        #volta que deu ruim
        conn.rollback()
        exito = False
    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()
    return exito

def listar_usuarios():
    con = conectardb()
    cur = con.cursor()
    sql = f"SELECT  nome, matricula from usuarios"
    cur.execute(sql)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida

