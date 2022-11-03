class DFA1:
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
            if alphabet == 0:
                state = 1
            elif alphabet == 1:
                state = 3
            else:
                print("INVALID CHARACTER: ", alphabet)
        elif state == 1:
            if alphabet == 0:
                state = 0
            elif alphabet == 1:
                state = 2
            else:
                print("INVALID CHARACTER: ", alphabet)
        elif state == 2:
            if alphabet == 0:
                state = 3
            elif alphabet == 1:
                state = 1
            else:
                print("INVALID CHARACTER: ", alphabet)
        elif state == 3:
            if alphabet == 0:
                state = 2
            elif alphabet == 1:
                state = 0
            else:
                print("INVALID CHARACTER: ", alphabet)
        return state

    def DFA_working(self, neword):
        self.word = neword
        for i in self.word:
            self.current_state = self.transition(int(i), self.current_state)
        if self.current_state == 0:
            print("VALID STRING")
            DFA_file1 = open("DFA_file1.txt", "a")
            DFA_file1.write(inputString + "\n")
            DFA_file1.close()
        else:
            print("INVALID STRING")


if __name__ == "__main__":
    print("DFA 1 STARTING")
    inputString = str(input("Enter the String: "))
    S = DFA1()
    S.DFA_working(inputString)
