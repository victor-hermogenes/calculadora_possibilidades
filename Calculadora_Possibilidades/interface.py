import os
import fitz  # Importe a biblioteca PyMuPDF (Fitz)
import PySimpleGUI as sg

def main():
    # Definição do caminho do arquivo PDF
    pdf_file = "LOGO_MAHALO_H.pdf"

    # Carregue o arquivo PDF
    pdf_document = fitz.open(pdf_file)

    # Obtenha a primeira página do PDF
    pdf_page = pdf_document[0]

    # Renderize a primeira página como imagem
    pixmap = pdf_page.get_pixmap()
    image_bytes = pixmap.get_png_data()

    # Definição do layout da interface
    layout = [
        [sg.Image(data=image_bytes)],
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

    # Feche o arquivo PDF
    pdf_document.close()

    window.close()

if __name__ == "__main__":
    main()

