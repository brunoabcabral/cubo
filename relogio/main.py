import tkinter as tk
from time import strftime
#bruno#
def atualizar_horario():
    string_horario = strftime('%H:%M:%S %p')
    label_horario.config(text=string_horario)
    label_horario.after(1000, atualizar_horario)  # Atualiza a cada 1000 milissegundos (1 segundo)

# Criar a janela principal
janela_relogio = tk.Tk()
janela_relogio.title("Relógio")

# Rótulo para exibir o horário
label_horario = tk.Label(janela_relogio, font=('calibri', 40, 'bold'), background='black', foreground='white')
label_horario.pack(anchor='center')

# Chamar a função para atualizar o horário
atualizar_horario()

# Iniciar o loop principal da interface gráfica
janela_relogio.mainloop()
