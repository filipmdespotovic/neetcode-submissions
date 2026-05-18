class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stek = []

        for asteroid in asteroids:
            if not stek or asteroid > 0:
                stek.append(asteroid)
                continue
            
            
            
            if stek[-1] < 0:
                stek.append(asteroid)
                continue

            while stek and stek[-1] > 0 and abs(asteroid) > stek[-1]:
                stek.pop()

            if not stek or stek[-1] < 0:
                stek.append(asteroid)
            
            if stek[-1] == abs(asteroid):
                stek.pop()

        return stek