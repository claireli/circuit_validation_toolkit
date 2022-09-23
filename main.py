import os
#from led.calculator import LEDCalculator

DIVIDER = 60
DIV_1 = ('=' * DIVIDER)
DIV_2 = ('-' * DIVIDER)

def box_header(message):
  print(DIV_2)
  spacer = '|  '
  if '\n' in message:
    for line in message.split('\n'):
      spacing = DIVIDER - (len(spacer)+len(line))
      print(f'{spacer}{line}{" " * (spacing-1)}|')
  else:
    spacing = DIVIDER - (len(spacer)+len(message))
    print(f'{spacer}{message}{" " * (spacing-1)}|')
  
  print(DIV_2)

# ==================================
# LED FORWARD VOLTAGE DROP
# ==================================
# Typically 1.8 to 3.3 V

FWD_VOLT_DROP = {}
FWD_VOLT_DROP['red'] = 2.0
FWD_VOLT_DROP['orange'] = 2.0
FWD_VOLT_DROP['yellow'] = 2.1
FWD_VOLT_DROP['green'] = 2.2
FWD_VOLT_DROP['blue'] = 3.3
FWD_VOLT_DROP['white'] = 3.3

# ==================================
# LED FORWARD CURRENT
# ==================================
# If (current forward), unit is mA
# The maximum safe current you can continuously pass through the device without causing it damage

# COMMON RESISTOR VALUES
COMMON_RES = [10,15,22,33,47,68,100,150,220,330,470,680,1000,1500,2200,3300 ,4700,6800,10000]
 
def menu():
  print(' [1] LED')
  print(' [2] VOLTAGE SUPPLY')
  print(' [3] FORWARD CURRENT')
  print(' [*] CALCULATE')
  print(' [0] RESET')

if __name__ == '__main__':
  #LEDCalculator()
  OPERANDS = {}
  OPERANDS['leds'] = []
  OPERANDS['volt_supply'] = 0
  OPERANDS['fwd_current'] = 0

  while True:
    menu()
    OP = input('ADD COMPONENT: ')
    
    if OP == '1':
      # color
      color = input(' COLOR: ')
      # voltage drop
      voltage_drop = FWD_VOLT_DROP[color]
      OPERANDS['leds'].append(voltage_drop)
      print(f' FWD VOLT DROP: {voltage_drop}')
    elif OP == '2':
      OPERANDS['volt_supply'] = int(input(' VOLTAGE SUPPLY: '))
    elif OP == '3':
      OPERANDS['fwd_current'] = int(input(' FWD CURRENT mA: '))
    elif OP == '*':
      voltage_leds = sum(OPERANDS['leds'])
      RESISTOR_VALUE = ((OPERANDS['volt_supply'] - voltage_leds)/OPERANDS['fwd_current'])*1000

      for r in COMMON_RES:
        if r >= RESISTOR_VALUE:
          CLOSEST_R = r
          break
      result = f'TOTAL LED VOLTAGE DROP is {voltage_leds}\n'
      result += f'RESISTOR VALUE is {RESISTOR_VALUE}\n'
      result += f'THE CLOSEST RESISTOR is {CLOSEST_R}\n'

      box_header(result)

    elif OP == '0':
      OPERANDS['leds'] = []
      OPERANDS['volt_supply'] = 0
      OPERANDS['fwd_current'] = 0
      os.system('clear')


    print(DIV_1)
    print(OPERANDS)      
    print(DIV_1)
