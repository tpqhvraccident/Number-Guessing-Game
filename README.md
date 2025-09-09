# Number Guessing Game

A simple Python game where the computer tries to guess the number you are thinking of (between 1 and 100) using your hints.

## How to Play

1. Run `number_guessing_game.py`.
2. Think of a number between 1 and 100.
3. After each computer guess, respond with:
   - `h` if your number is **higher** than the guess
   - `l` if your number is **lower** than the guess
   - `c` if the guess is **correct**
4. The computer will guess until it finds your number!

## Example

```
Welcome to the Number Guessing Game!
Think of a number between 1 and 100, and I'll try to guess it.
After each guess, tell me if your number is (h)igher, (l)ower, or (c)orrect.
My guess is 50.
Is your number higher (h), lower (l), or correct (c)? h
My guess is 75.
Is your number higher (h), lower (l), or correct (c)? l
My guess is 62.
Is your number higher (h), lower (l), or correct (c)? h
...
```

## Requirements

- Python 3.x

## Run

```bash
python number_guessing_game.py
```

## License

MIT
