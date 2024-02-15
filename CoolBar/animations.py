from time import time

# Bad code!

def animations(animation) -> tuple[list[str], int]:
    wave = ['▁', '▃', '▅', '▇', '█', '▇', '▅', '▃']
    spin = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇']
    arrows = ['←', '↖', '↑', '↗', '→', '↘', '↓', '↙']
    triangles = ['▲', '▶', '▼', '◀', '▲', '▶', '▼', '◀']
    line = ['|', '/', '—', '\\', '|', '/', '—', '\\']

    order = [wave.copy(), line.copy(), spin.copy(), arrows.copy(), triangles.copy()]
    return order[animation % len(order) - 1], animation % (len(order) + 1)


def main(string, animation) -> str:
    symbols, animation = animations(animation)

    timer = int((time() - int(time())) * len(symbols))

    if animation == 1:
        for _wave in range(3):
            string += symbols[(timer + len(symbols) + _wave % len(symbols)) % len(symbols)]
    else:
        string += f" {symbols[timer]} "

    return string
