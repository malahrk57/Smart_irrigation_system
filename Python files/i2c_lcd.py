from lcd_api import LcdApi
from time import sleep_ms

class I2cLcd(LcdApi):

    MASK_RS = 0x01
    MASK_RW = 0x02
    MASK_E  = 0x04
    SHIFT_BACKLIGHT = 3
    SHIFT_DATA = 4

    def __init__(self, i2c, i2c_addr, num_lines, num_columns):
        self.i2c = i2c
        self.i2c_addr = i2c_addr
        self.backlight = 1

        sleep_ms(20)

        self.hal_write_init_nibble(0x03)
        sleep_ms(5)
        self.hal_write_init_nibble(0x03)
        sleep_ms(5)
        self.hal_write_init_nibble(0x03)
        sleep_ms(5)
        self.hal_write_init_nibble(0x02)

        LcdApi.__init__(self, num_lines, num_columns)

        cmd = self.LCD_FUNCTION | self.LCD_FUNCTION_2LINES
        self.hal_write_command(cmd)

        self.hal_write_command(self.LCD_ON_CTRL | self.LCD_ON_DISPLAY)

        self.clear()

        self.hal_write_command(self.LCD_ENTRY_MODE | self.LCD_ENTRY_INC)

    def hal_write_init_nibble(self, nibble):
        byte = ((nibble << self.SHIFT_DATA) |
                (self.backlight << self.SHIFT_BACKLIGHT))
        self.i2c.writeto(self.i2c_addr, bytes([byte | self.MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytes([byte]))

    def hal_write_command(self, cmd):
        self.hal_write_byte(cmd, 0)

    def hal_write_data(self, data):
        self.hal_write_byte(data, self.MASK_RS)

    def hal_write_byte(self, byte, mode):
        high = mode | ((byte >> 4) << self.SHIFT_DATA) | (self.backlight << self.SHIFT_BACKLIGHT)
        low = mode | ((byte & 0x0F) << self.SHIFT_DATA) | (self.backlight << self.SHIFT_BACKLIGHT)

        self.i2c.writeto(self.i2c_addr, bytes([high | self.MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytes([high]))

        self.i2c.writeto(self.i2c_addr, bytes([low | self.MASK_E]))
        self.i2c.writeto(self.i2c_addr, bytes([low]))
