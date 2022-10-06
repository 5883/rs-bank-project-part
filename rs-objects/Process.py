# Управление процессом
from ToolsSet import CONST


class Proc:

    def __init__(self) -> None:
        self.process_names = ["termw", "EXCEL", "WINWORD"]
        self.terminal = TestedApps.termwGREY
        self.wait_time = CONST.WAIT_TIME_FOR_WINDOWS

    # Возвращяет процесс  без проверки
    def used_process(self):
        return Sys.Process("termw")

    # Возвращяет процесс с проверкой
    def checked_used_process(self):
        wait_process = Sys.WaitProcess(self.process_names[0], self.wait_time)
        if wait_process.Exists:
            return wait_process

    # Запуск процесса
    def run_terminal():
        # Закрытие лишних приложении
        for appName in self.process_names: control.forcedСlosingApps(appName)

        # Запуск тестируемого ПО
        self.terminal.Run()
        window.process()
        w1 = window.winI()
        w1.Maximize()
        w1.Activate()
