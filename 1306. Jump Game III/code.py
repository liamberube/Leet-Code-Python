class Solution(object):
    def canReach(self, arr, start, n=0):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        if arr[start] == 0:
            return True
        elif n > len(arr):
            return False
        else:
            n += 1
            can_reach_up = False
            can_reach_down = False
            new_up = start + arr[start]
            if new_up >= 0 and new_up < len(arr):
                can_reach_up = self.canReach(arr, new_up, n)
                if can_reach_up == 'False' and n != 1:
                    return 'False'
                elif can_reach_up == 'False' and n == 1:
                    can_reach_up = False
                elif can_reach_up == True:
                    return True
            new_down = start - arr[start]
            if new_down >= 0 and new_down < len(arr):
                can_reach_down = self.canReach(arr, new_down, n)
                if can_reach_down == 'False' and n != 1:
                    return 'False'
                elif can_reach_down == 'False' and n == 1:
                    can_reach_down = False
                elif can_reach_down == True:
                    return True
            return can_reach_up or can_reach_down