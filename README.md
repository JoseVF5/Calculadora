# 🧮 Calculadora em Python (com Tkinter + MVC)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-FFDF00?style=for-the-badge&logo=python&logoColor=black)
![MVC](https://img.shields.io/badge/MVC-Pattern-5C2D91?style=for-the-badge)
![VSCode](https://img.shields.io/badge/Editor-VSCode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Windows](https://img.shields.io/badge/OS-Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

---

## 🧭 Sumário

- [📌 Objetivo](#-objetivo)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [🧱 Estrutura do Projeto](#-estrutura-do-projeto)
- [🖼️ Interface](#️-interface)
- [🧠 Funcionamento](#-funcionamento)
- [🚀 Como Executar](#-como-executar)
- [✅ Funcionalidades](#-funcionalidades)
- [📚 Aprendizados](#-aprendizados)
- [💡 Status do Projeto](#-Status-do-Projeto)
- [📸 Ícone](#-ícone)
- [🧑‍💻 Desenvolvedores](#-Desenvolvedores)
- [📄 Licença](#-licença)

---

## 📌 Objetivo

O projeto foi criado com o intuito de:
- Praticar **lógica de programação**.
- Aprender e aplicar a **estrutura MVC** em aplicações gráficas.
- Explorar os recursos do **Tkinter** para desenvolvimento de interfaces.
- Criar uma calculadora funcional com operações básicas e adicionais como **porcentagem** e **limpar/apagar entrada**.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Tkinter** (interface gráfica nativa)
- Arquitetura **MVC**
- **VSCode** como editor
- Sistema Operacional: **Windows**

---

## 🧱 Estrutura do Projeto

```
Calculadora/
├── Controller/
│   └── Data.py           # Lógica de controle da aplicação
├── Model/
│   └── Funcoes.py        # Operações matemáticas
├── View/
│   ├── interface.py      # Interface gráfica da calculadora
│   └── imagens/
│       └── Tittle Icon/
│           └── Python.ico
├── main.py               # Arquivo principal que inicia a aplicação
├── .gitignore
└── README.md
```

---

## 🖼️ Interface

A interface da calculadora é intuitiva, com:
- Botões para números de 0 a 9
- Operações básicas: `+`, `-`, `x`, `÷`
- Funções especiais: `C` (limpar), `⌫` (apagar), `%` (porcentagem), `.` (ponto decimal), `=` (resultado)
- Display superior para visualização da entrada e resultado

---

## 🧠 Funcionamento

- O **Controller** conecta a interface com as funções matemáticas.
- O **Model** realiza os cálculos com tratamento de erros (ex: divisão por zero).
- A **View** desenha toda a interface da calculadora com botões e display centralizado na tela.
- O **main.py** inicializa a aplicação e injeta as dependências.

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone o repositório:

   ```bash
   git clone https://github.com/SeuUsuario/Calculadora.git
   cd Calculadora
   ```

3. Execute o projeto:

   ```bash
   python main.py
   ```

---

## ✅ Funcionalidades

- [x] Interface gráfica amigável com botões interativos
- [x] Cálculos em tempo real
- [x] Sistema de apagar e limpar entrada
- [x] Porcentagem
- [x] Tratamento de erros (ex: divisão por zero)
- [x] Arquitetura MVC aplicada

---

## 📚 Aprendizados

Durante o desenvolvimento, aprendi a:
- Integrar a estrutura MVC em uma aplicação real com interface gráfica.
- Lidar com manipulação de eventos e centralização de tela no Tkinter.
- Organizar código em módulos reutilizáveis e de fácil manutenção.

---

## 💡 Status do Projeto

- [✓] Concluído

---

## 📸 Ícone

O projeto usa um ícone personalizado na janela:  
![Ícone](https://raw.githubusercontent.com/JoseVF5/Calculadora/41df4a2f483c0ec9bcc73d7d53d00888113d99e2/View/imagens/Tittle%20Icon/Python.ico)

---

## 🧑‍💻 Desenvolvedores

**[José Victor Freitas](https://github.com/JoseVF5)**  


---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
