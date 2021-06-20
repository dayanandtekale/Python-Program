from cars.abc import ABC as ab
from cars.pqr import PQR as pq

if __name__ == "__main__":
    instanceABC = pq()
    instanceABC.speedKMPH(1000)
    