import tkinter as tk
from tkinter import messagebox

def calcular_media():
    try:
        aluno = entry_aluno.get()
        materia = entry_materia.get()
        nota_1 = float(entry_nota1.get())
        nota_2 = float(entry_nota2.get())
        nota_3 = float(entry_nota3.get())

        calcularMEDIA = (nota_1 + nota_2 + nota_3) / 3

        if calcularMEDIA >= 7:
            resultado = (f"O aluno {aluno}, foi aprovado na materia de {materia} com a média {calcularMEDIA: .2f}. Esperamos que ele continue assim!")
        else:
            resultado = (f"O aluno {aluno}, infelizmente nao foi aprovado na materia de {materia}. Esperamos que ele estude mais!")

        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para as notas.")

#JANELA INTERATIVA

root = tk.Tk()
root.title("CALCULADORA DE MEDIA BIMESTRAL - For MATHEUS FLORENCIO")

#WIDGETS 

tk.Label(root, text="Digite o nome do aluno:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_aluno = tk.Entry(root, width=40)
entry_aluno.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Digite o nome da matéria:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_materia = tk.Entry(root, width=40)
entry_materia.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Digite a primeira nota:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_nota1 = tk.Entry(root, width=10)
entry_nota1.grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Label(root, text="Digite a segunda nota:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_nota2 = tk.Entry(root, width=10)
entry_nota2.grid(row=3, column=1, padx=10, pady=5, sticky="w")

tk.Label(root, text="Digite a terceira nota:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_nota3 = tk.Entry(root, width=10)
entry_nota3.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Botão para calcular a média
tk.Button(root, text="Calcular Média", command=calcular_media).grid(row=5, column=0, columnspan=2, pady=20)

# Inicia o loop principal da interface gráfica
root.mainloop()




