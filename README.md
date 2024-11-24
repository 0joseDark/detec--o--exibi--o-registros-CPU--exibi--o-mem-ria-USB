# detecção -exibição-registros-CPU,-exibição-memória-USB
"""
 - detecção e exibição de informações sobre registros da CPU, 
 - exibição de posições de memória e informações de portas USB
"""
Exibir as informações sobre registradores e memória em uma janela gráfica no Windows 10 usando Python, podemos utilizar o módulo **Tkinter** para criar a interface. Este exemplo cria uma janela com botões para "Ler Registradores", "Escrever Valores", e uma área para exibição.

### **O que este programa faz:**
1. **Janela Principal**:
   - Exibe os valores atuais dos registradores simulados.
   - Botões para ler registradores, escrever valores e sair.

2. **Escrever Valores**:
   - Abre uma janela para escrever no registrador desejado.
   - Insira o nome do registrador (e.g., `AX`, `EAX`) e um valor em hexadecimal.

3. **Atualização Dinâmica**:
   - Após escrever valores, você pode atualizá-los clicando em "Ler Registradores".

---

### **Como usar:**
1. Execute o programa.
2. Clique em **"Ler Registradores"** para exibir os valores simulados.
3. Clique em **"Escrever Valores"** para abrir uma janela de entrada.
4. Escreva o nome do registrador e o valor desejado.
5. Atualize a exibição clicando novamente em "Ler Registradores".

Este programa é ideal para **simular e exibir os registradores de uma CPU x86** em Python!
