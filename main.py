
def my_name_is():
    # return ['0symbol', '1symbol', '2symbol', '3symbol', '4symbol', '5symbol', '6symbol', '7symbol', '8symbol', '9symbol', '10symbol', '11symbol', '12symbol', '13symbol', '14symbol', '15symbol', '16symbol', '17symbol', '18symbol', '19symbol', '20symbol', '21symbol', '22symbol', '23symbol', '24symbol', '25symbol', '26symbol', '27symbol', '28symbol', '29symbol', '30symbol', '31symbol', '32symbol', '33symbol', '34symbol', '35symbol', '36symbol', '37symbol', '38symbol', '39symbol', '40symbol', '41symbol', '42symbol', '43symbol', '44symbol', '45symbol', '46symbol', '47symbol', '48symbol', '49symbol', '50symbol', '51symbol', '52symbol', '53symbol', '54symbol', '55symbol', '56symbol', '57symbol', '58symbol', '59symbol', '60symbol', '61symbol', '62symbol', '63symbol', '64symbol', '65symbol', '66symbol', '67symbol', '68symbol', '69symbol', '70symbol', '71symbol', '72symbol', '73symbol', '74symbol', '75symbol', '76symbol', '77symbol', '78symbol', '79symbol', '80symbol', '81symbol', '82symbol', '83symbol', '84symbol', '85symbol', '86symbol', '87symbol', '88symbol', '89symbol', '90symbol', '91symbol', '92symbol', '93symbol', '94symbol', '95symbol', '96symbol', '97symbol', '98symbol', '99symbol', ]
    return ["A", "E", "N", "Circle Cross", "Circle X", "K", "Circle X", "M", "Circle X", "Dick", "N", "A", "M"]


def ceasar_decrypt(message):
    # https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
    return translated


if __name__ == '__main__':
    pass


