import random

class BlackJack:

    __slots__ = ('max', 'client_score', 'bank_score')

    def __init__(self, max: int = 21):
        self.max = max
        self.client_score = 0
        self.bank_score = 0

    def _print_results(self):
        if not self.client_score > self.max and self.client_score > self.bank_score or self.client_score == self.max or self.bank_score > self.max:
            print(f'\nLe joueur a gagné avec un score de {self.client_score} !')
        elif not not self.bank_score > self.max and self.bank_score > self.client_score or self.bank_score == self.max or self.client_score > self.max:
            print(f'\nLe croupier a gagné avec un score de {self.bank_score}.')
        else:
            print(f'\nLa partie est nulle.\n  Joueur : {self.client_score}\n  Coupier : {self.bank_score}')

    def _print_detailed_results(self):
        if self.client_score > self.max and self.bank_score > self.max:
            print(f'\nLa partie est nulle, les deux joueurs ayants dépassés {self.max}.')
        elif self.client_score > self.max:
            print(f'\nLe joueur à dépassé {self.max} ({self.client_score}), il a donc perdu contre un score de {self.bank_score} du croupier.')
        elif self.bank_score > self.max:
            print(f'\nLe croupier à dépassé {self.max} ({self.bank_score}), il a donc perdu contre un score de {self.client_score} du joueur.')
        elif self.bank_score > self.client_score:
            print(f'\nLe croupier à un score supérieur à celui du joueur, il a donc gagné. ({self.bank_score} > {self.client_score})')
        elif self.client_score > self.bank_score:
            print(f'\nLe joueur à un score supérieur à celui du croupier, il a donc gagné. ({self.client_score} > {self.bank_score})')
        elif self.client_score == self.max:
            print(f'\nLe joueur à atteint {self.max} ! Le croupier à quant à lui un score de {self.bank_score}.')
        elif self.bank_score == self.max:
            print(f'\nLe croupier à atteint {self.max} ! Le joueur à quant à lui un score de {self.bank_score}.')
        print()

    def _print_current_score(self):
        print(f'\nScore du joueur : {self.client_score}\nScore du croupier : {self.bank_score}\n')

    def run(self, detailed_results = False):
        running = True
        while running:
            dices = int(input(f"Entrez le nombre de dés que vous voulez lancer (1-3) : \n--> "))
            if dices == 0:
                running = False
                continue
            if not 1 <= dices <= 3:
                print('Le nombre de dés doit être égal à 1, 2 ou 3.\n')
                continue
            for i in range(1, dices + 1):
                r = random.randint(1, 6)
                print(f'    Dé [{i}] : {r}')
                self.client_score += r
            for _ in range(1, dices + 1):
                self.bank_score += random.randint(1, 6)
            self._print_current_score()
            if self.client_score >= self.max or self.bank_score >= self.max: # A vérifier
                running = False
        replay_err = True
        while replay_err:
            if self.client_score < self.max and self.bank_score < self.max:
                replay = input(f'\nLe croupier doit-il rejouer (y/n) ? ')
            else:
                replay = 'n'
            if replay == 'y':
                replay_err = False
                r = random.randint(1, 6)
                self.bank_score += r
                print(f'\nLe croupier a fait un score supplémentaire de {r}.')
                self._print_current_score()
                if detailed_results:
                    self._print_detailed_results()
                else:
                    self._print_results()
            elif replay == 'n':
                replay_err = False
                if detailed_results:
                    self._print_detailed_results()
                else:
                    self._print_results()
            else:
                print('Erreur, veuillez écrire y (pour oui) et n (pour non).\n')

if __name__ == '__main__':
    bj = BlackJack()
    bj.run()