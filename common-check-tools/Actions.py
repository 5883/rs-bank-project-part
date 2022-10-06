# ----------------------------------------------#
# Набор инструментов для управления приложениями #
# ----------------------------------------------#
import HotButtons

class Actions:

    def __init__(self) -> None:
        super().__init__()


    # -----------------------Принудительное закрытие тестовых приложении-----------------------
    def forcedСlosingApps(self, appName):

        """
           appName - принимает наименование процесса
        """
        wProcess = Sys.WaitProcess(appName, 3000)
        if wProcess.Exists:
            wProcess.Refresh()
            x = 1
            while Sys.WaitProcess(appName, 900, x).Exists:
                Sys.Process(appName, x).Terminate()
                x += 1
                Log.Message(f'"{appName}" с индексом "{x}" был закрыт')

    #


