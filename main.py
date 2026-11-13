import psutil
import platform
import time
import os

uname = platform.uname()

def clear():
    if os.environ == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def byets_legiveis(value, suffix="B"):
    if value is None:
        return "N/A"
    value = float(value)
    for unit in ("", "K", "M", "G", "T", "P"):
        if abs(value) < 1024:
            return f"{value:.2f}{unit}{suffix}"
        value /= 1024
    return f"{value:.2f}EB"

def cpu():
    
    print('=CPU='.center(50))
    print("-"*60)
    print('\n----ESPECIFICATIONS----')
    print("CPU_LOGICAL:", psutil.cpu_count(logical=True))  
    print("CPU_FISICAL:", psutil.cpu_count(logical=False),'\n')
    print('\n----USAGE----')
        
    per_cor = psutil.cpu_percent()
    freq = psutil.cpu_freq()
        
    print("CPU_CORE:", per_cor)
    print('CPU_FREQ:', round(freq.current, 2), 'MHz\n')

def ram():
    
    print('/=RAM=/'.center(50))    
    print('\n----ESPECIFICATIONS----')
    ram_virtual = psutil.virtual_memory()
    print("RAM_TOTAL:", byets_legiveis(ram_virtual.total), '\n')
    print('\n----USAGE----')
    print("USED_RAM:", byets_legiveis(ram_virtual.used))
    print("FREE_RAM:", byets_legiveis(ram_virtual.free))
    print('RAM_AVAILABLE:', byets_legiveis(ram_virtual.available,))
    print('RAM_CACHE:', byets_legiveis(ram_virtual.cached,'\n')) 

try:
    while True:
        
        clear()

        print('=Monitor do Systema='.center(50))
        print("-"*60)
        print(f'Sistema:', uname.system, uname.machine, uname.version.replace('#1 SMP PREEMPT_DYNAMIC', '-'))
        print("-"*60)
        cpu()

        print('-'*60)
        
        ram()
        
        time.sleep(0.5)
        
except KeyboardInterrupt:
    clear()
    print('KeyboardInterrupt: Monitor do Systema finalizado')
except Exception as e:
    clear()
    print(f'Error: {e}')