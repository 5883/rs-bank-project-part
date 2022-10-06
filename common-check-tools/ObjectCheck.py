
class ObjectCheck:

    def __init__(self) -> None:

        self.status = False
        self.objectWaitTime = 40_000
        self.fieldWaitTime = 500

    # ------------- Проверка окон и объектов на корректное отображение -------------

    def checkCorrectDisplay(self, object):
        objectCaption = object.WndCaption

        if object.Exists and object.Visible and object.Enabled:
            self.status = True
            if objectCaption != "":
                Log.Message(f'Объект "{objectCaption}" доступен и отображается корректно')
            else:
                Log.Message(f'Объект "Без наименования" доступен и отображается корректно')
        else:
            Log.Warning(f'Объект "{objectCaption}" недоступно')
        return self.status

