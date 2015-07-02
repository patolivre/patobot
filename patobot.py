import serial
from flask import Flask

app =  Flask(__name__)

direcoes_andar = {
    'frente': 1,
    'tras': 2,
}

direcoes_girar = {
    'direita': 3,
    'esquerda': 4,
}

@app.route('/andar/<direcao>')
def andar(direcao):
    com.write(str(direcoes_andar[direcao]))
    return 'andou para %s' % direcao

@app.route('/girar/<direcao>')
def girar(direcao):
    com.write(str(direcoes_girar[direcao]))
    return 'girou para a %s' % direcao

@app.route('/')
def main():
    return 'PatoBot :-)'


if __name__ == '__main__':

    device = '/dev/ttyACM0'
    baud_rate = 115200

    try:
        com = serial.Serial(device, baud_rate)
    except:
        exit() 

    app.run(host='0.0.0.0', debug=True)
