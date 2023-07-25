import PySimpleGUI as sg


def main():

    # Definição do tema Dark Blue3
    sg.theme('Yellow')

    # Definição do layout da interface
    layout = [
        [sg.Text('Valor 1:', size=(10, 1), pad=((10, 5), (5, 5))), sg.Input(key='-VALOR1-', size=(12, 1)),
         sg.Text('Valor 2:', size=(10, 1), pad=((10, 5), (5, 5))), sg.Input(key='-VALOR2-', size=(12, 1))],
        [sg.Text('Valor 3:', size=(10, 1), pad=((10, 5), (5, 10))), sg.Input(key='-VALOR3-', size=(12, 1)),
         sg.Text('Resultado:', size=(10, 1), pad=((10, 5), (5, 10))),
         sg.Input(key='-RESULTADO-', size=(12, 1), disabled=True)],
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
                valor1 = float(values['-VALOR1-'])
                valor2 = float(values['-VALOR2-'])
                valor3 = float(values['-VALOR3-'])

                # Calcula o valor3 usando a regra de três
                resultado = (valor2 * valor1) / valor3

                # Exibe o valor3 no campo de input correspondente
                window['-RESULTADO-'].update(resultado)

            except ValueError:
                sg.popup("Por favor, insira apenas números válidos.")

    window.close()


if __name__ == "__main__":
    main()
