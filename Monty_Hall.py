import random, sys


Closed_doors = '''
+------+ +------+ +------+
|      | |      | |      |
| 1    | | 2    | | 3    |
|      | |      | |      |
|      | |      | |      |
|      | |      | |      |
+------+ +------+ +------+'''


First_goat = '''
+------+ +------+ +------+
|   (( | |      | |      |
|  oo  | |   2  | |    3 |
| /_/|_| |      | |      |
|    | | |      | |      |
|CABR|A| |      | |      |
+------+ +------+ +------+'''


Second_goat = '''
+------+ +------+ +------+
|      | | ((   | |      |
| 1    | | oo   | | 3    |
|      | |/_/|_ | |      |
|      | |   |  | |      |
|      | |CABR|A| |      |
+------+ +------+ +------+'''


Third_goat = '''
+------+ +------+ +------+
|      | |      | |  ((  |
| 1    | | 2    | |  oo  |
|      | |      | | /_/|_|
|      | |      | |    | |
|      | |      | |CABR|A| 
+------+ +------+ +------+'''


First_car_goats = '''
+------+ +------+ +------+
| CAR! | | ((   | | ((   |
|    __| | oo   | | oo   |
|  _/  | |/_/|_ | |/_/|_ |
| /_  _| |   |  | |   |  |
|    O | |CABR|A| |CABR|A| 
+------+ +------+ +------+'''


Second_car_goats = '''
+------+ +------+ +------+
|  ((  | | CAR! | |  ((  |
|  oo  | |    __| |  oo  |
| /_/|_| |  _/  | | /_/|_|
|    | | | /_ __| |    | |
|CABR|A| |    O | |CABR|A| 
+------+ +------+ +------+'''


Third_car_goats = '''
+------+ +------+ +------+
|  ((  | |  ((  | | CAR! |
|  oo  | |  oo  | |    __|
| /_/|_| | /_/|_| |  _/  |
|    | | |    | | | /_ __|
|CABR|A| |CABR|A| |    O |
+------+ +------+ +------+'''

print('''

No game show Monty Hall, você pode escolher uma das três portas. Uma porta tem 
um carro novo para um prêmio. As outras duas portas têm cabras inúteis: {}
Digamos que você escolha a Porta #1. Antes que a porta que você escolher se 
abra, outra porta com uma cabra é aberta:{}
Você pode optar por abrir a porta que escolheu originalmente ou alternar para a outra porta.

Pode parecer que nao importa se você muda ou nao, mas suas chances aumentam se 
você mudar a porta! Este programa demonstra o problema de Monty Hall, permitindo que você execute experimentos repetidos.
'''.format(Closed_doors, Third_goat))

input('Pressione ENTER para iniciar....\n')

swap_Wins = 0
stay_Wins = 0
swap_Losses = 0
stay_Losses = 0
while True:
    door_that_Car = random.randint(1, 3)

    print(Closed_doors)
    while True:
        response = input('Escolha uma porta: 1, 2 ou 3? ').upper()
        if response == 'SAIR':
            print('Obrigado por jogar!')
            sys.exit()

        if response == '1' or response == '2' or response == '3':
            break
    door_Pick = int(response)                    

    while True:
        show_goat_door = random.randint(1, 3)
        if show_goat_door != door_Pick and show_goat_door != door_that_Car:
            break

    if show_goat_door == 1:
            print(First_goat)
    elif show_goat_door == 2:
            print(Second_goat)            
    elif show_goat_door == 3:
            print(Third_goat)

    print('\nA porta {} contém uma cabra!'.format(show_goat_door))

    while True:
        print('\nQuer trocar de porta? S/N')
        swap = input(' ').upper()
        if swap == 'S' or swap == 'N':
            break

    if swap == 'S':
        if door_Pick == 1 and show_goat_door == 2:
            door_Pick = 3
        elif door_Pick == 1 and show_goat_door == 3:
            door_Pick = 2                                             
        elif door_Pick == 2 and show_goat_door == 1:
            door_Pick = 3
        elif door_Pick == 2 and show_goat_door == 3:
            door_Pick = 1
        elif door_Pick == 3 and show_goat_door == 1:
            door_Pick = 2
        elif door_Pick == 3 and show_goat_door == 2:
            door_Pick = 1

    if door_that_Car == 1:
        print(First_car_goats)
    elif door_that_Car == 2:
        print(Second_car_goats)
    elif door_that_Car == 3:
        print(Third_car_goats)            


    print('A porta {} está com o carro!'.format(door_that_Car))


    if door_Pick == door_that_Car:
        print('Você ganhou!')
        if swap == 'S':
            swap_Wins += 1
        elif swap == 'N':
            stay_Wins += 1
    else:
        print('>>> Você perdeu!')
        if swap == 'S':
            swap_Losses += 1
        elif swap == 'N':
            stay_Losses += 1    

    total_Swaps = swap_Wins + swap_Losses
    if total_Swaps != 0:
        swap_sucess = round(swap_Wins / total_Swaps * 100, 1)

    else: 
        swap_sucess = 0.0


    total_Stays = stay_Wins + stay_Losses
    if (stay_Wins + stay_Losses) != 0:
            stay_sucess = round(stay_Wins / total_Stays * 100, 1)

    else: 
        stay_sucess = 0.0              


    print()
    print('Com troca(s): ', end='')
    print('{} vitória(s), {} derrota(s), '.format(swap_Wins, swap_Losses), end='')
    print('taxa de sucesso {}%'.format(swap_sucess))
    print('Sem troca(s): ', end='')
    print('{} vitória(s), {} derrota(s), '.format(stay_Wins, stay_Losses), end='')
    print('taxa de sucesso {}%'.format(stay_sucess))                                
    print()
    input('Pressione Enter para repetir o experimento...')                                           