import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        messagebox.showinfo("Resultado", f"Seu IMC é: {imc:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor válido para peso e altura.")

def calcular_agua():
    try:
        peso = float(entry_peso.get())
        quantidade_agua = peso * 0.033
        messagebox.showinfo("Resultado", f"A quantidade ideal de água por dia para você é: {quantidade_agua:.2f} litros")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor válido para o peso.")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de IMC e Água")

# Criando widgets
label_peso = tk.Label(root, text="Peso (kg):")
label_altura = tk.Label(root, text="Altura (m):")
entry_peso = tk.Entry(root)
entry_altura = tk.Entry(root)
button_calcular_imc = tk.Button(root, text="Calcular IMC", command=calcular_imc)
button_calcular_agua = tk.Button(root, text="Calcular Água", command=calcular_agua)

# Posicionando os widgets na janela
label_peso.grid(row=0, column=0, padx=10, pady=5)
entry_peso.grid(row=0, column=1, padx=10, pady=5)
label_altura.grid(row=1, column=0, padx=10, pady=5)
entry_altura.grid(row=1, column=1, padx=10, pady=5)
button_calcular_imc.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
button_calcular_agua.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

# Rodando a aplicação
root.mainloop()
