from sys import stdout
from time import time
from .animations import main


class Bar:
    def __init__(self, total: int, bar_amount: int = 20, animation: int = 1) -> None:
        if total <= 0:
            raise ValueError("The 'total' parameter must be a positive integer greater than zero.")
        if not isinstance(total, int):
            raise ValueError("The 'total' parameter must be an integer.")

        self.done = 0
        self.total = total
        self.amount = bar_amount
        self.animation = animation

        self.start_time = time()
        self.elapsed_time = 0.0
        self.averages = []

        self.max_string_length = 0

    def update(self, done: int) -> bool:
        """
        Updates the progress bar with the given completed tasks.

        :param done: Number of completed tasks.
        :return: True if all tasks are completed, False otherwise.
        """
        self.done = done

        if self.done >= self.total:
            self._output("(!)")
        elif self.animation != 0:
            self._output(main("", self.animation))
        else:
            self._output("...")

        self.start_time = time()
        return self.done >= self.total

    def _output(self, prefix: str) -> None:
        """
        Outputs the progress bar.

        :param prefix: Prefix for the animation.
        """
        filled_bars = int(self.amount * self.done / self.total)

        # Progress bar
        progress_bar = f"{prefix} ["
        progress_bar += "█" * filled_bars
        progress_bar += "-" * (self.amount - filled_bars)
        progress_bar += "] "

        # Progress tracker
        progress_bar += f"{self.done}/{self.total} "
        progress_bar += f"[{self.done / self.total * 100:.1f}%]"

        # Time tracker
        self.elapsed_time = time() - self.start_time
        self.averages.append(self.elapsed_time)
        if self.done < self.total:
            average = sum(self.averages) / len(self.averages)
            progress_bar += f" ({self.elapsed_time:.3f}s, eta: {int(average * (self.total - self.done))}s)"
        else:
            progress_bar += f" (Done in {sum(self.averages):.3f} seconds)"

        # Fix overflow error
        progress_bar += " " * (self.max_string_length - len(progress_bar))
        self.max_string_length = len(progress_bar)

        # Write to the console
        stdout.write(f"\r{progress_bar}")
        stdout.flush()
