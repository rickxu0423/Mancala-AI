class Human:
    def __init__(self, name):
        self.name = name

    def choice(self):
        command = ""
        while not command:
            command = input("{}(human) move: ".format(self.name)).split()
            if not command:
                continue
            choice = int(command[0]) - 1
        return choice