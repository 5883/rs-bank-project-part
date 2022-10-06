from Windows import Window
from ObjectDecors import DecorTools


class Fields(Window):
    check = DecorTools.checked_field

    def __init__(self) -> None:
        super().__init__()
        self.w4 = "Edit"

    # Ожидание поля
    @check
    def fileld(self, object_path, edit_index=1):
        wait_field = object_path.WaitChild(self.w4, 3000)
        if wait_field.Exists and wait_field.Index == edit_index:
            return wait_field