# Desafio J - Painel de LEDs

## Descrição
João quer montar um painel de LEDs contendo diversos números. Porém, ele possui uma quantidade limitada de LEDs e não tem certeza se conseguirá montar todos os números desejados. Considerando a configuração dos LEDs dos números de `0` a `9`, crie um algoritmo que ajude João a descobrir a quantidade de LEDs necessária para montar um número.

## Tabela de LEDs por dígito
| Dígito | LEDs Necessários |
|--------|------------------|
| 0      | 6               |
| 1      | 2               |
| 2      | 5               |
| 3      | 5               |
| 4      | 4               |
| 5      | 5               |
| 6      | 6               |
| 7      | 3               |
| 8      | 7               |
| 9      | 6               |

## Entrada
A entrada contém:
1. Um número inteiro `N` (1 ≤ N ≤ 1000) representando o número de casos de teste.
2. `N` linhas contendo um número inteiro `S` (1 ≤ |S| ≤ 10^100), que corresponde ao valor que João quer montar com os LEDs.

## Saída
Para cada caso de teste, o programa deve imprimir uma linha indicando o número de LEDs necessários para montar o valor especificado, seguido pela palavra `leds`.

### Formato da Saída
```
<number_of_leds> leds
```

## Exemplo de Entrada e Saída

**Entrada**
```
3
115380
2819311
23456
```

**Saída**
```
27 leds
29 leds
25 leds
```

## Explicação do Exemplo
1. Para o número `115380`:
   - `1` precisa de 2 LEDs (duas vezes) => 4 LEDs
   - `5` precisa de 5 LEDs => 5 LEDs
   - `3` precisa de 5 LEDs => 5 LEDs
   - `8` precisa de 7 LEDs => 7 LEDs
   - `0` precisa de 6 LEDs => 6 LEDs
   - Total: 4 + 5 + 5 + 7 + 6 = 27 LEDs

2. Para o número `2819311`:
   - `2` precisa de 5 LEDs => 5 LEDs
   - `8` precisa de 7 LEDs => 7 LEDs
   - `1` precisa de 2 LEDs (duas vezes) => 4 LEDs
   - `9` precisa de 6 LEDs => 6 LEDs
   - `3` precisa de 5 LEDs => 5 LEDs
   - `1` precisa de 2 LEDs (duas vezes) => 4 LEDs
   - Total: 5 + 7 + 2 + 6 + 5 + 2 + 2 = 29 LEDs

3. Para o número `23456`:
   - `2` precisa de 5 LEDs => 5 LEDs
   - `3` precisa de 5 LEDs => 5 LEDs
   - `4` precisa de 4 LEDs => 4 LEDs
   - `5` precisa de 5 LEDs => 5 LEDs
   - `6` precisa de 6 LEDs => 6 LEDs
   - Total: 5 + 5 + 4 + 5 + 6 = 25 LEDs

## Solução do Problema

### Lógica Utilizada
1. Usamos um dicionário para mapear cada dígito (`0` a `9`) ao número de LEDs necessários para exibi-lo.
2. Para cada número de entrada:
   - Lemos o número como uma string para poder acessar cada dígito individualmente.
   - Para cada dígito, consultamos o dicionário e somamos o número de LEDs necessários.
3. Imprimimos o total de LEDs necessários para cada número, seguido da palavra `leds`.

### Implementação em Python

```python
# Dicionário que mapeia cada dígito para o número de LEDs necessários
led_count = {
    '0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
    '5': 5, '6': 6, '7': 3, '8': 7, '9': 6
}

# Função para calcular a quantidade de LEDs necessária para um número
def calculate_leds(number):
    return sum(led_count[digit] for digit in number)

# Leitura da entrada
n = int(input())
for _ in range(n):
    num = input().strip()
    total_leds = calculate_leds(num)
    print(f"{total_leds} leds")
```

### Como Executar
1. Copie o código para um arquivo Python (`leds_calculator.py`).
2. Execute o script no terminal:
   ```bash
   python3 leds_calculator.py
   ```
3. Insira os valores conforme o exemplo de entrada.

### Complexidade
A complexidade do algoritmo é `O(N * M)`, onde `N` é o número de casos de teste e `M` é o número de dígitos em cada número. Dado que `M` pode ser no máximo `100` (pois cada número pode ter até `10^100` dígitos), o algoritmo é eficiente o suficiente para os limites propostos no problema.

## Observações
- Certifique-se de que o programa está utilizando `input().strip()` para evitar problemas com espaços em branco.
- Teste o código em diferentes ambientes (como a plataforma Beecrowd) para garantir que ele funcione corretamente.
