import spacy

# Carregar modelo de linguagem em português
nlp = spacy.load("pt_core_news_sm")

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

def extrair_informacao(mensagem, intencao):
    # ... (substitua por código para extrair informações relevantes)
    print('a')

def main():
    # Obter a mensagem do cliente
    mensagem = json.loads(input())["mensagem"]

    # Analisar a intenção da mensagem
    intencao = analisar_intencao(mensagem)

    # Extrair informações relevantes da mensagem
    informacao = extrair_informacao(mensagem, intencao)

    # Retornar o resultado como JSON
    print(json.dumps({"intencao": intencao, "informacao": informacao}))

if __name__ == "__main__":
    main()
