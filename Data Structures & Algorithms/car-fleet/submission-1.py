class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        fleets = 0
        last_eta = -math.inf
        for (p, s) in cars:
            eta = (target - p) / s
            if eta <= last_eta:
                continue
            else:
                fleets += 1
                last_eta = eta
        return fleets

