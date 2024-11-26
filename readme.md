

# Pixel Designer Maker

**Pixel Designer Maker (PDM)** é um software desenvolvido em Python, com o uso da biblioteca `pygame`, para criar objetos PDM. Esses objetos são utilizados na criação de jogos e animações baseadas em pixels. O PDM é uma ferramenta poderosa e versátil que permite manipular cores, criar animações, e até integrar projetos eletrônicos com LEDs.

## 🎨 Funcionalidades

- **Edição de Pixels**: Criação de matrizes de pixels editáveis.
- **Gestão de Cores**: Suporte a diferentes paletas de cores, incluindo modos 1-bit, 2-bit e RGB.
- **Geração de Arquivos PDM**: Salve designs no formato `.pdm` para integração em jogos ou outros projetos.
- **Modos de Animação**: Suporte à criação de animações quadro a quadro.
- **Integração com Projetos de LED**: Adaptação dos objetos PDM para uso em projetos de hardware, como matrizes de LEDs.

## 🛠️ Tecnologias Utilizadas

- **Python** (versão 3.8 ou superior)
- **Pygame** (biblioteca para criação de jogos e interfaces gráficas)

## 🖥️ Instalação e Execução

1. Clone este repositório:
   ```bash
   git clone hhttps://github.com/gabrieljsantos/Pixel-Designer-Maker.git
   cd pixel-designer-maker
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install pygame
   ```

3. Execute o software:
   ```bash
   python main.py
   ```

## 📁 Estrutura do Projeto

```
Pixel-Designer-Maker/
│
├── PDM Objects/                # Diretório para salvar objetos criados
├── Setup_Screen.py             # Configurações de tela e cores
├── ******.py                     # Arquivo principal
├── README.md                   # Documentação do projeto
└── requirements.txt            # Lista de dependências
```

## 🕹️ Como Usar

1. **Interface Principal**:
   - Edite sua matriz de pixels usando o mouse:
     - Botão esquerdo: Preenche um pixel.
     - Botão direito: Apaga um pixel.
   - Use os botões para salvar designs ou acessar o gerenciador de cores.

2. **Gerenciamento de Cores**:
   - Acesse a paleta de cores para selecionar ou personalizar a aparência de seus objetos.

3. **Salvar Design**:
   - Clique no botão **"Write Design"** para salvar o design atual em um arquivo `.pdm`.

## 🚀 Recursos Futuramente Planejados

- Suporte para mais tipos de animação.
- Exportação para formatos gráficos populares como `.png` ou `.gif`.
- Melhorias na integração com projetos de hardware.
- Ferramentas para edição avançada de animações.

## 🖼️ Exemplo de Uso

Design básico salvo em formato `.pdm`:

```pdm
(0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0),
(0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0),
(0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0),
...
```

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir **Issues** ou enviar **Pull Requests**.

1. Faça um fork do repositório.
2. Crie uma nova branch:
   ```bash
   git checkout -b minha-feature
   ```
3. Envie suas alterações:
   ```bash
   git commit -m "Adiciona minha nova feature"
   git push origin minha-feature
   ```

## 📜 Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

- **Gabriel de Jesus Santos**  
  Desenvolvedor apaixonado por jogos, animação e eletrônica!

---
