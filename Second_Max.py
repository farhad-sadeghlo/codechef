class second_max:
    def __init__(self):
        self.counter = int(input('please type in your number of lists: '))
        self.lists = [sorted(list(map(int, input(f'please type in your list {count + 1}: ').
                                      rstrip().split()))) for count in range(self.counter)]
    def second_max(self):

        for lst in self.lists:

            print(lst[1])
