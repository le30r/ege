def get_moves(m, n):
    return [(m, n + 1), (m, n * 4), (m + 1, n), (m * 4, n)]

def can_win_now(m, n):
    return any(nm + ns >= 82 for nm, ns in get_moves(m, n)) # можем ли мы выиграть хотя бы одним ходом сейчас

def wins_on_move_2(m, n):
    if can_win_now(m, n): # проверяем что мы не можем выиграть с первого хода
        return False

    for pm, ps in get_moves(m, n): # для всех наших ходов
        if pm + ps >= 82:  # проверяем что не выигрываем
            continue

        vanya_moves = get_moves(pm, ps) # все ходы Вани

        if any(vm + vs >= 82 for vm, vs in vanya_moves): # если хотя бы один из них - выигрышный, нам такой ход не подходит
            continue

        if all(can_win_now(vm, vs) for vm, vs in vanya_moves): # если все ходы Вани из этой комбинации принесут нам победу следующим ходом, нам это подходит
            return True

    return False


results = []
for s in range(1, 78):
    if wins_on_move_2(4, s):
        results.append(s)
print(results)