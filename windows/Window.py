#
from BasicObjectsSuite import BaseObjects
from ObjectDecors import DecorTools


class Window(BaseObjects, DecorTools):
    checkCls = DecorTools()
    check = checkCls.checked

    def __init__(self) -> None:
        super().__init__()
        self.objectWaitTime = 1_000

    # Ожидание окна
    @check
    def window(self, wnd_caption="*", index=1):
        wait_window = self.second_wnd().WaitWindow(self.third_lvl_wnd, wnd_caption, -index, self.objectWaitTime)
        if wait_window.Exists:
            return wait_window

