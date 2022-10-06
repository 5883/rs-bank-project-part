from Process import Proc


class BaseObjects(Proc):

    def __init__(self) -> None:
        self.first_lvl_wnd = "ewFrameWnd"
        self.second_lvl_wnd = "ewClientWnd"
        self.third_lvl_wnd = "ewDialogWnd"

    # Возвращяет окно без проверки
    def first_wnd(self, wnd_caption="*", index=1):
        w1 = self.used_process().Window(self.first_lvl_wnd, wnd_caption, index)
        return w1

    def second_wnd(self, wnd_caption="*", index=1):
        w2 = self.first_wnd().Window(self.second_lvl_wnd, wnd_caption, index)
        return w2

    def third_wnd(self, wnd_caption="*", index=1):
        w3 = self.second_wnd().Window(self.third_lvl_wnd, wnd_caption, index)
        return w3


