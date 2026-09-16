
CATEGORIAS = [
    {"slug": "barras", "nome": "Barras", "emoji": ""},
    {"slug": "trufas", "nome": "Trufas", "emoji": ""},
    {"slug": "presentes", "nome": "Presentes", "emoji": ""},
    {"slug": "kits", "nome": "Kits", "emoji": ""},
    {"slug": "premium", "nome": "Linha Premium", "emoji": ""},
    {"slug": "promocoes", "nome": "Promoções", "emoji": ""},
]

PRODUTOS = [
    {
        "id": 1,
        "nome": "Barra de Chocolate ao Leite 90g",
        "preco": 12.90,
        "preco_antigo": 16.90,
        "tag": ["Oferta"],
        "emoji": "🍫",
        "imagem": "barra-ao-leite.jpg",
        "categoria": ["barras", 'premium'],
        "descricao": "Nossa clássica barra de chocolate ao leite cremosa, feita com grãos selecionados de cacau de origem sustentável."
    },
    {
        "id": 2,
        "nome": "Caixa de Bombons Sortidos 250g",
        "preco": 39.90,
        "preco_antigo": None,
        "tag": ["Novo", "Presente", "Mais vendido"],
        "emoji": "🎁",
        "imagem": "caixa-bombons.jpg",
        "categoria": ["presentes", "premium"],
        "descricao": "Uma seleção artesanal de bombons trufados com recheios sortidos: avelã, caramelo salgado e licor."
    },
    {
        "id": 3,
        "nome": "Trufa de Chocolate Belga 30g",
        "preco": 6.50,
        "preco_antigo": None,
        "tag": ["Mais vendido"],
        "emoji": "🍬",
        "imagem": "trufa-belga.jpg",
        "categoria": ["trufas"],
        "descricao": "Deliciosa trufa feita com autêntico chocolate belga 54% e polvilhada com cacau em pó 100% puro."
    },
    {
        "id": 4,
        "nome": "Ovo de Páscoa Recheado 350g",
        "preco": 59.90,
        "preco_antigo": 74.90,
        "tag": ["Promoção"],
        "emoji": "🥚",
        "imagem": None, # Exemplo sem imagem -> fallback para o emoji
        "categoria": ["promocoes"],
        "descricao": "Ovo artesanal de chocolate meio amargo recheado com camadas generosas de brigadeiro gourmet."
    },
    {
        "id": 5,
        "nome": "Tablete Chocolate 70% Cacau 100g",
        "preco": 18.90,
        "preco_antigo": None,
        "tag": None,
        "emoji": "🍫",
        "imagem": "tablete-70.jpg",
        "categoria": ["barras"],
        "descricao": "Para os amantes de cacau intenso. Sabor marcante, notas frutadas e zero adição de gorduras hidrogenadas."
    },
    {
        "id": 6,
        "nome": "Cesta Chocolates Premium",
        "preco": 89.90,
        "preco_antigo": 109.90,
        "tag": ["Presente"],
        "emoji": "🧺",
        "imagem": "exemplo.webp",
        "categoria": ["kits"],
        "descricao": "O presente perfeito: reúne nossas melhores barras, trufas especiais e uma caixa exclusiva BrasZela."
    },
    {
        "id": 7,
        "nome": "Chocolate Branco com Morango 90g",
        "preco": 14.90,
        "preco_antigo": None,
        "tag": ["Novo"],
        "emoji": "🍓",
        "imagem": "exemplo.webp",
        "categoria": ["barras"],
        "descricao": "Cremoso chocolate branco combinado com pedaços crocantes de morango desidratado."
    },
    {
        "id": 8,
        "nome": "Kit Degustação 5 Sabores",
        "preco": 49.90,
        "preco_antigo": None,
        "tag": ["Kit"],
        "emoji": "🍫",
        "imagem": "exemplo.webp",
        "categoria": ["kits"],
        "descricao": "Explore a diversidade BrasZela com 5 minitabletes em porcentagens e sabores variados."
    },
]