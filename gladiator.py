import random


class Gladiator:
    """ A game where Gladiators fight to the death with, health, rage
damage_low, and damage_high"""
    def __init__(self, name, health, rage, ld, hd):
        self.name = name
        self.health = health
        self.rage = rage
        self.damage_low = ld
        self.damage_high = hd

    def attack(self, other):
        hits = random.randint(self.damage_low, self.damage_high)
        if self.rage > random.randint(0, 100):
            hits *= 2
            self.rage = 0
        else:
            self.rage += 15
        # deliver the blow
        other.health -= hits

    def heal(self):
        if self.health > 0 and self.health <= 95:
            if self.rage >= 10:
                self.health += 5
                self.rage -= 10

    def is_dead(self):
        if self.health < 1:
            return True

        else:
            return False

    def __str__(self):
        return '({0}, {1}, {2}, {3}, {4})'.format(self.name, self.health,
                                                  self.rage, self.damage_low,
                                                  self.damage_high)

    def __repr__(self):
        return 'Gladiator({0}, {1}, {2}, {3}, {4})'.format(self.name,
                                                           self.health,
                                                           self.rage,
                                                           self.damage_low,
                                                           self.damage_high)
