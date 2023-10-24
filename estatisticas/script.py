import csv

# Função que recebe a matrícula do aluno e retorna a média de todas as suas cadeiras
def mediaAluno(matricula):
    notas = [] # Lista contendo as notas

    with open("dados.csv", encoding="utf8") as file:
        next(file) # Pula uma linha para não dar erro nas conversões de tipo, a primeira linha tem os nomes das colunas
        csvreader = csv.reader(file)

        for row in csvreader: # Percorre todas as linhas do arquivo CSV
            # Verifica se a linha tem dados, se tiver verifica se a primeira coluna tem a matrícula recebida;
            # se a quinta coluna que é a de número de créditos é menor que 10, pois a única cadeira com mais 
            # de 10 créditos é a de atividades complementares, onde a nota não importa; e se a nona coluna 
            # que é a de status da cadeira não diz que a cadeira ainda está em andamento (ongoing)
            if row != []:
                if int(row[0]) == matricula and int(row[3]) < 10 and row[8] != 'ONGOING':
                    notas.append(float(row[7]))
                
    # Caso não tenha nenhuma nota do aluno, imprime uma mensagem e retorna 0;
    # caso tenha, soma as notas e retorna a média formatada com duas casas decimais
    if len(notas) == 0:
        print("Aluno não foi encontrado.")
        return 0

    soma = 0.0
    for n in notas: soma += n
    return "{:.2f}".format(soma/len(notas))

# Função que recebe a matrícula do aluno e retorna a média das suas notas em cada período
def mediaAlunoPeriodo(matricula):
    notas = {} # Dicionário das notas, as keys são os períodos, os values são listas contendo as notas do período

    with open("dados.csv", encoding="utf8") as file:
        next(file) # Pula uma linha para não dar erro nas conversões de tipo, a primeira linha tem os nomes das colunas
        csvreader = csv.reader(file)

        for row in csvreader: # Percorre todas as linhas do arquivo CSV
            # Verifica se a linha tem dados, se tiver verifica se a primeira coluna tem a matrícula recebida;
            # se a quinta coluna que é a de número de créditos é menor que 10, pois a única cadeira com mais 
            # de 10 créditos é a de atividades complementares, onde a nota não importa; e se a nona coluna 
            # que é a de status da cadeira não diz que a cadeira ainda está em andamento (ongoing)
            if row != []:
                if int(row[0]) == matricula and int(row[3]) < 10 and row[8] != 'ONGOING':
                    # Se não tiver uma key com o período, cria uma lista com o valor da nota,
                    # se já tiver, adiciona a nota na lista de notas dentro do dicionário
                    if notas.get(float(row[5])): notas[float(row[5])].append(float(row[7]))
                    else: notas[float(row[5])] = [float(row[7])]
                
    # Caso não tenha nenhuma nota do aluno, imprime uma mensagem e retorna 0;
    if len(notas) == 0:
        print("Aluno não foi encontrado.")
        return 0

    # Itera pelo dicionário de notas, somando as notas por período e colocando a média formatada na lista de notasPorPeriodo
    notasPorPeriodo = []
    for periodo in notas:
        soma = 0.0
        for n in notas.get(periodo): soma += n
        notasPorPeriodo.append("{:.2f}".format(soma/len(notas.get(periodo))))
    return notasPorPeriodo

# Função que recebe a matrícula do aluno e diz a média das suas em cada período
def comparaMediaAlunoPeriodo(matricula):
    notas = {} # Dicionário das notas, as keys são os períodos, os values são listas contendo as notas do período

    with open("dados.csv", encoding="utf8") as file:
        next(file) # Pula uma linha para não dar erro nas conversões de tipo, a primeira linha tem os nomes das colunas
        csvreader = csv.reader(file)

        for row in csvreader: # Percorre todas as linhas do arquivo CSV
            # Verifica se a linha tem dados, se tiver verifica se a primeira coluna tem a matrícula recebida;
            # se a quinta coluna que é a de número de créditos é menor que 10, pois a única cadeira com mais 
            # de 10 créditos é a de atividades complementares, onde a nota não importa; e se a nona coluna 
            # que é a de status da cadeira não diz que a cadeira ainda está em andamento (ongoing)
            if row != []:
                if int(row[0]) == matricula and int(row[3]) < 10 and row[8] != 'ONGOING':
                    # Se não tiver uma key com o período, cria uma lista com o valor da nota,
                    # se já tiver, adiciona a nota na lista de notas dentro do dicionário
                    if notas.get(float(row[5])): notas[float(row[5])].append(float(row[7]))
                    else: notas[float(row[5])] = [float(row[7])]
                
    # Caso não tenha nenhuma nota do aluno, imprime uma mensagem e retorna 0;
    if len(notas) == 0:
        print("Aluno não foi encontrado.")
        return 0

    # Itera pelo dicionário de notas, somando as notas por período e colocando
    # a média no dicionário de notasPorPeriodo com o número de cadeiras como key
    notasPorPeriodo = {}
    for periodo in notas:
        soma = 0.0
        for n in notas.get(periodo): soma += n

        media = soma/len(notas.get(periodo))
        if notasPorPeriodo.get(len(notas.get(periodo))): notasPorPeriodo[len(notas.get(periodo))].append(media)
        else: notasPorPeriodo[len(notas.get(periodo))] = [media]
    
    # Itera pelo dicionário de notasPorPeriodo, somando as notas por número de cadeiras
    # e colocando a média formatada delas no dicionário de mediasPorNumeroCadeiras
    mediasPorNumeroCadeiras = {}
    for cadeiras in notasPorPeriodo:
        soma = 0.0
        for n in notasPorPeriodo.get(cadeiras): soma += n
        mediasPorNumeroCadeiras[cadeiras] = "{:.2f}".format(soma/len(notasPorPeriodo.get(cadeiras)))

    return mediasPorNumeroCadeiras

# Função que recebe a matrícula do aluno e retorna o número de reprovações em cada período
def reprovacoesAlunoPeriodo(matricula):
    reprovacoes = {} # Dicionário que tem como key o período e como value o número de reprovações

    with open("dados.csv", encoding="utf8") as file:
        next(file) # Pula uma linha para não dar erro nas conversões de tipo, a primeira linha tem os nomes das colunas
        csvreader = csv.reader(file)

        for row in csvreader: # Percorre todas as linhas do arquivo CSV
            # Verifica se a linha tem dados, se tiver verifica se a primeira coluna tem a matrícula recebida e
            # coloca 0 no dicionário de reprovações nos períodos em que o aluno esteve matriculado
            if row != []:
                if int(row[0]) == matricula:
                    reprovacoes[row[5]] = 0
        
    with open("dados.csv", encoding="utf8") as file:
        next(file) # Pula uma linha para não dar erro nas conversões de tipo, a primeira linha tem os nomes das colunas
        csvreader = csv.reader(file)

        for row in csvreader: # Percorre todas as linhas do arquivo CSV
            # Verifica se a linha tem dados, se tiver verifica se a primeira coluna tem a matrícula recebida e
            # se a nona coluna que é a de status da cadeira diz que o aluno reprovou por nota ou falta
            if row != []:
                if int(row[0]) == matricula and (row[8] == "FAILED_DUE_TO_GRADE" or row[8] == "FAILED_DUE_TO_ABSENCE"):
                    reprovacoes[row[5]] += 1

    return reprovacoes

def main():
    print(reprovacoesAlunoPeriodo(112213381))

if __name__ == "__main__":
    main()
