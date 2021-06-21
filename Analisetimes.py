times = ('América-MG', 'Athletico', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Bragantino', 'Ceará', 'Chapecoense',
         'Corinthians', 'Cuiabá', 'Fortaleza', 'Flamengo', 'Fluminense', 'Grêmio', 'Internacional', 'Juventude',
         'Palmeiras', 'Santos','São Paulo', 'Sport')
print('-=' * 15)
print('BRASILEIRÃO 2021')
print('-=' * 15)
print(f'Participam do campeonato: {sorted(times)}')
print('-=' * 15)
print(f'O TOP 5 possui: {times[0:5]}')
print('-=' * 15)
print(f'O Z4 possui: {times[-4:]}')
print('-=' * 15)
print(f'O Fluminense está na {times.index("Fluminense")+1}ª posição. ')
print('-=' * 15)