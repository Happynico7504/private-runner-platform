from math import gcd

def factorization(n):

    factors = []

    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            print('*')
            for count in range(cycle_size):
                print('+')
                print(count)
                if factor > 1: break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)

            cycle_size *= 2
            x_fixed = x

        return factor

    while n > 1:
        print('\nf: \n')
        print(n)
        print('\n')
        next = get_factor(n)
        factors.append(next)
        n //= next

    return factors

result = factorization(76889510448807168345230106505231282172445482308350399964579551548209770977552809727399478220395677478798296017594029571570524874238967925338901224089283791776552686564367466679830236440714504227717064581635531814705999689011180826862755273540442376703746264986060890649139254495017631555645349469613309994811823941769464705576232626838164702053538653290972109374925392455122099808981496134836376486460084120265385857300477133112515652064502187118207043845481420283977389969095887678138051496625004050682396972160324085016179337957479568486756998545746143984479214853095389374835460811209024585274757021864016308815)
print('Result:')
print(result)