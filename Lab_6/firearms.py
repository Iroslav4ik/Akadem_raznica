class Firearm:
    def __init__(self, ammo_capacity, fire_rate, effective_range):
        self.ammo_capacity = ammo_capacity
        self.fire_rate = fire_rate
        self.effective_range = effective_range

    def time_to_empty_magazine(self):
        """Время (в секундах) до опустошения магазина"""
        shots_per_second = self.fire_rate / 60.0
        return self.ammo_capacity / shots_per_second

    def ratio_fire_rate_to_range(self):
        """Соотношение скорострельности к дальности стрельбы"""
        return self.fire_rate / self.effective_range

class AssaultRifle(Firearm):
    def __init__(self, ammo_capacity, fire_rate, effective_range, burst_mode):
        super().__init__(ammo_capacity, fire_rate, effective_range)
        self.burst_mode = burst_mode

    def ratio_fire_rate_to_range(self):
        """Увеличенное соотношение для режимов burst/auto"""
        base_ratio = super().ratio_fire_rate_to_range()
        if self.burst_mode == 'auto':
            return base_ratio * 1.5
        elif self.burst_mode == 'burst':
            return base_ratio * 1.2
        return base_ratio

class SniperRifle(Firearm):
    def __init__(self, ammo_capacity, fire_rate, effective_range, scope_magnification):
        super().__init__(ammo_capacity, fire_rate, effective_range)
        self.scope_magnification = scope_magnification

    def ratio_fire_rate_to_range(self):
        """Уменьшенное соотношение для точной стрельбы"""
        return super().ratio_fire_rate_to_range() * 0.7


ak47 = AssaultRifle(
    ammo_capacity=30,
    fire_rate=600,
    effective_range=500,
    burst_mode='auto'
)

awp = SniperRifle(
    ammo_capacity=10,
    fire_rate=30,
    effective_range=1500,
    scope_magnification=10
)

print(f"AK-47 опустеет за: {ak47.time_to_empty_magazine():.1f} сек")
print(f"AK-47 соотношение: {ak47.ratio_fire_rate_to_range():.4f}")
print(f"AWP опустеет за: {awp.time_to_empty_magazine():.1f} сек")
print(f"AWP соотношение: {awp.ratio_fire_rate_to_range():.4f}")