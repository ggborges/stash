import random

# criar reward_matrix
#   linhas são estados
#   colunas são ações

# Atualiza a utilidade referente ao estado 'state' e a ação 'action'

def q_update(state, action, next_state, rw, q_matrix, alpha, gamma):
    # Recompensa atual + utilidade esperada da melhor ação possível para o próximo estado
    
    if(state == next_state): # se o estado é igual ao próximo estado, significa que o agente bateu na parede
        reward = -10
        estimate_q = reward + gamma * max(q_matrix[next_state][0], q_matrix[next_state][1], q_matrix[next_state][2], q_matrix[next_state][3])
        print('==> Estimate Q: ', estimate_q)
    else:
        estimate_q = rw[state] + gamma * max(q_matrix[next_state][0], q_matrix[next_state][1], q_matrix[next_state][2], q_matrix[next_state][3])
        print('==> Estimate Q: ', estimate_q)

    # Ajusta a q_matrix considerando o valor atual da qualidade e o desvio em relação a estimativa estimate_q
    # Equação de Bellman
    value = q_matrix[state][action] + alpha * (estimate_q - q_matrix[state][action])
    q_value = float("{:.2f}".format(value))
    print('==> Q Value: ', q_value)

    return q_value

# MÉTODOS PARA ESCOLHA DE AÇÕES BASEADA EM TRAJETÓRA PRE-DEFINIDA
def get_trajetoria(num_trajetoria):
    
    trajetoria1 = [0, 1, 3, 2, 3, 2, 2, 0, 3] # up - down - right - left - right - left - left - up - right
    trajetoria2 = [0, 0, 2, 2, 2, 3] # up - up - left - left - left - right
    trajetoria3 = [1, 0, 3, 0, 1, 2, 1, 0, 3, 3] # down - up - right - up - down - left - down - up - right - right
    trajetoria4 = [0, 3, 0] # up - right - up
    trajetoria5 = [2, 0, 0, 0, 2, 1, 0, 0, 0, 1, 0, 2, 3, 0] # left - up - up - up - left - down - up - up - up - down - up - left - right - up

    if (num_trajetoria == 1):
        return trajetoria1

    elif (num_trajetoria == 2):
        return trajetoria2

    elif (num_trajetoria == 3):
        return trajetoria3

    elif (num_trajetoria == 4):
        return trajetoria4

    elif (num_trajetoria == 5):
        return trajetoria5

def explore_trajetoria(num_trajetoria, action_names, rw, q_matrix, alpha, gamma):

    state = 0 # estado 1
    terminal = True
    iter = 1

    trajetoria = get_trajetoria(num_trajetoria)

    while(terminal):
        for i in range(len(trajetoria)):   
            # enquanto não alcançarmos o estado terminal
            # Escolhe uma ação da trajetória
            action = trajetoria[i]
            print('---------------\naction: ', action, '\nstate: ', state+1)
            print('Acao escolhida: ', action_names[action])
            next_state = move_trajetoria(state, action)
            print('\n', state + 1, action_names[action], next_state, '\n')

            # Atualizar o valor da utilidade correspondente ao estado 'state' e ação 'action'
            q_matrix[state][action] = q_update(state, action, next_state-1, rw, q_matrix, alpha, gamma)

            state = next_state - 1

            print('Q-Matrix #' + str(iter) + ':')
            for j in range(6):
                print(q_matrix[j])

            # Teste de parada
            if (state == 5):
                terminal = False

            iter += iter
   
def move_trajetoria(state, action):

    state = state + 1 

    # grid com os números dos estados
    grid = [
        [5, 6],
        [3, 4],
        [1, 2]
    ]

    print('-<>-\nMapa:\n', grid[0], '\n', grid[1], '\n', grid[2])

    # iniciando no estado 1
    #agentY = 2 # -1 sobe, +1 desce
    #agentX = 0 # +1 direita, -1 esquerda

    #print('estado inicial no grid:', grid[agentY][agentX])

    agentX = 0
    agentY = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == state:
                agentX = i
                agentY = j
    
    print('\nagentX: ', agentX, ' agentY: ', agentY)

    print('Acao realizada: ', action)

    xLim = len(grid)
    yLim = len(grid[0])

    #print('xLim: ' + str(xLim) + ' yLim: ' + str(yLim))

    newX = agentX
    newY = agentY


    if action == 0:
        # (x-1, y)
        newX -= 1
    elif action == 1:
        # (x+1, y)
        newX += 1
    elif action == 2:
        # (x, y-1)
        newY -= 1
    elif action == 3:
        # (x, y+1)
        newY += 1


    # verificamos se bateu na parede
    bateu = False

    if newX >= xLim:
        bateu = True
        newX -= 1
    if newX < 0:
        bateu = True
        newX = 0

    if newY >= yLim:
        newY -= 1
        bateu = True
    if newY < 0:
        newY = 0
        bateu = True

    if (bateu):
        print('<-> Bateu na parede <->')

    next_state = grid[newX][newY]

    print('newX: ' + str(newX) + ' newY: ' + str(newY))
    print('Novo estado: ', next_state)

    return next_state

# MÉTODOS PARA ESCOLHA DE AÇÃO BASEADA NAS QUALIDADES DA MATRIZ Q
def explore_choose_action(action_names, rw, q_matrix, alpha, gamma):
    state = 0 # estado 1
    terminal = True
    iter = 1

    while(terminal):
        # enquanto não alcançarmos o estado terminal
        # Escolhe uma ação da trajetória
        action = choose_action(state, q_matrix)
        print('---------------\naction: ', action, '\nstate: ', state+1)
        print('Acao escolhida: ', action_names[action])
        next_state = move(state, action)


        # Atualizar o valor da utilidade correspondente ao estado 'state' e ação 'action'
        q_matrix[state][action] = q_update(state, action, next_state-1, rw, q_matrix, alpha, gamma)

        state = next_state - 1

        print('Q-Matrix #' + str(iter) + ':')
        for j in range(6):
            print(q_matrix[j])

        # Teste de parada
        if (state == 5):
            terminal = False

        iter += iter

def choose_action(state, q_matrix):
    
    # Usar trajetórias previamente descritas
    # ou
    # Escolher ações de acordo com a tabela Q 'q_matrix'

    action = 0
    aux = -10

    # Correndo a linha correspondente ao 'state'
    # procurando pela ação de maior valor
    # o index 'i' corresponde ao número relacionado às ações (colunas)
    for i in range(4):
        if (q_matrix[state][i] > aux):
            action = i
            aux = q_matrix[state][i]
    
    
    return action

# Recebe um estado ('state') e uma ação ('action')
# aplica a ação, considerando as taxas de erro
# Retorna o novo estado, a partir do estado 'state'
def move(state, action):

    state = state + 1 

    # grid com os números dos estados
    grid = [
        [5, 6],
        [3, 4],
        [1, 2]
    ]

    print('-<>-\nMapa:\n', grid[0], '\n', grid[1], '\n', grid[2])

    # iniciando no estado 1
    #agentY = 2 # -1 sobe, +1 desce
    #agentX = 0 # +1 direita, -1 esquerda

    #print('estado inicial no grid:', grid[agentY][agentX])

    agentX = 0
    agentY = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == state:
                agentX = i
                agentY = j
    
    print('\nagentX: ', agentX, ' agentY: ', agentY)

    rd = random.randint(1,10)

    trueMove = ''

    if action == 0:
        if rd < 2:
            trueMove = 'l'
        elif rd > 9:
            trueMove = 'r'
        else:
            trueMove = 'u'
    elif action == 1:
        if rd < 2:
            trueMove = 'r'
        elif rd > 9:
            trueMove = 'l'
        else:
            trueMove = 'd'
    elif action == 2:
        if rd < 2:
            trueMove = 'd'
        elif rd > 9:
            trueMove = 'u'
        else:
            trueMove = 'l'
    elif action == 3:
        if rd < 2:
            trueMove = 'u'
        elif rd > 9:
            trueMove = 'd'
        else:
            trueMove = 'r'

    print('Acao realizada: ', trueMove)

    xLim = len(grid)
    yLim = len(grid[0])

    #print('xLim: ' + str(xLim) + ' yLim: ' + str(yLim))

    newX = agentX
    newY = agentY

    if trueMove == 'u':
        # (x-1, y)
        newX -= 1
    elif trueMove == 'd':
        # (x+1, y)
        newX += 1
    elif trueMove == 'l':
        # (x, y-1)
        newY -= 1
    elif trueMove == 'r':
        # (x, y+1)
        newY += 1


    # verificamos se bateu na parede
    bateu = False

    if newX >= xLim:
        bateu = True
        newX -= 1
    if newX < 0:
        bateu = True
        newX = 0

    if newY >= yLim:
        newY -= 1
        bateu = True
    if newY < 0:
        newY = 0
        bateu = True

    if (bateu):
        print('<-> Bateu na parede <->')

    next_state = grid[newX][newY]

    print('newX: ' + str(newX) + ' newY: ' + str(newY))
    print('Novo estado: ', next_state)

    print('\n', state, trueMove, next_state, '\n')

    return next_state


number_states = 6 # 0..5
number_actions = 4 # 0..3

action_names = ['u', 'd', 'l', 'r']

# Exemplo: No modelo q_matrix[2][0] -> Qualidade de andar para cima no estado 3
# Actions -> 0: up | 1: down | 2: left | 3: right

# Initialize Q-Table with zeros

q_matrix = [[float("{:.2f}".format(0)) for x in range(number_actions)] for y in range(number_states)]
#q_matrix[4][3] = 10 # estado 5, ação right
#q_matrix[3][0] = 10 # estado 4, ação up
print('q_matrix: ')
for i in range(6):
    print(q_matrix[i])

# Inserção dos valores dos estados terminais

# Matriz de recompensa

R = -1
rw = [R for i in range(number_states)]
rw[5] = 10

print('Matriz de recompensa:', rw)

alpha = 0.5
gamma = 1

number_f = 0
num_f = input("\nEscolha o numero (1 ~ 2) do metodo de exploracao: \n[1- Escolher acao baseada na tabela Q.]\n[2- Escolher acao baseada na trajetoria.]\n")
try:
    number_f = int(num_f)
except ValueError:
    print('Nao digitou um numero ou numero invalido!')

if (number_f == 1): # Escolheu método de escolha da ação na tabela Q!
    print('.. Escolheu o metodo de escolha da acao na tabela Q ..')
# Iterações para preencher a tabela Q
    for i in range(10):
        explore_choose_action(action_names, rw, q_matrix, alpha, gamma)
        print('Fim do loop #', i)
        print('---------------------------------------------------------')

elif (number_f == 2): # Escolheu o método de escolha da ação da trajetória!
    print('.. Escolheu o metodo de escolha da acao de acordo com a trajetoria ..')
# Usando trajetória para explorar o ambiente
    for i in range(5):
        explore_trajetoria(i+1, action_names, rw, q_matrix, alpha, gamma)
        print('Fim do loop #', i)
        print('---------------------------------------------------------')

print('\n#############\n\nQ-Matrix:\n')

print(q_matrix[0])
print(q_matrix[1])
print(q_matrix[2])
print(q_matrix[3])
print(q_matrix[4])
print(q_matrix[5])

def max_col(matrix, num_states):
    max_cols = [-1 for x in range(num_states)]
    for i in range(len(matrix)):
        max_q = -9999
        for j in range(len(matrix[i])):
            if (matrix[i][j] >= max_q):
                max_q = matrix[i][j]
                max_cols[i] = j
    
    return max_cols

policy = max_col(q_matrix, number_states)

print('\nMelhores actions por estado:\n s1,s2,s3,s4,s5,s6\n', policy)


print('\n~~~~~~~~~~~~\nPolitica de transicao:\n')
print(action_names[policy[4]], '+10')
print(action_names[policy[2]], action_names[policy[3]])
print(action_names[policy[0]], action_names[policy[1]])

# PRINTAR A POLÍTICA E A MATRIZ Q



# function get_action(current_state, reward_matrix)
#   - recebe um estado atual e a matriz de recompensas
#       a fim de decidr a melhor ação

# function take_action(current_state, reward_matrix, gamma)
#       professor chamou a função de choose_action
#   action = get_action(current_state, reward_matrix)
#   sa_reward = reward_matrix[current_state, action] -> state-action reward
#   ns_reward = max(q_matrix[action,]) -> next_state_action reward
#       - valor máximo entre todos os estados que podemos acessar ao usar a ação 'action' no current_state
#   q_current_state = state_action_rw + (gamma * ns_reward)


# function initialize_episode(rw_matrix, initial_state, gamma)
#   current_state = initial_state
#   while True:
#       current_state = take_action(current_state, rw_matrix, gamma)

# function train_agent(iterations, rw_matrix, gamma)
#   for episode in range(iterations):
#       initial_state -= set_initial_state() - function that picks a random state to be the initial_state
#       initializa_episode(rw_matrix, initial_state, gamma)
#
#   return q_matrix