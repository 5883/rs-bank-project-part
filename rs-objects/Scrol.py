from VerifiedBaseObjects import Window
from Decor import DecorFunc


class Scroll(Window):
    check = DecorFunc.check_object_to_correct_display

    def __init__(self) -> None:
        super().__init__()
        self.w4 = "ewScrollWnd"

    # Ожидание поля
    @check()
    def scroll(self, object_path, edit_index=1):
        wait_field = self.window().WaitChild(self.w4, 3000)
        if wait_field.Exists and wait_field.Index == edit_index:
            return wait_field