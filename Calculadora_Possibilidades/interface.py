import os
import shutil
import PySimpleGUI as sg

def main():
    # Definição do caminho da imagem
    image_source_path = os.path.join('C:\\Users\\Micro\\Downloads', 'LOGO_MAHALO_H.png')

    # Crie um diretório temporário para a imagem sem espaços no nome
    temp_directory = os.path.join(os.getcwd(), 'temp_images')
    os.makedirs(temp_directory, exist_ok=True)
    image_temp_path = os.path.join(temp_directory, 'logo.png')

    # Copie a imagem para o diretório temporário
    shutil.copy(image_source_path, image_temp_path)

    # Definição do layout da interface
    layout = [
        [sg.Image(filename=image_temp_path)],
        [sg.Text('Valor Principal:'), sg.Input(key='-VALOR_PRINCIPAL-')],
        [sg.Text('Valor Multiplicado:'), sg.Input(key='-VALOR_MULTIPLICADO-')],
        [sg.Text('Valor Dividido:'), sg.Input(key='-VALOR_DIVIDIDO-')],
        [sg.Button('Calcular'), sg.Button('Sair')]
    ]

    # Configuração do tamanho da janela
    window = sg.Window('Calculadora de Valores', layout, size=(1366, 768))

    # Loop para interação com a interface
    while True:
        event, values = window.read()

        # Se o usuário fechar a janela
        if event == sg.WINDOW_CLOSED or event == 'Sair':
            break

        # Se o usuário clicar no botão 'Calcular'
        if event == 'Calcular':
            try:
                valor_principal = float(values['-VALOR_PRINCIPAL-'])
                valor_multiplicado = float(values['-VALOR_MULTIPLICADO-'])
                valor_dividido = float(values['-VALOR_DIVIDIDO-'])

                # Realize as operações desejadas com os valores aqui
                # Por exemplo:
                # resultado = valor_principal * valor_multiplicado / valor_dividido
                # ou qualquer outra operação que você precise

                sg.popup(f"Resultado: {resultado}")

            except ValueError:
                sg.popup("Por favor, insira apenas números válidos.")

    # Exclua o diretório temporário e seu conteúdo após fechar a janela
    shutil.rmtree(temp_directory)

    window.close()

if __name__ == "__main__":
    main()
