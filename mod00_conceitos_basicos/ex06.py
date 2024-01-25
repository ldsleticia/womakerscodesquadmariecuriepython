# Exercicio 6

def calcular_tempo_viagem():
    distancia = float(input("Digite a distância da viagem em km: "))

    velocidade_aviao = 600
    velocidade_carro = 100
    velocidade_onibus = 80

    # Função para converter horas em horas e minutos
    def converter_para_horas_e_minutos(tempo_em_horas):
        horas = int(tempo_em_horas)
        minutos = int((tempo_em_horas - horas) * 60)
        return (horas, minutos)

    # Converte para horas e minutos
    horas_aviao, minutos_aviao = converter_para_horas_e_minutos(distancia / velocidade_aviao)
    horas_carro, minutos_carro = converter_para_horas_e_minutos(distancia / velocidade_carro)
    horas_onibus, minutos_onibus = converter_para_horas_e_minutos(distancia / velocidade_onibus)

    # Imprime o tempo de viagem para cada meio de transporte em horas e minutos
    print(f"Tempo de viagem de avião: {horas_aviao} horas e {minutos_aviao} minutos")
    print(f"Tempo de viagem de carro: {horas_carro} horas e {minutos_carro} minutos")
    print(f"Tempo de viagem de ônibus: {horas_onibus} horas e {minutos_onibus} minutos")

calcular_tempo_viagem()

'''
