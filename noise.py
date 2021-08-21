import random

from PIL import Image


class Noise:
    def __init__(self, iteration_num, width, height):
        self.iterator_num = iteration_num
        self.width = width
        self.height = height
        self.img = Image.new('L', (width, height))
        self.pix = self.img.load()
        self.buffer = 0

    def get_neighbors(self, x, y):
        o = self.pix[x, y - 1]
        u = self.pix[x, y + 1]
        r = self.pix[x + 1, y]
        l = self.pix[x - 1, y]
        return o, u, r, l

    def flatten(self):
        for x in range(self.width):
            for y in range(self.height):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    self.buffer += 1
                    pass
                else:
                    o, u, r, l = self.get_neighbors(x, y)
                    self.pix[x, y] = self.calc_pixels(o, u, r, l, self.pix[x, y])

    def calc_pixels(self, u, o, l, r, c):
        sum = u + o + l + r + c
        return int(sum / 5)

    def generate(self):
        for x in range(self.width):
            for y in range(self.height):
                self.pix[x, y] = random.randrange(0, 255, 1)

        for _ in range(self.iterator_num):
            self.flatten()
            print(f"iteration {_+1}")

        self.img.show()


noise = Noise(4, 720, 360)
noise.generate()


