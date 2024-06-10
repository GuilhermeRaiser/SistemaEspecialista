'''
FALTA FAZER
ifs das posições de acordo com os atributos:
Goleiro

Laterais
	Direito
	Esquerdo

Meias
	Meia Central
	Meia esquerda
	Meia direita
    Meias-atacantes

Pontas
	Pontas Direita
	Pontas Esquerda

Centroavantes
	Centroavantes Pivô
	Centroavantes Homem de área
	Centroavantes Falso 9

Variavéis de atributos que precisam ser criadas:
Finalização
Visão
Passe
Cruzamento
Posionamento tatico

Documentação:
Explicação da escala 0 a 5 para cada atributo:

Níveis de cada atributo:
1- Tempo de reação:
Definição: Habilidade de responder rapidamente a estímulos e situações imprevistas no jogo.

0: Reage lentamente a situações imprevistas, frequentemente perde duelos por não conseguir antecipar ações.
1: Reage com alguma lentidão, ocasionalmente falha em acompanhar jogadas rápidas.
2: Reage razoavelmente bem, mas ainda perde em algumas situações de pressão.
3: Reage bem à maioria das situações, conseguindo antecipar várias ações dos adversários.
4: Reage rapidamente, raramente é pego de surpresa, consegue interceptar e se adaptar às mudanças de jogo.
5: Reage de forma excepcional, antecipar jogadas com precisão e tem uma leitura de jogo impecável.

2 - Aceleração:
Definição: Capacidade de aumentar a velocidade rapidamente ao iniciar uma corrida.

0: Muito lento nos arranques, incapaz de ganhar velocidade rapidamente.
1: Lento na aceleração, geralmente superado por adversários mais rápidos.
2: Acelera de forma moderada, suficiente para acompanhar o jogo, mas sem destaque.
3: Acelera bem, conseguindo vantagem em várias disputas curtas.
4: Acelera muito rapidamente, frequentemente deixando adversários para trás.
5: Aceleração explosiva, capaz de criar grandes vantagens em curto espaço de tempo.

3 - Velocidade:
Definição: Velocidade máxima ou constante que um jogador pode atingir durante o jogo.

0: Muito lento, incapaz de manter-se competitivo em corridas.
1: Lento, frequentemente superado por adversários mais rápidos.
2: Velocidade moderada, suficiente para manter-se no jogo, mas sem se destacar.
3: Rápido, conseguindo acompanhar e superar adversários em várias situações.
4: Muito rápido, frequentemente utilizado para explorar jogadas de velocidade.
5: Extremamente rápido, um dos jogadores mais velozes em campo, essencial para contra-ataques e coberturas.

4 - Controle de bola:
Definição: Habilidade de manter a posse da bola sob controle ao recebê-la ou manuseá-la.

0: Muito fraco, frequentemente perde o controle em situações simples.
1: Controle precário, dificuldade em manter a posse sob pressão.
2: Controle razoável, consegue manter a posse, mas com dificuldades em situações complexas.
3: Bom controle, consegue manejar a bola bem em diversas situações.
4: Excelente controle, raramente perde a posse, mesmo sob pressão intensa.
5: Controle excepcional, maneja a bola com maestria, mesmo nas situações mais difíceis.

5 - Drible:
Definição: Capacidade de manobrar a bola ao redor dos adversários enquanto avança no campo.

0: Incapaz de driblar, perde a posse ao tentar fintas.
1: Drible muito limitado, dificuldade em superar adversários.
2: Drible básico, consegue fintar adversários menos habilidosos.
3: Bom drible, frequentemente supera adversários e cria oportunidades.
4: Excelente drible, supera adversários com facilidade e criatividade.
5: Drible fenomenal, capaz de criar jogadas sozinho e desconcertar defesas inteiras.

6 - Fôlego:
Definição: Capacidade de manter um nível elevado de esforço físico durante todo o jogo.

0: Muito baixo, cansa rapidamente e tem queda significativa de desempenho.
1: Baixo, visivelmente cansado no segundo tempo.
2: Moderado, consegue manter-se durante o jogo, mas com queda no final.
3: Bom fôlego, mantém desempenho consistente durante a maior parte do jogo.
4: Excelente fôlego, raramente cansa, mantém intensidade alta durante o jogo todo.
5: Fôlego excepcional, incansável, mantém alto desempenho e intensidade durante os 90 minutos e mais.

7 - Força:
Definição: Capacidade física de vencer duelos corpo a corpo e manter a posse da bola sob pressão.

0: Muito fraco, facilmente superado em duelos físicos.
1: Fraco, geralmente perde confrontos físicos.
2: Força moderada, consegue resistir em alguns duelos, mas com dificuldade.
3: Boa força, vence a maioria dos confrontos físicos.
4: Muito forte, raramente superado em duelos corpo a corpo.
5: Força extraordinária, domina adversários fisicamente, fundamental em duelos aéreos e de corpo.

8 - Impulso:
Definição: Habilidade de saltar alto e de forma explosiva para disputar bolas aéreas.

0: Incapaz de saltar alto, perde quase todas as disputas aéreas.
1: Salto limitado, raramente ganha disputas aéreas.
2: Salta razoavelmente, suficiente para competir em bolas altas.
3: Bom salto, frequentemente vence disputas aéreas.
4: Salto muito bom, ganha a maioria das disputas aéreas.
5: Salto excepcional, praticamente imbatível no jogo aéreo.

9 - Finalização:
Definição: Precisão e habilidade ao concluir jogadas com chutes ao gol.

0: Muito fraco, raramente acerta o gol, pouca precisão.
1: Fraco, pouca precisão e potência nas finalizações.
2: Moderado, consegue algumas finalizações precisas, mas inconsistente.
3: Bom finalizador, frequentemente acerta o gol e marca.
4: Excelente finalizador, muito preciso e confiável nas conclusões.
5: Finalizador excepcional, alta taxa de conversão, marca muitos gols.

10 - Visão de jogo
Definição: Capacidade de perceber e antecipar movimentos dos colegas e adversários para tomar decisões táticas eficazes.

0: Muito limitada, dificuldade em perceber e antecipar movimentos.
1: Limitada, frequentemente perde oportunidades por não ver opções.
2: Moderada, percebe e antecipa algumas jogadas, mas com limitações.
3: Boa visão, percebe bem o jogo e antecipa ações.
4: Excelente visão, frequentemente antecipa movimentos e cria jogadas.
5: Visão excepcional, lê o jogo perfeitamente, cria inúmeras oportunidades.

11 - Passe
Definição: Precisão e técnica ao enviar a bola para um companheiro de equipe.

0: Muito impreciso, frequentemente erra passes simples.
1: Impreciso, dificuldade em acertar passes sob pressão.
2: Passe moderado, consegue distribuir a bola, mas sem grande precisão.
3: Bom passe, distribui a bola com precisão e consistência.
4: Passe excelente, raramente erra, cria muitas oportunidades.
5: Passe excepcional, alta precisão, fundamental na criação de jogadas.

12 - Cruzamento
Definição: Habilidade de enviar a bola com precisão da lateral do campo para a área adversária.

0: Muito impreciso, raramente encontra um companheiro na área.
1: Impreciso, dificuldade em acertar cruzamentos.
2: Moderado, consegue alguns cruzamentos precisos, mas é inconsistente.
3: Bom cruzamento, frequentemente encontra companheiros na área.
4: Excelente cruzamento, muito preciso e cria muitas oportunidades de gol.
5: Cruzamento excepcional, praticamente sempre encontra um companheiro, criando inúmeras chances.

13 - Posicionamento tático
Definição: Capacidade de estar no lugar certo em campo conforme a estratégia da equipe.

0: Muito fraco, frequentemente fora de posição, comprometendo a equipe.
1: Fraco, dificuldade em manter a posição e seguir a estratégia.
2: Moderado, compreende o posicionamento, mas comete erros.
3: Bom posicionamento, geralmente está no lugar certo, seguindo a tática.
4: Excelente posicionamento, sempre bem posicionado e seguindo a estratégia da equipe.
5: Posicionamento excepcional, liderança tática, fundamental na organização da equipe.

14 - Resistência
Definição: Capacidade de resistir ao cansaço e manter a eficácia durante toda a partida

0: Muito baixa, cansa rapidamente e não consegue manter o ritmo.
1: Baixa, visivelmente cansado ao longo do jogo, perde eficiência.
2: Moderada, mantém o ritmo por boa parte do jogo, mas cansa no final.
3: Boa resistência, mantém o ritmo durante a maior parte do jogo.
4: Excelente resistência, raramente cansa, mantém alto desempenho.
5: Resistência excepcional, incansável, mantém alto nível de performance do início ao fim.

"""
Explanação

MEIAS
1. Meia Central: O Maestro do Meio-campo

Visão de Águia: O maestro precisa ter uma visão de jogo ampla e profunda para ler as jogadas e tomar decisões rápidas.
Passe Maestro: Domínio da bola nos pés para distribuir passes precisos e longos, curtos e em diagonal, abrindo espaços para os companheiros.
Cérebro do Time: Inteligência tática para ditar o ritmo do jogo, cadenciar as jogadas e escolher o momento certo para atacar ou defender.
Físico Robusto: Resistência para acompanhar o jogo durante os 90 minutos, com ou sem bola.
Exemplos: Andrea Pirlo, Xavi, Toni Kroos, Joshua Kimmich.

2. Meia Esquerda: Maestro com Ataque na Alma

Combatividade: Combina as habilidades do meia central com a agilidade para atacar pelo lado esquerdo do campo.
Dribles e Finalizações: Habilidade para driblar e finalizar com precisão, criando chances de gol pelo lado esquerdo.
Cruzamentos Perfeitos: Precisa ter qualidade nos cruzamentos para abastecer os atacantes na área.
Conexão com o Ataque: Trabalha em conjunto com o atacante de lado e com o meia central para criar jogadas perigosas.
Exemplos: Arjen Robben, Franck Ribéry, David Silva, Leroy Sané.

3. Meia Direita: Maestro com Ataque na Veia

Espelho do Meia Esquerda: As mesmas habilidades do meia esquerda, mas atuando pelo lado direito do campo.
Conexão com o Outro Lado: Colaboração com o meia central e com o meia esquerda para criar jogadas pelas duas pontas do campo.
Adaptabilidade: Versatilidade para jogar em outras posições do meio-campo, se necessário.
Exemplos: Luis Figo, Kevin De Bruyne, David Beckham, Mohamed Salah.

4. Meia-atacante: O Maestro Finalizador

Fúria Ofensiva: Foco em atacar e finalizar, buscando sempre criar jogadas e marcar gols.
Chutes Potentes e Colocados: Habilidade para finalizar de longa e curta distância, com precisão e força.
Passe Decisivo: Visão de jogo para encontrar passes precisos para os companheiros bem posicionados na área.
Inteligência para se Mover: Movimentação inteligente para buscar espaços na defesa adversária e criar chances de gol.
Exemplos: Zico, Ronaldinho Gaúcho, Mesut Özil, Paulo Dybala.
'''

'''
PONTAS
Pontas Direita: Maestros da Velocidade e Precisão

Pé Direito Dominante: Na maioria dos casos, são canhotos, utilizando o pé direito para dribles, cruzamentos e finalizações precisas.
Corte para o Meio: Costumam cortar para o centro do campo com o pé dominante, buscando finalizações com o pé direito ou passes precisos para os companheiros.
Diagonal Letal: Cruzamentos diagonais com o pé direito são sua arma secreta, buscando a cabeça dos atacantes na área.
Exemplos: Arjen Robben, Mohamed Salah, Gareth Bale, Paulo Dybala.
Pontas Esquerda: Magos da Inversão e Criatividade

Pé Esquerdo Dominante: Destros habilidosos, utilizando o pé esquerdo para dribles, cruzamentos e finalizações precisas.
Corte para a Linha de Fundo: Costumam cortar para a linha de fundo com o pé dominante, buscando cruzamentos rasos para a área ou dribles para ultrapassar a marcação.
Cruzamentos Perfeitos: Cruzamentos rasteiros com o pé esquerdo são sua especialidade, criando chances perigosas para os atacantes.
Exemplos: Franck Ribéry, David Silva, Leroy Sané, Son Heung-min.

'''

"""
Centroavantes
1. Centroavante Pivô: O Gigante Guerreiro

Altura e Força Física: Um gigante imponente que domina o jogo aéreo e as disputas de bola com os zagueiros.
Finalização Potente: Chutes fortes e precisos, tanto com o pé direito quanto com o esquerdo, para finalizar jogadas cruzadas ou rebotes dentro da área.
Jogo de Corpo: Habilidade para proteger a bola e criar espaços para si mesmo e para os companheiros finalizarem.
Bom Cabeceador: Cabeceia com precisão e força, sendo uma grande ameaça em cruzamentos e bolas paradas.
Exemplos: Olivier Giroud, Edinson Cavani, Jan Vennegoor of Hesselink, Hulk.

2. Centroavante Homem de Área: O Caçador Implacável

Instinto Assassino: Faro natural para o gol, sempre buscando a melhor posição para finalizar as jogadas.
Finalização Oportunista: Aproveita qualquer rebote, erro ou desvio para finalizar com precisão e marcar gols.
Inteligência para se Mover: Movimenta-se com inteligência dentro da área, buscando espaços para receber passes e chutes a gol.
Trabalho em Equipe: Colabora com os companheiros, criando jogadas e abrindo espaços para finalizações.
Exemplos: Romário, Ronaldo Fenômeno, Luis Suárez, Robert Lewandowski.
3. Centroavante Falso 9: O Maestro Camuflado

Visão de Jogo e Passe: Visão de jogo apurada para passes precisos e inteligentes, tanto curtos quanto longos.
Mobilidade: Mobilidade para se movimentar por todo o campo, buscando espaços e criando jogadas.
Finalização Técnica: Habilidade para finalizar com precisão, tanto de dentro da área quanto de fora.
Conexão com o Meio-campo: Trabalha em conjunto com os meias para criar jogadas e abrir espaços para os companheiros.
Exemplos: Lionel Messi, Johan Cruyff, Roberto Firmino, Thomas Müller.

"""

from tkinter import *
from tkinter import messagebox

class Jogador:
    def __init__(self, nome, altura, pe_dominante, tempo_reacao, aceleracao, velocidade, controle_bola, drible, folego, resistencia, forca, impulso, finalizacao,visao,passe,cruzamento,pos_tatico):
        self.nome = nome
        self.atributos = {
            "altura": altura, 
            "pe_dominante": pe_dominante, 
            "tempo_reacao": tempo_reacao, 
            "aceleracao": aceleracao, 
            "velocidade": velocidade, 
            "controle_bola": controle_bola, 
            "drible": drible, 
            "folego": folego, 
            "resistencia": resistencia, 
            "forca": forca, 
            "impulso": impulso, 
            "finalizacao": finalizacao, 
            "visao": visao,
            "passe": passe,
            "cruzamento": cruzamento,
            "posicionamento_tatico": pos_tatico,   
            
        }

    def pode_atuar(self):
        altura = self.atributos["altura"] 
        forca = self.atributos["forca"] 
        impulso = self.atributos["impulso"] 
        velocidade = self.atributos["velocidade"] 
        folego = self.atributos["folego"] 
        controle_bola = self.atributos["controle_bola"] 
        resistencia = self.atributos["resistencia"] 
        aceleracao = self.atributos["aceleracao"] 
        tempo_reacao = self.atributos["tempo_reacao"] 
        pe_dominante = self.atributos["pe_dominante"] 
        drible = self.atributos["drible"] 
        finalizacao = self.atributos["finalizacao"] 
        visao = self.atributos["visao"]
        passe = self.atributos["passe"]
        cruzamento = self.atributos["cruzamento"]
        posicionamento_tatico = self.atributos["posicionamento_tatico"]
        posicoes = []
        

        #LÓGICA DOS IFS 
        
        ### Goleiro
        if altura >= 1.80 and tempo_reacao >=3 and forca >= 2 and impulso >= 4: 
            posicoes.append("Goleiro")

        if altura >= 1.80 and tempo_reacao >=3 and finalizacao <=2 and impulso >= 4:
            posicoes.append("Goleiro")

        if altura >= 1.80 and tempo_reacao >=3 and visao >= 3 and impulso >= 4:
            posicoes.append("Goleiro")

        
        ###Zagueiro
        if altura >= 1.85 and forca >= 3 and impulso >=3 and resistencia >=3:
            if pe_dominante == "D":
             posicoes.append("Zagueiro Direito")
            else:
             posicoes.append("Zagueiro Esquerdo")

        if altura >= 1.85 and forca >= 3 and folego >=3 and resistencia >=3:
            if pe_dominante == "D":
             posicoes.append("Zagueiro Direito")
            else:
             posicoes.append("Zagueiro Esquerdo")

        if altura >= 1.85 and forca >= 3 and impulso >=3 and posicionamento_tatico >=2 and folego>=3:
            if pe_dominante == "D":
             posicoes.append("Zagueiro Direito")
            else:
             posicoes.append("Zagueiro Esquerdo")

        if altura >= 1.85 and forca >= 3 and impulso >=3 and posicionamento_tatico >=2 and folego>=3 and passe >=3:
            if pe_dominante == "D":
             posicoes.append("Zagueiro Direito")
            else:
             posicoes.append("Zagueiro Esquerdo")
             
        ### Lateral    
        if altura >= 1.70 and velocidade >= 4 and folego >= 4 and resistencia >=4 and cruzamento >3:
            if pe_dominante == "D":
             posicoes.append("Lateral Direito")
            else:
             posicoes.append("Lateral Esquerdo")
        
        if altura >= 1.70 and velocidade >= 3 and folego >= 4 and resistencia >=4 and cruzamento >2 and passe >=3:
            if pe_dominante == "D":
             posicoes.append("Lateral Direito")
            else:
             posicoes.append("Lateral Esquerdo")
         
         ### Meio de campo    
        if altura >= 1.75 and controle_bola >= 4 and resistencia >= 3 and visao >=4 and finalizacao >=3 and passe >3:
            posicoes.append("Meio Campo Central")
        
        if altura <=1.75 and controle_bola <4 and resistencia >3 and folego >=4:
            posicoes.append("Volante")
        
        if altura and controle_bola >= 4 and resistencia >= 4 and visao >=3 and finalizacao <3:
            if pe_dominante =="D":
              posicoes.append("Meio Campo Direito")
            else:
              posicoes.append("Meio Campo Esquerdo")
        
        
        #Atacantes      
        if altura >= 1.75 and aceleracao >= 3 and velocidade >= 3 and finalizacao >4 and posicionamento_tatico >3:
            posicoes.append("Atacante Centro Avante")

        if altura >= 1.70 and aceleracao < 4 and velocidade <4 and finalizacao >3 and controle_bola >3 and visao > 3:
            posicoes.append("Segundo atacante")  

        if altura >= 1.70 and aceleracao >= 4 and velocidade >=4 and finalizacao <4 and cruzamento >2 and controle_bola >3:
            if pe_dominante == "D":
             posicoes.append("Ponta Direita")
            else:
             posicoes.append("Ponta Esquerda") 

        if altura >= 1.70 and aceleracao >= 4 and velocidade >=4 and finalizacao <4 and drible >=3 and controle_bola >3:
            if pe_dominante == "D":
             posicoes.append("Ponta Direita")
            else:
             posicoes.append("Ponta Esquerda") 

        if altura >= 1.70 and aceleracao >= 4 and velocidade >=4 and finalizacao <4 and drible >=3:
            if pe_dominante == "D":
             posicoes.append("Ponta Direita")
            else:
             posicoes.append("Ponta Esquerda")  

        if posicoes:
            messagebox.showinfo("Posições", f"{self.nome} pode atuar como: " + ", ".join(posicoes))
        else:
            messagebox.showinfo("Posições", f"{self.nome} não tem uma posição ideal encontrada")

def obter_input_jogador():
    nome = tk_nome.get()
    altura = float(tk_altura.get())
    pe_dominante = tk_pe_dominante.get()
    tempo_reacao = tk_tempo_reacao.get()
    aceleracao = tk_aceleracao.get()
    velocidade = tk_velocidade.get()
    controle_bola = tk_controle_bola.get()
    drible = tk_drible.get()
    folego = tk_folego.get()
    resistencia = tk_resistencia.get()
    forca = tk_forca.get()
    impulso = tk_impulso.get()
    finalizacao = tk_finalizcao.get()
    visao = tk_visao.get()
    passe = tk_passe.get()
    cruzamento = tk_cruzamento.get()
    pos_tatico = tk_pos_tatico.get()
        
    
    return Jogador(nome, altura, pe_dominante, tempo_reacao, aceleracao, velocidade, controle_bola, drible, folego, resistencia, forca, impulso, finalizacao,visao,passe,cruzamento,pos_tatico)


def validar_atributos():
    try:
        float(tk_altura.get())
    except ValueError:
        messagebox.showerror("Erro", "A altura deve ser um número válido.")
        return False
    pe_dominante = tk_pe_dominante.get().upper()

    if pe_dominante not in ["D", "E"]:
        messagebox.showerror("Erro", "O pé dominante deve ser 'D' para Direito ou 'E' para Esquerdo.")
        return False

    return True

def submit():
    if validar_atributos():
        jogador = obter_input_jogador()
        jogador.pode_atuar()

# Função para mostrar a tela de boas-vindas
def mostrar_tela_boas_vindas():
    tela_boas_vindas = Tk()
    tela_boas_vindas.title("Bem-Vindo ao Sistema")
    boas_vindas_label = Label(tela_boas_vindas, text="Bem-Vindo! Por favor, clique em 'Continuar' para acessar o sistema.")
    boas_vindas_label.pack(padx=20, pady=20)
    continuar_button = Button(tela_boas_vindas, text="Continuar", command=lambda: [tela_boas_vindas.destroy()])#, criar_janela_principal()])
    continuar_button.pack(padx=20, pady=20)

    # Obtendo a largura e a altura da tela
    largura_tela = tela_boas_vindas.winfo_screenwidth()
    altura_tela = tela_boas_vindas.winfo_screenheight()

    # Definindo a largura e a altura da janela
    largura_janela = 400
    altura_janela = 150

    # Calculando a posição para centralizar a janela
    x = (largura_tela - largura_janela) // 2
    y = (altura_tela - altura_janela) // 2

    # Definindo a geometria da janela para centralizá-la
    tela_boas_vindas.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

    tela_boas_vindas.mainloop()

# Iniciar a aplicação mostrando a tela de boas-vindas
mostrar_tela_boas_vindas()

# Criando a janela principal
root = Tk()
root.title("Cadastro de Jogador")
root.configure(bg="#f0f0f0") # Definindo a cor de fundo

# Criando os widgets
label_nome = Label(root, text="Nome:")
label_altura = Label(root, text="Altura (m):")
label_pe_dominante = Label(root, text="Pé Dominante (D/E):")

tk_nome = Entry(root)
tk_altura = Entry(root)
tk_pe_dominante = Entry(root)

tk_tempo_reacao = IntVar()
tk_aceleracao = IntVar()
tk_velocidade = IntVar()
tk_controle_bola = IntVar()
tk_drible = IntVar()
tk_folego = IntVar()
tk_resistencia = IntVar()
tk_forca = IntVar()
tk_impulso = IntVar()
tk_finalizcao = IntVar()
tk_visao = IntVar()
tk_passe = IntVar()
tk_cruzamento = IntVar()
tk_pos_tatico = IntVar()
tk_finalizcao = IntVar()


tempo_reacao_label = Label(root, text="Tempo de Reação:")
tempo_reacao_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_tempo_reacao)

aceleracao_label = Label(root, text="Aceleração:")
aceleracao_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_aceleracao)

velocidade_label = Label(root, text="Velocidade:")
velocidade_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_velocidade)

controle_bola_label = Label(root, text="Controle de Bola:")
controle_bola_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_controle_bola)

drible_label = Label(root, text="Drible:")
drible_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_drible)

folego_label = Label(root, text="Fôlego:")
folego_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_folego)

resistencia_label = Label(root, text="Resistência:")
resistencia_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_resistencia)

forca_label = Label(root, text="Força:")
forca_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_forca)

impulso_label = Label(root, text="Impulso:")
impulso_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_impulso)

finalizacao_label = Label(root, text="Finalização:")
finalizacao_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_finalizcao)

visao_label = Label(root, text="Visão:")
visao_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_visao)

passe_label = Label(root, text="Passe:")
passe_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_passe)

cruzamento_label = Label(root, text="Cruzamento:")
cruzamento_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_cruzamento)

postatico_label = Label(root, text="Posicionamento tático:")
postatico_scale = Scale(root, from_=0, to=5, orient=HORIZONTAL, variable=tk_pos_tatico)


submit_button = Button(root, text="Enviar", command=submit)

label_nome.grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk_nome.grid(row=0, column=1, padx=10, pady=5)

label_altura.grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk_altura.grid(row=1, column=1, padx=10, pady=5)

label_pe_dominante.grid(row=2, column=0, sticky="w", padx=10, pady=5)
tk_pe_dominante.grid(row=2, column=1, padx=10, pady=5)

tempo_reacao_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
tempo_reacao_scale.grid(row=3, column=1, padx=10, pady=5)

aceleracao_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)
aceleracao_scale.grid(row=4, column=1, padx=10, pady=5)

velocidade_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)
velocidade_scale.grid(row=5, column=1, padx=10, pady=5)

controle_bola_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)
controle_bola_scale.grid(row=6, column=1, padx=10, pady=5)

drible_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)
drible_scale.grid(row=7, column=1, padx=10, pady=5)

folego_label.grid(row=8, column=0, sticky="w", padx=10, pady=5)
folego_scale.grid(row=8, column=1, padx=10, pady=5)

resistencia_label.grid(row=9, column=0, sticky="w", padx=10, pady=5)
resistencia_scale.grid(row=9, column=1, padx=10, pady=5)

forca_label.grid(row=10, column=0, sticky="w", padx=10, pady=5)
forca_scale.grid(row=10, column=1, padx=10, pady=5)

impulso_label.grid(row=11, column=0, sticky="w", padx=10, pady=5)
impulso_scale.grid(row=11, column=1, padx=10, pady=5)

finalizacao_label.grid(row=13, column=0, sticky="w", padx=10, pady=5)
finalizacao_scale.grid(row=13, column=1, padx=10, pady=5)

visao_label.grid(row=14, column=0, sticky="w", padx=10, pady=5)
visao_scale.grid(row=14, column=1, padx=10, pady=5)

passe_label.grid(row=15, column=0, sticky="w", padx=10, pady=5)
passe_scale.grid(row=15, column=1, padx=10, pady=5)

cruzamento_label.grid(row=16, column=0, sticky="w", padx=10, pady=5)
cruzamento_scale.grid(row=16, column=1, padx=10, pady=5)

postatico_label.grid(row=17, column=0, sticky="w", padx=10, pady=5)
postatico_scale.grid(row=17, column=1, padx=10, pady=5)


submit_button.grid(row=18, columnspan=2, pady=10)

largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

largura_janela = 400
altura_janela = 900

x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2

root.geometry(f'{largura_janela}x{altura_janela}+{x}+{y}')

root.mainloop()


