# Importar bibliotecas necessárias
import tkinter as tk
from tkinter import messagebox, Menu
import psutil
import usb.core
import usb.util

# Função para exibir os registros da CPU
def mostrar_registros_cpu():
    info_cpu = f"""
    Frequência Atual: {psutil.cpu_freq().current:.2f} MHz
    Frequência Mínima: {psutil.cpu_freq().min:.2f} MHz
    Frequência Máxima: {psutil.cpu_freq().max:.2f} MHz
    Utilização: {psutil.cpu_percent(interval=1)}%
    """
    text_box.insert(tk.END, "=== Registros da CPU ===\n" + info_cpu + "\n")

# Função para exibir posições de memória
def mostrar_posicoes_memoria():
    memoria = psutil.virtual_memory()
    info_memoria = f"""
    Memória Total: {memoria.total / (1024**3):.2f} GB
    Memória Disponível: {memoria.available / (1024**3):.2f} GB
    Memória Usada: {memoria.used / (1024**3):.2f} GB
    """
    text_box.insert(tk.END, "=== Posições de Memória ===\n" + info_memoria + "\n")

# Função para listar informações das portas USB
def listar_portas_usb():
    dispositivos = usb.core.find(find_all=True)
    if dispositivos is None:
        messagebox.showinfo("USB", "Nenhum dispositivo USB encontrado.")
        return
    usb_info = "=== Dispositivos USB ===\n"
    for dispositivo in dispositivos:
        usb_info += f"ID: {hex(dispositivo.idVendor)}:{hex(dispositivo.idProduct)}\n"
    text_box.insert(tk.END, usb_info + "\n")

# Criar a janela principal
janela = tk.Tk()
janela.title("Informações do Sistema")
janela.geometry("600x400")

# Criar uma barra de menu
menu = Menu(janela)
janela.config(menu=menu)

# Adicionar opções ao menu
menu_sistema = Menu(menu, tearoff=0)
menu_sistema.add_command(label="Mostrar Registros CPU", command=mostrar_registros_cpu)
menu_sistema.add_command(label="Mostrar Posições Memória", command=mostrar_posicoes_memoria)
menu_sistema.add_command(label="Listar Portas USB", command=listar_portas_usb)
menu_sistema.add_separator()
menu_sistema.add_command(label="Sair", command=janela.quit)
menu.add_cascade(label="Sistema", menu=menu_sistema)

# Caixa de texto para exibir as informações
text_box = tk.Text(janela, wrap=tk.WORD, height=20, width=70)
text_box.pack(pady=10)

# Botão para sair
botao_sair = tk.Button(janela, text="Sair", command=janela.quit)
botao_sair.pack(pady=5)

# Iniciar o loop principal da aplicação
janela.mainloop()
