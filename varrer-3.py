import tkinter as tk
from tkinter import ttk, messagebox


class CPU:
    def __init__(self):
        # Registradores simulados
        self.registers_16 = {"AX": 0, "BX": 0, "CX": 0, "DX": 0}
        self.registers_32 = {"EAX": 0, "EBX": 0, "ECX": 0, "EDX": 0}
        self.registers_64 = {"RAX": 0, "RBX": 0, "RCX": 0, "RDX": 0}

    def write_register(self, name, value):
        """Escreve no registrador."""
        try:
            if name in self.registers_16:
                self.registers_16[name] = value & 0xFFFF
            elif name in self.registers_32:
                self.registers_32[name] = value & 0xFFFFFFFF
            elif name in self.registers_64:
                self.registers_64[name] = value
            else:
                raise ValueError("Registrador inválido.")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def read_registers(self):
        """Retorna todos os registradores formatados."""
        output = "=== Registradores de 16 bits ===\n"
        output += "\n".join([f"{reg}: {val:#06x}" for reg, val in self.registers_16.items()])
        output += "\n\n=== Registradores de 32 bits ===\n"
        output += "\n".join([f"{reg}: {val:#010x}" for reg, val in self.registers_32.items()])
        output += "\n\n=== Registradores de 64 bits ===\n"
        output += "\n".join([f"{reg}: {val:#018x}" for reg, val in self.registers_64.items()])
        return output


class App:
    def __init__(self, root):
        self.cpu = CPU()  # Simulação da CPU

        # Configuração da janela
        root.title("Simulador de Registradores")
        root.geometry("600x400")
        root.resizable(False, False)

        # Campo de texto para exibir os registradores
        self.text_area = tk.Text(root, wrap=tk.WORD, font=("Consolas", 10))
        self.text_area.place(x=20, y=20, width=560, height=250)

        # Botão para ler os registradores
        btn_read = ttk.Button(root, text="Ler Registradores", command=self.display_registers)
        btn_read.place(x=20, y=300, width=150)

        # Botão para escrever no registrador
        btn_write = ttk.Button(root, text="Escrever Valores", command=self.write_register)
        btn_write.place(x=200, y=300, width=150)

        # Botão para sair
        btn_exit = ttk.Button(root, text="Sair", command=root.quit)
        btn_exit.place(x=380, y=300, width=150)

    def display_registers(self):
        """Exibe os registradores na área de texto."""
        self.text_area.delete(1.0, tk.END)  # Limpa o texto existente
        self.text_area.insert(tk.END, self.cpu.read_registers())  # Adiciona os registradores

    def write_register(self):
        """Janela para escrever no registrador."""
        write_window = tk.Toplevel()
        write_window.title("Escrever Registrador")
        write_window.geometry("300x200")
        write_window.resizable(False, False)

        # Entrada para o nome do registrador
        tk.Label(write_window, text="Nome do Registrador:").pack(pady=5)
        reg_entry = ttk.Entry(write_window)
        reg_entry.pack(pady=5)

        # Entrada para o valor
        tk.Label(write_window, text="Valor (em hexadecimal):").pack(pady=5)
        value_entry = ttk.Entry(write_window)
        value_entry.pack(pady=5)

        # Botão para salvar
        def save_value():
            reg_name = reg_entry.get().strip().upper()
            try:
                value = int(value_entry.get().strip(), 16)
                self.cpu.write_register(reg_name, value)
                messagebox.showinfo("Sucesso", f"Valor {value:#x} escrito em {reg_name}.")
                write_window.destroy()
            except ValueError:
                messagebox.showerror("Erro", "Valor inválido. Use hexadecimal (e.g., 0x1234).")

        ttk.Button(write_window, text="Salvar", command=save_value).pack(pady=20)


# Inicialização da aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
