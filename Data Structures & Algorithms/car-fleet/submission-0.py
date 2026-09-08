class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        fleets = []
        for (p, s) in cars:
            eta = (target - p) / s
            if fleets and eta <= fleets[-1]:
                continue
            else:
                fleets.append(eta)
        return len(fleets)

