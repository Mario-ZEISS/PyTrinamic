from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC6200
from pytrinamic.helpers import TMC_helpers


class TMC6200_eval(TMCLEval):
    """
    Use TMC6100-EVAL with Landungsbrücke/Startrampe at DRV spi channel to access the TMC6100.
    """
    def __init__(self, connection, module_id=1):
        TMCLEval.__init__(self, connection, module_id)
        self.ics = [TMC6200()]

    # use Landungsbrücke/Startrampe with DRV channel for register access

    def write_register(self, register_address, value):
        return self._connection.write_drv(register_address, value, self._module_id)

    def read_register(self, register_address, signed=False):
        return self._connection.read_drv(register_address, self._module_id, signed)

    def write_register_field(self, field, value):
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]),
                                   field[1], field[2], value))

    def read_register_field(self, field):
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])
