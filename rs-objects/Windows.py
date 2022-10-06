# Проверенный Window объект
from FoundationForObjects import FoundationObjects
from CheckObjectDecors import CheckDecorTools


class Window(FoundationObjects, CheckDecorTools):
    check_cls = CheckDecorTools()
    check = check_cls.checked

    def __init__(self) -> None:
        super().__init__()
        self.objectWaitTime = 60_000

    @check
    def window(self, wnd_caption="*", index=1):
        wait_window = self.second_wnd().WaitWindow(self.third_lvl_wnd, wnd_caption, -index, self.objectWaitTime)
        if wait_window.Exists:
            return wait_window

    @check
    def window_1(self, wnd_caption="*", index=1):
        wait_window = self.used_process().WaitWindow(self.first_lvl_wnd, wnd_caption, -index, self.objectWaitTime)
        if wait_window.Exists:
            return wait_window

    @check
    def window_2(self, wnd_caption="*", index=1):
        wait_window = self.first_wnd().WaitWindow(self.second_lvl_wnd, wnd_caption, -index, self.objectWaitTime)
        if wait_window.Exists:
            return wait_window




