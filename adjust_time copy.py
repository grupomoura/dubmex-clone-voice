def calcular_velocidade_pronuncia(segundos):
    velocidade_minima = 0
    velocidade_maxima = 2

    # Calcula a velocidade de pronúncia baseada nos segundos
    velocidade = (segundos / 60) * (velocidade_maxima - velocidade_minima) + velocidade_minima

    return velocidade

velocidade = calcular_velocidade_pronuncia(50)
print(velocidade)