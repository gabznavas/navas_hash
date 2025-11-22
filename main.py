import random

BITS_32 = 0xFFFFFFFF
BITS_64 = 0xFFFFFFFFFFFFFFFF
MIN_DATA_LEN = 4

fmt = {
    '8': "{:08x}",
    '16': "{:016x}",
}

class SimpleHash:
    def execute(self, data: bytes, mask = BITS_32, fmt = fmt['8']) -> str:
        # estado interno com 4 palavras
        words = [0xFFFFFFFF] * 4

        # garante tamanho mínimo
        total_len = len(data)
        if total_len < MIN_DATA_LEN:
            data = data + b'\x00' * (MIN_DATA_LEN - total_len)

        # divide em 4 partes
        n = len(data) // 4
        parts = [data[i:i+n] for i in range(0, len(data), n)]

        # processa cada palavra
        for index in range(4):
            part = 0
            for b in parts[index]:
                part += (b << 5)

            # rotação
            rotated = ((part << 5) | (part >> 3))

            # aplica máscara (define número de bits)
            words[index] = rotated & mask

        # monta hash em string
        hash_out = ''.join(fmt.format(w) for w in words)
        return hash_out


s = 'navas.dev'

sh = SimpleHash()
print(sh.execute(s.encode(), mask=BITS_32, fmt=fmt['8']))
print(sh.execute(s.encode(), mask=BITS_64, fmt=fmt['16']))
