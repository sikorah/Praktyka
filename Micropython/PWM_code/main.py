import machine
import time

PWM_GPIO = machine.Pin(22, machine.Pin.OUT)
ADC0_GPIO = machine.Pin(26)
ADC1_GPIO = machine.Pin(27)
Vref = 3.3

# Inicjalizacje

machine.mem32[0x4001c05c] = 0x3 << 4

pwm = machine.PWM(PWM_GPIO)
pwm.freq(400_000)
pwm.duty_u16(0)

adc0 = machine.ADC(ADC0_GPIO)
adc1 = machine.ADC(ADC1_GPIO)

def SetPWM(percent):
    duty = int(percent * 65535) // 100
    pwm.duty_u16(duty)

# Czytanie ADC i konwersja


def ReadVoltage(adc):
    samples = list()
    for i in range(100): 
        samples.append(adc.read_u16())
    return (sum(samples)/len(samples)) * 3.3 / 65535

csv = open("data.csv", "w")
csv.close()
print("PWM: U_in: U_base:")

for pwm_val in range(0, 101, 1):
    
    PWM = SetPWM(pwm_val)
    time.sleep(0.2)
    U_in = ReadVoltage(adc0)
    U_base = ReadVoltage(adc1)
    
    print("{:03d}% {:.3f}V {:.3f}V ".format(pwm_val, U_in, U_base))
    
    csv = open("data.csv", "at")
    csv.write("{:03d},{:4f},{:4f}\n".format(pwm_val,U_in,U_base))
    csv.close()
    

    