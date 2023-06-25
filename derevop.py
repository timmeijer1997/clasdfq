class PriestMixin(object):
    def heal_one(target):
        # do something
        pass
    
    def heal_many(targets):
        for target in targets:
            self.heal_one(target)

class WarriorMixin(object):
    def kick_ass(target):
        # kick ass
        pass

class KnightMixin(object):
    def protect(target):
        # protect target
        pass

class Patrol(object):
    def __init__(self, id, name, containments):
        self.id = id
        self.name = name
        self.unit_classes = [type(cont['name'], (*cont['mixins']), {}) for cont in containments]
        self.containment = [unit_class() for unit_class in unit_classes]

Patrol('SuicideSquad', 'Suicide Squad', [
    {'name': 'VasyaTheKnight', 'mixins': [PriestMixin, KnightMixin]},
    {'name': 'YouraMotherFucker', 'mixins': [WarriorMixin]}
    ])
