class CPU:
    def __init__(self):
        # Registradores de propósito geral
        self.registers_16 = {"AX": 0, "BX": 0, "CX": 0, "DX": 0}  # 16 bits
        self.registers_32 = {"EAX": 0, "EBX": 0, "ECX": 0, "EDX": 0}  # 32 bits
        self.registers_64 = {"RAX": 0, "RBX": 0, "RCX": 0, "RDX": 0}  # 64 bits

        # Registradores de propósito específico
        self.special_registers = {
            "IP": 0, "SP": 0, "BP": 0,  # 16 bits
            "EIP": 0, "ESP": 0, "EBP": 0,  # 32 bits
            "RIP": 0, "RSP": 0, "RBP": 0  # 64 bits
        }

        # FLAGS
        self.flags = {"ZF": 0, "SF": 0, "OF": 0}  # Zero, Sign, Overflow flags

        # Registradores de controle
        self.control_registers = {"CR0": 0, "CR1": 0, "CR2": 0, "CR3": 0, "CR4": 0}

        # Registradores de depuração
        self.debug_registers = {"DR0": 0, "DR1": 0, "DR2": 0, "DR3": 0, "DR7": 0}

    def write_register(self, name, value):
        """Escreve no registrador especificado."""
        if name in self.registers_16:
            self.registers_16[name] = value & 0xFFFF
        elif name in self.registers_32:
            self.registers_32[name] = value & 0xFFFFFFFF
        elif name in self.registers_64:
            self.registers_64[name] = value
        elif name in self.special_registers:
            self.special_registers[name] = value
        elif name in self.control_registers:
            self.control_registers[name] = value
        elif name in self.debug_registers:
            self.debug_registers[name] = value
        elif name in self.flags:
            self.flags[name] = value
        else:
            raise ValueError(f"Registrador '{name}' não encontrado.")

    def read_register(self, name):
        """Lê o valor de um registrador."""
        if name in self.registers_16:
            return self.registers_16[name]
        elif name in self.registers_32:
            return self.registers_32[name]
        elif name in self.registers_64:
            return self.registers_64[name]
        elif name in self.special_registers:
            return self.special_registers[name]
        elif name in self.control_registers:
            return self.control_registers[name]
        elif name in self.debug_registers:
            return self.debug_registers[name]
        elif name in self.flags:
            return self.flags[name]
        else:
            raise ValueError(f"Registrador '{name}' não encontrado.")

    def display_registers(self):
        """Exibe todos os registradores."""
        print("=== Registradores de Propósito Geral ===")
        print("16 bits:", self.registers_16)
        print("32 bits:", self.registers_32)
        print("64 bits:", self.registers_64)
        print("\n=== Registradores de Propósito Específico ===")
        print(self.special_registers)
        print("\n=== FLAGS ===")
        print(self.flags)
        print("\n=== Registradores de Controle ===")
        print(self.control_registers)
        print("\n=== Registradores de Depuração ===")
        print(self.debug_registers)


# Exemplo de uso
cpu = CPU()

# Escrever valores
cpu.write_register("AX", 0x1234)
cpu.write_register("EAX", 0x12345678)
cpu.write_register("RAX", 0x123456789ABCDEF0)

# Ler e exibir valores
print("Valor de AX:", cpu.read_register("AX"))
cpu.display_registers()
