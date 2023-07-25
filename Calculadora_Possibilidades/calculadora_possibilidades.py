import PySimpleGUI as sg


def main():

    # Definição do tema Dark Blue3
    sg.theme('Dark')

    # Definição do layout da interface
    layout = [
        [sg.Text('Valor Principal:', size=(12, 1), pad=((10, 5), (5, 5))), sg.Input(key='-VALOR1-', size=(12, 1)),
         sg.Text('Valor Multiplicado:', size=(13, 1), pad=((10, 5), (5, 5))), sg.Input(key='-VALOR2-', size=(12, 1))],
        [sg.Text('Valor Dividido:', size=(12, 1), pad=((10, 5), (5, 10))), sg.Input(key='-VALOR3-', size=(12, 1)),
         sg.Text('Resultado:', size=(12, 1), pad=((10, 5), (5, 10))), sg.Input(key='-RESULTADO-', size=(12, 1))],
        [sg.Button('Calcular'), sg.Button('Sair')]
    ]

    # Configuração do tamanho da janela
    window = sg.Window('Calculadora de Regra de Três', layout, size=(400, 200))

    # Loop para interação com a interface
    while True:
        event, values = window.read()

        # Se o usuário fechar a janela
        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break

        # Se o usuário clicar no botão 'Calcular'
        if event == 'Calcular':
            try:
                # Obtém os valores inseridos pelo usuário
                valorp = float(values['-VALOR1-'])
                valorm = float(values['-VALOR2-'])
                valord = float(values['-VALOR3-'])

                # Calcula o valor3 usando a regra de três
                resultado = (valorp * valorm) / valord

                # Exibe o valor3 no campo de input correspondente
                window['-RESULTADO-'].update(resultado)

            except ValueError:
                sg.popup("Por favor, insira apenas números válidos.")

    window.close()


if __name__ == "__main__":
    main()
