class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ans = 0
        for i in range(len(energy)):
            if initialEnergy <= energy[i]:
                ans += energy[i]+1 - initialEnergy
                initialEnergy = 1
            else:
                initialEnergy -= energy[i]
            if initialExperience <= experience[i]:
                ans += experience[i]+1 - initialExperience
                initialExperience += experience[i]+1 - initialExperience
            initialExperience += experience[i]
        return ans