import psutil
import platform
import time
import os
import colorama

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
    
    print(colorama.Fore.BLUE + '=CPU='.center(50))
    print(colorama.Fore.BLACK + "-"*60)
    print(colorama.Fore.WHITE + '\n----ESPECIFICATIONS----')
    print(colorama.Fore.GREEN + "CPU_LOGICAL:", psutil.cpu_count(logical=True))  
    print(colorama.Fore.GREEN + "CPU_FISICAL:", psutil.cpu_count(logical=False),'\n')
    print(colorama.Fore.WHITE + '\n----USAGE----')
        
    per_cor = psutil.cpu_percent()
    freq = psutil.cpu_freq()
        
    print(colorama.Fore.GREEN + "CPU_CORE:", per_cor)
    print(colorama.Fore.GREEN + 'CPU_FREQ:', round(freq.current, 2), 'MHz\n')

def ram():
    
    print(colorama.Fore.BLUE +'/=RAM=/'.center(50))    
    print(colorama.Fore.BLUE +'\n----ESPECIFICATIONS----')
    ram_virtual = psutil.virtual_memory()
    print(colorama.Fore.WHITE +"RAM_TOTAL:", byets_legiveis(ram_virtual.total), '\n')
    print(colorama.Fore.BLUE +'\n----USAGE----')
    print(colorama.Fore.RED +"USED_RAM:", byets_legiveis(ram_virtual.used))
    print(colorama.Fore.GREEN +"FREE_RAM:", byets_legiveis(ram_virtual.free))
    print(colorama.Fore.YELLOW +'RAM_AVAILABLE:', byets_legiveis(ram_virtual.available,))
    print(colorama.Fore.YELLOW +'RAM_CACHE:', byets_legiveis(ram_virtual.cached,'\n')) 

def swap():
 
    print(colorama.Fore.BLUE +'/=SWAP=/'.center(50))    
    print(colorama.Fore.BLUE +'\n----ESPECIFICATIONS----')
    swap = psutil.swap_memory()
    print(colorama.Fore.WHITE +"SWAP_TOTAL:", byets_legiveis(swap.total), '\n')
    print(colorama.Fore.BLUE +'\n ----USAGE----')
    print(colorama.Fore.RED +"USED_SWAP:", byets_legiveis(swap.used)) 
    print(colorama.Fore.GREEN +"FREE_SWAP:", byets_legiveis(swap.free))

try:
    while True:
        
        clear()

        print(colorama.Fore.BLUE + '=Monitor do Systema='.center(50))
        print(colorama.Fore.BLACK + "-"*60)
        print(colorama.Fore.BLUE + 'Sistema:', uname.system, uname.machine, uname.version.replace('#1 SMP PREEMPT_DYNAMIC', '-'))
        print(colorama.Fore.BLACK + "-"*60)
        cpu()
        print(colorama.Fore.BLACK +'-'*60)
        ram()
        print(colorama.Fore.BLACK +'-'*60)
        swap()
        time.sleep(0.5)
        
except KeyboardInterrupt:
    clear()
    print(colorama.Fore.RED + 'KeyboardInterrupt: Monitor do Systema finalizado')
except Exception as e:
    clear()
    print(colorama.Fore.RED + f'Error: {e}')