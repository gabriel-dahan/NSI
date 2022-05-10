## EXERCICE 1 :

def ip_address(ip: str, mask: str) -> str:
    return '.'.join([int(ip_bdigit) & int(mask_bdigit) for ip_bdigit, mask_bdigit in zip(ip.split('.'), mask.split('.'))])

def addresses_nb(mask: str):
    zeros = 0
    for digit in mask.split('.'):
        bdigit = bin(int(digit))[2:]
        if bdigit == '0':
            zeros += 8
        elif '0' in bdigit:
            zeros += bdigit.count('0')
    return 2 ** zeros - 2

if __name__ == '__main__':
    # print(ip_address('115.250.207.0', '255.255.240.0')) # EX 1
    print(addresses_nb('255.255.240.0')) # EX 2