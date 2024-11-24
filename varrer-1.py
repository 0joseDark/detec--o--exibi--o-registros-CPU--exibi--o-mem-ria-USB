# Importar bibliotecas necessárias
import tkinter as tk
from tkinter import messagebox, Menu
import psutil
import platform
import usb.core
import usb.util

# Função para exibir os registros e o nome da CPU
def mostrar_registros_cpu():
    try:
        nome_cpu = platform.processor()  # Nome da CPU
        frequencia = psutil.cpu_freq()  # Frequências da CPU
        utilizacao = psutil.cpu_percent(interval=1)  # Utilização da CPU
        info_cpu = f"""
        Nome da CPU: {nome_cpu}
        Frequência Atual: {frequencia.current:.2f} MHz
        Frequência Mínima: {frequencia.min:.2f} MHz
        Frequência Máxima: {frequencia.max:.2f} MHz
        Utilização da CPU: {utilizacao}%
        """
        text_box.insert(tk.END, "=== Registros da CPU ===\n" + info_cpu + "\n")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao obter informações da CPU: {e}")

# Função para listar dispositivos USB conectados
def listar_portas_usb():
    try:
        dispositivos = usb.core.find(find_all=True)
        if dispositivos is None:
            text_box.insert(tk.END, "Nenhum dispositivo USB encontrado.\n")
            return
        usb_info = "=== Dispositivos USB ===\n"
        for dispositivo in dispositivos:
            fabricante = usb.util.get_string(dispositivo, dispositivo.iManufacturer) or "Desconhecido"
            produto = usb.util.get_string(dispositivo, dispositivo.iProduct) or "Desconhecido"
            porta = dispositivo.port_number or "Não disponível"
            usb_info += f"Fabricante: {fabricante}\nProduto: {produto}\nPorta: {porta}\n\n"
        text_box.insert(tk.END, usb_info)
    except usb.core.NoBackendError:
        messagebox.showerror("Erro", "Backend USB não encontrado. Instale o LibUSB.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao listar dispositivos USB: {e}")

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
