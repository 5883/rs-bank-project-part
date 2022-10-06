# from BugHunters import BugHunter
from Messages import Msg


class ObjectTools():  # BugHunter

    msgCls = Msg()
    msg = msgCls.obj_msg

    def __init__(self) -> None:
        super().__init__()
        self.status = False
        self.objectWaitTime = 80_000
        self.fieldWaitTime = 200

    # --------------------- Проверка объекта на корректное отображение ---------------------
    @msg
    def check_object_to_correct_display(self, object):
        try:
            if object.Exists and object.Visible and object.Enabled:
                self.status = True
        except:
            Log.Warning(f'Проверяемый объект не найден. {object}')
        return self.status

    # --------------------- Проверка поля на наличие и на доступность для ввода ---------------------
    @msg
    def check_field_to_input(self, field):

        field.Click()
        Delay(self.fieldWaitTime)
        if self.check_object_to_correct_display(field) and field.Focused:
            self.status = True
        return self.status