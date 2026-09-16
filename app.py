import os
from flask import Flask, render_template, request, session, redirect, url_for, flash
from env import CATEGORIAS, PRODUTOS
app = Flask(__name__)
app.secret_key = "45o8h53iok453inhiro820bn8902v8v90sjd809hvavujac890vyaioncv89qdhd--fasd9823n-a=+-0sdk1!"


# Função auxiliar para injetar categorias e quantidade do carrinho em todos os templates
@app.context_processor
def inject_global_data():
    carrinho = session.get("carrinho", {})
    total_itens = sum(carrinho.values())
    return dict(categorias=CATEGORIAS, total_carrinho=total_itens)

@app.route("/")
def index():
    return render_template("index.html", produtos=PRODUTOS, usuario=session.get("usuario"), email=session.get("email"))

@app.route("/produto/<int:produto_id>")
def detalhe_produto(produto_id):
    produto = next((p for p in PRODUTOS if p["id"] == produto_id), None)
    if not produto:
        flash("Produto não encontrado.", "erro")
        return redirect(url_for('index'))
    
    relacionados = [p for p in PRODUTOS if produto["categoria"] in p["categoria"] and p["id"] != produto["id"]]
    return render_template("produto.html", produto=produto, relacionados=relacionados[:4])

@app.route("/categoria/<slug>")
def categoria(slug):
    cat_atual = next((c for c in CATEGORIAS if c["slug"] == slug), None)
    if not cat_atual:
        flash("Categoria não encontrada.", "erro")
        return redirect(url_for('index'))
    
    produtos_cat = [p for p in PRODUTOS if slug in p['categoria'] or (slug == 'promocoes' and p["tag"] == 'Promoção')]
    return render_template("categoria.html", categoria=cat_atual, produtos=produtos_cat)

@app.route("/busca")
def busca():
    q = request.args.get("q", "").strip()
    resultados = [p for p in PRODUTOS if q.lower() in p["nome"].lower()] if q else []
    return render_template("busca.html", produtos=resultados, busca=q)

# --- ROTAS DE CARRINHO ---

@app.route("/carrinho")
def carrinho():
    carrinho_session = session.get("carrinho", {})
    itens = []
    subtotal = 0.0

    for p_id_str, qtd in carrinho_session.items():
        produto = next((p for p in PRODUTOS if p["id"] == int(p_id_str)), None)
        if produto:
            total_item = produto["preco"] * qtd
            subtotal += total_item
            itens.append({
                "produto": produto,
                "quantidade": qtd,
                "total": total_item
            })

    frete = 0.0 if subtotal >= 99.0 or subtotal == 0 else 15.00
    total_geral = subtotal + frete

    return render_template("carrinho.html", itens=itens, subtotal=subtotal, frete=frete, total=total_geral)

@app.route("/carrinho/adicionar/<int:produto_id>", methods=["POST"])
def adicionar_carrinho(produto_id):
    carrinho_session = session.get("carrinho", {})
    p_id_str = str(produto_id)
    qtd = int(request.form.get("quantidade", 1))

    carrinho_session[p_id_str] = carrinho_session.get(p_id_str, 0) + qtd
    session["carrinho"] = carrinho_session
    flash("Produto adicionado ao carrinho!", "sucesso")
    return redirect(request.referrer or url_for('carrinho'))

@app.route("/carrinho/remover/<int:produto_id>")
def remover_carrinho(produto_id):
    carrinho_session = session.get("carrinho", {})
    p_id_str = str(produto_id)
    if p_id_str in carrinho_session:
        del carrinho_session[p_id_str]
        session["carrinho"] = carrinho_session
        flash("Item removido do carrinho.", "sucesso")
    return redirect(url_for('carrinho'))

# --- OUTRAS PÁGINAS ---

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        # Aqui você pode adicionar a lógica de autenticação real
        if email == 'admin@braszela.com.br' and senha == 'trabalho123':
            session['usuario'] = 'admin'
            session['email'] = email
            flash("Login realizado com sucesso!", "sucesso")
            return redirect(url_for('index'))
    return render_template("login.html")

@app.route("/institucional/<pagina>")
def institucional(pagina):
    titulos = {
        "quem-somos": "Quem Somos",
        "lojas": "Nossas Lojas",
        "atendimento": "Central de Atendimento",
        "trocas": "Trocas e Devoluções"
    }
    titulo = titulos.get(pagina, "Informações")
    return render_template("institucional.html", titulo=titulo, pagina=pagina)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')