class Solution:
    def solve(goal_state, init_state=None):
        wears = ['MASK', 'LEFTEYE', 'RIGHTEYE', 'HAT', 'BAND']
        allparts = ['m1', 'm2', 'm3', 'm4', 'l1', 'l2', 'l3', 'l4', 'l5', 'r1', 'r2', 'r3', 'r4', 'r5', 'f1', 'f2',
                    'f3']
        wear2parts = {
            'MASK': {'m1', 'm2', 'm3', 'm4', 'l1', 'l2', 'l3', 'r1', 'r2', 'r3'},
            'LEFTEYE': {'l1', 'l2', 'l3', 'l4', 'l5'},
            'RIGHTEYE': {'r1', 'r2', 'r3', 'r4', 'r5'},
            'HAT': {'f1', 'f2', 'm1', 'm2', 'l1', 'l2', 'l4', 'r1', 'r2', 'r4'},
            'BAND': {'f2', 'f3', 'm2', 'm3', 'l2', 'l3', 'l4', 'l5', 'r2', 'r3', 'r4', 'r5'}
        }
        if init_state is None:
            init_state = {part: 'ORANGE' for part in allparts}
        considered_parts = set(allparts)
        
        wearcomblist = []
        cur = []
        def dfs(i):
            if i==len(wear2parts):
                wearcomblist.append(set(cur))
                return
            dfs(i+1)
            cur.append(wears[i])
            dfs(i+1)
            cur.pop()
        dfs(0)
        #print(wearcomblist)
        
        affpartslist = []
        for wearlist in wearcomblist:
            unaffected_parts = []
            for wear in wearlist:
                for part in wear2parts[wear]:
                    unaffected_parts.append(part)
            affpartslist.append(set(allparts) - set(unaffected_parts))
        #print(affpartslist)
        
        plan = []
        while considered_parts:
            maxnumparts = 0
            wearcombchosen = None
            colorchosen = None
            partschosen = None
            for i in range(len(wearcomblist)):
                wearcomb,affparts = wearcomblist[i],affpartslist[i]
                colored_parts = considered_parts.intersection(affparts)
                
                target_color = None
                possiblewearcomb = True
                for part in colored_parts:
                    if target_color is None:
                        target_color = goal_state[part]
                    elif target_color != goal_state[part]:
                        possiblewearcomb = False
                if not possiblewearcomb:
                    continue
                
                if len(colored_parts) > maxnumparts:
                    maxnumparts = len(colored_parts)
                    wearcombchosen = set(wearcomb)
                    colorchosen = target_color
                    partschosen = colored_parts
            action = (wearcombchosen, colorchosen)
            plan.append(action)
            for part in partschosen:
                considered_parts.discard(part)
            
        return plan

if __name__ == "__main__":
    colors = ['BLACK', 'WHITE', 'ORANGE', 'BLUE', 'YELLOW']
    goal_state = {
        'm1': 0, 'm2': 0, 'm3': 0, 'm4': 1,
        'l1': 0, 'l2': 0, 'l3': 0, 'l4': 1, 'l5': 1,
        'r1': 0, 'r2': 0, 'r3': 0, 'r4': 1, 'r5': 1,
        'f1': 0, 'f2': 0, 'f3': 0
    }

    for key in goal_state:
        goal_state[key] = colors[goal_state[key]]
    plan = Solution.solve(goal_state)
    print(plan[::-1])