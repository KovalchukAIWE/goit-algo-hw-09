# Список доступних монет
COINS = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    """
    Жадібний алгоритм для видачі решти.
    
    Аргументи:
        amount (int): сума, яку необхідно видавати.
    
    Повертає:
        dict: словник {номінал: кількість}, що показує, скільки монет кожного номіналу потрібно.
    
    Приклад:
        find_coins_greedy(113) -> {50: 2, 10: 1, 2: 1, 1: 1}
    """
    result = {}
    for coin in COINS:
        if amount >= coin:
            count = amount // coin  # визначаємо максимальну кількість монет цього номіналу
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount):
    """
    Алгоритм динамічного програмування для знаходження оптимального (мінімального) набору монет.
    
    Аргументи:
        amount (int): сума, яку необхідно видавати.
    
    Повертає:
        dict: словник {номінал: кількість}, що показує, скільки монет кожного номіналу використовувати.
    
    Приклад:
        find_min_coins(113) -> {50: 2, 10: 1, 2: 1, 1: 1}
    """
    # Ініціалізуємо dp-масив, де dp[i] - мінімальна кількість монет для суми i.
    dp = [float('inf')] * (amount + 1)
    # Масив для відновлення вибраних монет: coin_used[i] - монета, яку додали останньою для отримання суми i.
    coin_used = [None] * (amount + 1)
    
    dp[0] = 0  # базовий випадок: для суми 0 не потрібно монет
    
    # Обчислюємо dp[i] для кожної суми від 1 до amount
    for i in range(1, amount + 1):
        for coin in COINS:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Відновлюємо набір монет за допомогою масиву coin_used
    result = {}
    current = amount
    while current > 0:
        coin = coin_used[current]
        result[coin] = result.get(coin, 0) + 1
        current -= coin

    return result


# Приклад використання функцій
if __name__ == "__main__":
    test_amount = 113
    print("Жадібний алгоритм:")
    print(find_coins_greedy(test_amount))
    
    print("\nДинамічне програмування:")
    print(find_min_coins(test_amount))