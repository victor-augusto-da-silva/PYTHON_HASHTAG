#flat é um sistema que serve tanto back-front e .exec, .web...etc
import flet as ft

def main(pagina):
    titulo = ft.Text("Hashzap")
    
    def enviar_mensagem(e):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
     
        texto = ft.Text(f"{nome_usuario} : {texto_campo_mensagem}")
        #adicione um dado no fim do chat
        chat.controls.append(texto)
        #Limpar caixa de enviar mensagem
        campo_enviar_mensagem.value = ""
        pagina.update()
    #onsubmit envia com enter, ele chama a função com o enter
    campo_enviar_mensagem =ft.TextField(label="Digite aqui sua mensagem!",on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar",on_click=enviar_mensagem)

    def abrir_popup(e):
        #ao cliclar em entrar ele chama um novo pop up
        pagina.dialog = popup
        popup.open=True
        #ele recarrega a pagina automaticamente
        pagina.update()
       

    #criação do pop up
    titulo_popup = ft.Text("Bem-Vindo ao HashZap")
    caixa_nome = ft.TextField(label="Digite seu nome")
    #exibe em forma de linha
    linha_enviar = ft.Row([campo_enviar_mensagem,botao_enviar])

    chat = ft.Column();



    def entrar_chat(e):
        popup.open=False
        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.add(chat)
        pagina.add(linha_enviar)
        #adicionar a mensagem de entrou no chat
        nome_usuario = caixa_nome.value
        texto_mensagem = f"O usuario {nome_usuario} entrou no chat"
        pagina.update()

    botao_popup = ft.ElevatedButton("Entrar no chat",on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup,content=caixa_nome,actions=[botao_popup])
    botao = ft.ElevatedButton("Iniciar Chat",on_click=abrir_popup)
    

    pagina.add(titulo)
    pagina.add(botao)

ft.app(main,view=ft.WEB_BROWSER)