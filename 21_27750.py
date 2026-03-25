from functools import lru_cache

@lru_cache(maxsize=None)
def vanya_can_win_by_move(x, y, move_num, max_move):
    """
    move_num: номер текущего хода (1=Петя, 2=Ваня, 3=Петя, 4=Ваня)
    Возвращает True если Ваня гарантированно выигрывает до max_move хода включительно
    """
    if x + y >= 82:
        # Игра уже закончена — выиграл тот, кто сделал предыдущий ход
        # Если предыдущий ход чётный — Ваня выиграл
        return (move_num - 1) % 2 == 0  # ход (move_num-1): чётный = Ваня

    if move_num > max_move:
        return False

    moves = [(x + 1, y), (x, y + 1), (x * 4, y), (x, y * 4)]

    if move_num % 2 == 1:  # Ход Пети — он минимизирует (хочет чтобы Ваня не выиграл)
        return all(vanya_can_win_by_move(nx, ny, move_num + 1, max_move) for nx, ny in moves) # при любом ходе Пети мы должны выиграть
    else:  # Ход Вани — он максимизирует
        return any(vanya_can_win_by_move(nx, ny, move_num + 1, max_move) for nx, ny in moves) # есть хотя бы один ход при котором мы побеждаем


results_1or2 = []
results_1 = []

for s in range(1, 78):
    x, y = 4, s
    wins_1or2 = vanya_can_win_by_move(x, y, 1, 4)
    wins_1 = vanya_can_win_by_move(x, y, 1, 2)

    if wins_1or2 and not wins_1:
        print(s)
        break
