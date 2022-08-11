import os

class Console:
    def log(self, text):
        print(text)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def warn(self, text):
        print(f'\033[31m{text}\033[0m')


console = Console()

console.log('Texto criativo.')
console.clear()
console.log('outro texto criativo.')
console.warn('Texto criativo com erro.')
