# Importar bibliotecas necessárias
import tkinter as tk
from tkinter import messagebox, Menu
import psutil
import usb.core
import usb.util

# Função para exibir os registros e o nome da CPU
def mostrar_registros_cpu():
    cpu_info = psutil.cpu_freq()
    nome_cpu = " ".join(psutil.cpu_info()[0].split()[:4])  # Extrair o nome principal da CPU
    info_cpu = f"""
    Nome da CPU: {nome_cpu}
    Frequência Atual: {cpu_info.current:.2f} MHz
    Frequência Mínima: {cpu_info.min:.2f} MHz
    Frequência Máxima: {cpu_info.max:.2f} MHz
    Utilização: {psutil.cpu_percent(interval=1)}%
    """
    text_box.insert(tk.END, "=== Registros da CPU ===\n" + info_cpu + "\n")

# Função para listar dispositivos USB conectados
def listar_portas_usb():
    dispositivos = usb.core.find(find_all=True)
    if dispositivos is None:
        text_box.insert(tk.END, "Nenhum dispositivo USB encontrado.\n")
        return
    usb_info = "=== Dispositivos USB ===\n"
    for dispositivo in dispositivos:
        fabricante = usb.util.get_string(dispositivo, dispositivo.iManufacturer)
        produto = usb.util.get_string(dispositivo, dispositivo.iProduct)
        porta = dispositivo.port_number
        usb_info += f"Fabricante: {fabricante}\nProduto: {produto}\nPorta: {porta}\n\n"
    text_box.insert(tk.END, usb_info)

# Criar a janela principal
janela = tk.Tk()
janela.title("Informações do Sistema")
janela.geometry("700x500")

# Criar uma barra de menu
menu = Menu(janela)
janela.config(menu=menu)

# Adicionar opções ao menu
menu_sistema = Menu(menu, tearoff=0)
menu_sistema.add_command(label="Mostrar Registros CPU", command=mostrar_registros_cpu)
menu_sistema.add_command(label="Listar Portas USB", command=listar_portas_usb)
menu_sistema.add_separator()
menu_sistema.add_command(label="Sair", command=janela.quit)
menu.add_cascade(label="Sistema", menu=menu_sistema)

# Caixa de texto para exibir as informações
text_box = tk.Text(janela, wrap=tk.WORD, height=25, width=80)
text_box.pack(pady=10)

# Botão para sair
botao_sair = tk.Button(janela, text="Sair", command=janela.quit)
botao_sair.pack(pady=5)

# Iniciar o loop principal da aplicação
janela.mainloop()
