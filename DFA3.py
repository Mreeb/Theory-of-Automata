class DFA3:
    word = ''
    initial_state = 0
    current_state = 0
    valid = False

    def __int__(self):
        self.word = ''
        self.initial_state = 0

    def constructor(self, w, i):
        self.word = w
        self.initial_state = i

    def transition(self, alphabet, state):
        if state == 0:
            if alphabet == 'c':
                state = 1
            elif alphabet == 'a':
                state = 2
            elif alphabet == 'b':
                state = 2
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state == 1:
            if alphabet == 'a':
                state = 3
            elif alphabet == 'b':
                state = 2
            elif alphabet == 'c':
                state = 2
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state == 2:
            if alphabet == 'a':
                state = 3
            elif alphabet == 'b':
                state = 3
            elif alphabet == 'c':
                state = 3
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state == 3:
            if alphabet == 'a':
                state = 3
            elif alphabet == 'b':
                state = 3
            elif alphabet == 'c':
                state = 3
            else:
                print("INVALID CHARACTER: ", alphabet)
        return state


    def DFA_working(self, neword):
        self.word = neword
        for i in self.word:
            self.current_state = self.transition(str(i), self.current_state)
        if self.current_state == 2:
            print("VALID STRING")
            DFA_file3 = open("DFA_file3.txt", "a")
            DFA_file3.write(inputString + "\n")
            DFA_file3.close()
        else:
            print("INVALID STRING")


if __name__ == "__main__":
    print("DFA 3 STARTING")
    inputString = str(input("Enter the String: "))
    S = DFA3()
    S.DFA_working(inputString)
