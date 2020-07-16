class Army:
    def __init__(self, name, city, target = None):
        self.name = name
        self.target = target
        self.city = city
        self.power = 0
        self.fighting = False
    
    def __str__(self):
        return self.name + " " + self.city

def diplomacy_start(s):
    info = s.split()
    if info[2] == "Support":
        army = Army(info[0], info[1], info[3])
    elif info [2] == "Move":
        army = Army(info[0], info[3])
    else:
        army = Army(info[0], info[1])
    return army
    
    
def diplomacy_action(armies, battlefield):
    for i in range(len(armies)):
        army = armies[i]
        if army.fighting:
            continue
        battle = [army]
        j = i + 1
        while j < len(armies):
            if armies[j].city == army.city:
                battle.append(armies[j])
                army.fighting = True
                armies[j].fighting = True
            j += 1
        if len(battle) > 1:
            battlefield.append(battle)


def diplomacy_support(armies, results):
    for army in armies:
        if (not army.fighting):
            results.append(army.name + " " + army.city)
            if not not army.target:
                for army2 in armies:
                    if army2.name == army.target:
                        army2.power += 1
                        break


def diplomacy_outcome(battlefield):
    outcome = []
    for battle in battlefield:
        max_power = 0
        while len(battle) > 1:
            for army in battle:
                if army.power <= max_power:
                    result = army.name + " [dead]"
                    outcome.append(result)
                    battle.remove(army)
            max_power += 1
        result = battle[0].name + " " + battle[0].city
        outcome.append(result)
    return outcome
    

def diplomacy_solve(r, w):
    """
    r a reader
    w a writer
    """
    armies = []
    for s in r:
        armies.append(diplomacy_start(s))
    battlefield = []
    diplomacy_action(armies, battlefield)
    results = []
    diplomacy_support(armies, results)
    results.extend(diplomacy_outcome(battlefield))
    for army in sorted(results):
        w.write(army + "\n")
