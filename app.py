# Trabalho de Extensão - Inteligência Artificial para Devs
# Aluno: Lucas Druzian Rodrigues dos Santos
import time

class RoboAtendimentoBairro:
    def __init__(self, loja, tipo_negocio):
        self.loja = loja
        self.tipo_negocio = tipo_negocio
        
        # Dados do comércio local para o robô consultar
        self.dados_loja = {
            "funcionamento": "Segunda a sábado, das 08h às 19h.",
            "onde_fica": "Rua Principal da Comunidade, número 150.",
            "taxa_entrega": "Entregamos na comunidade toda de graça!",
            "formas_pagamento": "Aceitamos Pix, dinheiro e cartões de crédito/débito."
        }

    def responder_cliente(self, texto_usuario):
        # Deixa tudo em minúsculo para facilitar a busca por palavras-chave
        texto = texto_usuario.lower()
        time.sleep(0.5) # Simula o tempo de resposta da IA
        
        # Testando o que o usuário digitou
        if "horario" in texto or "hora" in texto or "quando abre" in texto or "fecha" in texto:
            return self.dados_loja["funcionamento"]
            
        elif "onde" in texto or "fica" in texto or "endereco" in texto or "local" in texto:
            return self.dados_loja["onde_fica"]
            
        elif "entrega" in texto or "leva" in texto or "frete" in texto:
            return self.dados_loja["taxa_entrega"]
            
        elif "pagar" in texto or "cartao" in texto or "pix" in texto or "dinheiro" in texto or "pagamento" in texto:
            return self.dados_loja["formas_pagamento"]
            
        else:
            return "Olá! Sou o assistente com IA. Não entendi muito bem, mas logo um atendente humano vai te responder!"

# Parte principal para rodar o teste no terminal
if __name__ == "__main__":
    bot = RoboAtendimentoBairro("Mercadinho do Bairro", "Comércio")
    
    print("=" * 50)
    print(f"SISTEMA INICIADO: {bot.loja}")
    print("=" * 50)
    
    # Perguntas para testar o funcionamento
    perguntas_teste = [
        "Qual o horário de funcionamento de vocês?",
        "Vocês fazem entrega na comunidade?",
        "Quais as formas de pagamento?"
    ]
    
    for p in perguntas_teste:
        print(f"\n[Cliente]: {p}")
        resposta = bot.responder_cliente(p)
        print(f"[Robô]: {resposta}")
        print("-" * 30)