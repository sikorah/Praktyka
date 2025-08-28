import machine
import time

PWM_GPIO = machine.Pin(22, machine.Pin.OUT)
ADC0_GPIO = machine.Pin(26)
ADC1_GPIO = machine.Pin(27)
ADC2_GPIO = machine.Pin(28)
Vref = 3.3

# Inicjalizacje

machine.mem32[0x4001c05c] = 0x3 << 4

pwm = machine.PWM(PWM_GPIO)
pwm.freq(400_000)
pwm.duty_u16(0)

adc0 = machine.ADC(ADC0_GPIO)
adc1 = machine.ADC(ADC1_GPIO)
adc2 = machine.ADC(ADC2_GPIO)

def SetPWM(percent):
    duty = int(percent * 65535) // 100
    pwm.duty_u16(duty)

# Czytanie ADC i konwersja


def ReadVoltage(adc):
    samples = list()
    for i in range(100): 
        samples.append(adc.read_u16())
    return (sum(samples)/len(samples)) * 3.3 / 65535

csv = open("data2.csv", "w")
csv.close()
print("PWM: U_in: U_base: U_col:")

for pwm_val in range(0, 101, 1):
    
    PWM = SetPWM(pwm_val)
    time.sleep(0.2)
    U_in = ReadVoltage(adc2)
    U_base = ReadVoltage(adc1)
    U_col = ReadVoltage(adc0)
    
    print("{:03d}% {:.3f}V {:.3f}V {:.3f}V".format(pwm_val, U_in, U_base, U_col))
    
    csv = open("data.csv", "at")
    csv.write("{:03d},{:4f},{:4f},{:.3f}V\n".format(pwm_val,U_in,U_base,U_col))
    csv.close()
    

    