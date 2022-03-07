import PySimpleGUI as sg
import sistemas.icones as i 


font = ('Futura, 15')


class Telas:
    def tela1():
        sg.theme('Dark')
        
        layout = [
            [sg.Column(Telas.layout_main(), justification='center')],
            [sg.Column(Telas.layout_campos(), justification='center')]
        ]
        
        return sg.Window('Tela Principal', layout=layout, finalize=True, )
    
    
    def layout_campos():
        layout_campos = [
            [sg.Frame('Consultar CEP', border_width=0, layout=Telas.layout_cep(), visible=False, font=font, key='-CONSULTAR_CEP-', title_location='n'),
             sg.Frame('Consultar Rastreio', layout=Telas.layout_rastreio(), border_width=0, visible=False, font=font, key='-CONSULTAR_RASTREIO-',title_location='n')]
        ]
        
        return layout_campos
    
    def layout_cep(): 
        layout = [
            [sg.Text('CEP'), sg.Input(key='-CEP_DESEJADO-', size=(30,0), border_width=0),
             sg.Button(image_data=i.btn_pesquisar, border_width=0, tooltip='Pesquisar CEP', button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-PESQUISAR-')],
            
        ]
        
        layout_cep = [
            [sg.Column(layout, justification='center')],
            [sg.Text("Logradouro", size=(10,0)), sg.Input(key='-LOGRADOURO-', size=(50,0), border_width=0, disabled=True, disabled_readonly_text_color=("Black"))],
            [sg.Text("Bairro", size=(10,0)), sg.Input(key='-BAIRRO-', size=(50,0), border_width=0, disabled=True, disabled_readonly_text_color=("Black"))],
            [sg.Text("Cidade", size=(10,0)), sg.Input(key='-CIDADE-', size=(20,0), border_width=0, disabled=True, disabled_readonly_text_color=("Black")),
            sg.Text("Cod.IBGE", size=(10,0)), sg.Input(key='-COD.IBGE_CIDADE-', size=(15,0), border_width=0, disabled=True, disabled_readonly_text_color=("Black"))],
            [sg.Text("Complemento", size=(10,0)), sg.Input(key='-COMPLEMENTO-', size=(20,0), border_width=0, disabled=True, disabled_readonly_text_color=("Black")),
            sg.Text("Estado", size=(10,0)), sg.Input(key='-ESTADO-', size=(15,0), border_width=0, disabled=True, disabled_readonly_text_color=("Black"))],      
        ]
        return layout_cep
    
    def layout_rastreio():
        layout = [
            
        ]
        
        layout_rastreio = [
             [sg.Column(layout, justification='center')]
        ]
        return layout_rastreio
    
    def layout_btn():
        layout_btn = [
            [sg.Button(image_data=i.btn_pesquisar_cep, border_width=0, tooltip='Pesquisar CEP', button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-CEP-'),
            sg.Button(image_data=i.btn_pesquisar_rastreio, border_width=0, tooltip='Pesquisar Rastreio', button_color=(sg.theme_background_color(), sg.theme_background_color()), key='-RASTREIO-'),],
        ]
        return layout_btn

    def layout_main():
        
        layout_main = [
            [sg.Button(image_data=i.btn_seta_baixo2, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color())), sg.Text('Clique na função que deseja usar abaixo', font=font), sg.Button(image_data=i.btn_seta_baixo, border_width=0, button_color=(sg.theme_background_color(), sg.theme_background_color()), )],
            [sg.Column(Telas.layout_btn(), justification='center')]
        
        ]
        return layout_main
    
    