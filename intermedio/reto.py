def run():
    numero = [i for i in range (1, 100000) if i % 36 == 0]
    print(f'{numero}')


if __name__ == '__main__':
    run()