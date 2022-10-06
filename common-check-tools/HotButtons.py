class HotButtons:

    def __init__(self) -> None:
        self.F2 = f'{"[F2]"}'
        self.F3 = f'{"[F3]"}'
        self.F4 = f'{"[F4]"}'
        self.F5 = f'{"[F5]"}'
        self.F6 = f'{"[F6]"}'
        self.F7 = f'{"[F6]"}'
        self.F8 = f'{"[F8]"}'
        self.F9 = f'{"[F9]"}'
        self.F10 = f'{"[F10]"}'
        self.F11 = f'{"[F11]"}'
        self.F12 = f'{"[F12]"}'
        self.Esc = f'{"[Esc]"}'
        self.Enter = f'{"[Enter]"}'

        self.buttonList = [
            self.F2,
            self.F3,
            self.F4,
            self.F5,
            self.F6,
            self.F7,
            self.F8,
            self.F9,
            self.F10,
            self.F11,
            self.F12,
            self.Esc,
            self.Enter,
        ]


        def getButtons(self):
            return self.buttonList
