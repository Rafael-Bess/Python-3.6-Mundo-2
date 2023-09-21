from time import sleep
print('Os fogos vão começar em: \n'
      '** pausa dramatica **')
for fogos in range(10, -1, -1):
    sleep(1)
    print('{} {} {}'.format(4 * '=', fogos, 4 * '='))
print('🎆🎆🎆🎆🎆🎆🎆')