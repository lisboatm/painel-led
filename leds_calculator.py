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
