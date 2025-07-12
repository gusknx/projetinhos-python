"""esse módulo faz isso e isso e isso"""
import time

def testando_coisas() -> None:
    """Esse código é um teste

    Args:
        None

    Returns:
        None

    """

    for number in range(1, 5):
        if number == 4:
            print('teste, encerrado.')
            time.sleep(2)

        if number != 5:
            print('vez errada')

if __name__  == '__main__':
    testando_coisas()
