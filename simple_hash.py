import random

BITS_32 = 0xFFFFFFFF
BITS_64 = 0xFFFFFFFFFFFFFFFF

fmt = {
    '8': "{:08x}",
    '16': "{:016x}",
}

class SimpleHash:
    MIN_DATA_LEN = 4

    def make_internal_state(self):
        return [0xFFFFFFFF] * 4

    def assure_min_length(self, data: bytes) -> bytes:
        total_len = len(data)
        if total_len < self.MIN_DATA_LEN:
            data = data + b'\x00' * (self.MIN_DATA_LEN - total_len)
        return data

    def split_parts(self, data: bytes) -> [bytes]:
        n = len(data) // 4
        parts = [data[i:i+n] for i in range(0, len(data), n)]
        return parts

    def rotate(self, data: int) -> int:
        return ((data << 5) | (data >> 3))

    def add_mask(self, data: int, mask = BITS_32):
        return data & mask

    def make_hash(self, words: [int], fmt: str) -> str:
        return ''.join(fmt.format(w) for w in words)

    def execute(self, data: bytes, mask = BITS_32, fmt = fmt['8']) -> str:
        words = self.make_internal_state()
        data = self.assure_min_length(data)
        parts = self.split_parts(data)
    
        # processa cada palavra
        for index in range(4):
            part = 0
            for b in parts[index]:
                part += (b << 5)

            rotated = self.rotate(part)

            words[index] = self.add_mask(rotated, mask)

        return self.make_hash(words, fmt)


s = 'navas.dev'

sh = SimpleHash()
print(sh.execute(s.encode(), mask=BITS_32, fmt=fmt['8']))
print(sh.execute(s.encode(), mask=BITS_64, fmt=fmt['16']))
