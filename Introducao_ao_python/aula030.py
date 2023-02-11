# Constantes: Variáveis que não vão mudar.

velocidade = 30
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_no_primeiro_terco_radar =  local_carro >= (LOCAL_1 - RADAR_RANGE)
carro_no_ultimo_terco_radar = local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_passou_radar_1 = carro_no_primeiro_terco_radar and carro_no_ultimo_terco_radar
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1


if velocidade_carro_passou_radar_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:    
    print('Carro multado em radar 1')
