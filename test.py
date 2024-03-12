import spacy

# Carregar modelo de linguagem em português
nlp = spacy.load("pt_core_news_sm")

from spacy.matcher import Matcher

# Carregar modelo de linguagem em português
nlp = spacy.load("pt_core_news_sm")

# Adicionar padrões de correspondência para "Instagram" e "Facebook"
matcher = Matcher(nlp.vocab)
matcher.add("REDE_SOCIAL", [[{"LOWER": "instagram"}], [{"LOWER": "facebook"}]])
matcher.add("SERVICOS_MARKETING", [[{"LOWER": "tráfego"},{"LOWER": "pago"}], [{"LOWER": "gestão de redes sociais"}]])

# Definir intenções do cliente
intencoes = [
    "saudacao",
    "consulta",
    "reclamacao",
    "pedido_suporte",
    "solicitacao",
    "de_contato",
    "elogio",
    "pedido_orcamento",
    "marcacao_horario",
    "cancelamento_servico",
    "confirmacao_pagamento",
    "solicitacao_amostra",
    "feedback_experiencia",
    "pedido_recomendacao",
    "pedido_desconto",
    "cancelamento_assinatura",
    "solicitacao_informacao_adicional",
    "sugestao_melhoria",
    "feedback_produto_servico",
    "acompanhamento_pos_venda",
    "solicitacao_devolucao_troca"
    ]

# Função para analisar a mensagem do cliente e determinar a intenção
def analisar_intencao(mensagem):
    # Processar a mensagem usando spaCy
    doc = nlp(mensagem)
    
    # Inicializar variáveis para armazenar a intenção e a pontuação máxima
    intencao_detectada = None
    pontuacao_maxima = 0
    
    # Iterar sobre as intenções conhecidas
    for intencao in intencoes:
        # Calcular a similaridade entre a mensagem e a intenção
        similaridade = doc.similarity(nlp(intencao))
        
        # Se a similaridade for maior que a pontuação máxima atual, atualizar a intenção detectada
        if similaridade > pontuacao_maxima:
            pontuacao_maxima = similaridade
            intencao_detectada = intencao
    
    # Retornar a intenção detectada
    return intencao_detectada

# Exemplo de uso
mensagem_cliente = "Quero tráfego pago para o meu site."
intencao = analisar_intencao(mensagem_cliente)
print("Intenção detectada:", intencao)


# Função para extrair informações relevantes da mensagem
def extrair_informacao(mensagem, intencao):
    doc = nlp(mensagem)
    informacao_relevante = []
    
    if intencao == "consulta":
        # Exemplo de extração de entidade para consulta de informações
        entidades = [entidade.text for entidade in doc.ents if entidade.label_ == "INFORMACAO"]
        informacao_relevante.extend(entidades)
    elif intencao == "reclamacao":
        # Exemplo de extração de entidade para reclamação
        aspectos = [token.text for token in doc if token.pos_ == "NOUN"]
        informacao_relevante.extend(aspectos)
    elif intencao == "pedido_suporte":
        # Exemplo de extração de detalhes sobre o tipo de suporte necessário
        suporte = [token.text for token in doc if token.pos_ == "NOUN" or token.pos_ == "ADJ"]
        informacao_relevante.extend(suporte)
    elif intencao == "solicitacao_de_contato":
        # Exemplo de extração de informações de contato
        contatos = [token.text for token in doc if token.like_email or token.like_phone]
        informacao_relevante.extend(contatos)
    elif intencao == "elogio":
        # Exemplo de extração de aspectos específicos elogiados
        elogios = [token.text for token in doc if token.pos_ == "NOUN" or token.pos_ == "ADJ"]
        informacao_relevante.extend(elogios)
    elif intencao == "pedido_orcamento":
        matches = matcher(doc)
        for match_id, start, end in matches:
            informacao_relevante.append(doc[start:end].text)
        # Exemplo de extração de detalhes sobre os itens para os quais o cliente está solicitando um orçamento
        orcamento = [entidade.text for entidade in doc.ents if entidade.label_ == "PRODUTO" or entidade.label_ == "SERVICO"]
        informacao_relevante.extend(orcamento)
    elif intencao == "marcacao_horario":
        # Exemplo de extração de datas e horários para marcação de horário
        datas_horarios = [entidade.text for entidade in doc.ents if entidade.label_ == "DATE" or entidade.label_ == "TIME"]
        informacao_relevante.extend(datas_horarios)
    elif intencao == "pedido_servico":
        # Exemplo de extração de detalhes sobre o tipo de serviço solicitado
        servico = [token.text for token in doc if token.pos_ == "NOUN" or token.pos_ == "ADJ"]
        informacao_relevante.extend(servico)
    # Adicione mais casos conforme necessário para outras intenções
    
    # Retornar informações relevantes ou None se não houver
    return informacao_relevante or None


# Exemplo de uso
mensagem_cliente = "sobre Tráfego pago para meu site."
intencao = "pedido_orcamento"
informacao = extrair_informacao(mensagem_cliente, intencao)
print("Informação extraída:", informacao)
#codigo para solicitar mais informação com uma mensagem_do_cliente_nova
intencao = "pedido_orcamento"

mensagem_cliente_nova = "sobre Instagram/Facebook."
informacao = extrair_informacao(mensagem_cliente_nova, intencao)
print("Informação extraída:", informacao)

mensagem_cliente = "Tráfego."
intencao = "pedido_orcamento"
informacao = extrair_informacao(mensagem_cliente, intencao)
print("Informação extraída:", informacao)