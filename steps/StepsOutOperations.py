from abc import ABCMeta, abstractmethod

class StepsOutOperations():

    exe = tc.EXE
    def __init__(self, exe) -> None:
        self.exe = exe

    def before_test_operation(self):

        if exe.Exists and exe.ReadyToStart:
            Sys.process.start(self.exe)

        else:
            Sys.process.restart()
            Log.Message(f'.exe был перезапущен {Sys.process.count} раз')

    def after_test_operation(self):
        Sys.process.close(self.exe)