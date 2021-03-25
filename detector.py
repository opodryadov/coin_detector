import cv2
import numpy
import os


class CoinDetector:
    def __init__(self, image):
        self.image = cv2.imread(os.path.abspath(image))

        # prep image - blur and convert to grey scale
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.blur = cv2.medianBlur(self.gray, 7)

        self.total_coins = 0
        self.total_amount = 0

    # find contours, recognize coins and calc total amount
    def find_contours(self):
        radius, coins = [], []
        one, two, five, ten = 0, 0, 0, 0

        circles = cv2.HoughCircles(self.blur, cv2.HOUGH_GRADIENT, 1.9, 100,
                                   param1=200, param2=100, minRadius=50, maxRadius=120)

        if circles is not None:
            circles = numpy.round(circles[0, :]).astype('int')

            for (x, y, r) in circles:
                cv2.circle(self.image, (x, y), r, (0, 255, 0), 2)
                radius.append([r, x, y])

        radius.sort()

        for i in radius:
            coins.append(i[0] / radius[0][0])

        for coin in coins:
            if 0.97 <= coin <= 1.03:
                one += 1
            elif 1.04 <= coin <= 1.128:
                two += 1
            elif 1.20 <= coin <= 1.25:
                five += 1
            else:
                ten += 1

        self.total_coins = len(coins)
        self.total_amount = one * 1 + two * 2 + five * 5 + ten * 10

    @property
    def size(self):
        height, width = self.image.shape[0], self.image.shape[1]
        return height, width

    @property
    def average_color(self):
        avg_color = list(map(int, [self.image[:, :, i].mean() for i in range(self.image.shape[-1])]))
        return avg_color
