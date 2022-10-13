import tkinter as tk

janela =tk.Tk()

var_receberemail = tk.IntVar()
var_politicas = tk.IntVar()

checkbox_receberemail = tk.Checkbutton(text="Eu autorizo o envio de promoções para o meu e-mail", variable=var_receberemail)
checkbox_politicas = tk.Checkbutton(text="Eu concordo com os Termos de Uso", variable=var_politicas)
checkbox_receberemail.grid(row=0, column=0)
checkbox_politicas.grid(row=1, column=0)

def enviar_dados():
    if var_receberemail.get():
        print('Usuário deseja receber e-mails promocionais')
    else:
        print('Usuário não deseja receber e-mails promocionais')
    if var_politicas.get():
        print('Usuário concorda com as políticas')
    else:
        print('Usuário não concorda com as políticas')

botão_enviar = tk.Button(text='Enviar', command=enviar_dados)
botão_enviar.grid(row=2, column=0)

janela.mainloop()
