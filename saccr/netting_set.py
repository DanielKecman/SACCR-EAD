from saccr.position import IRPosition

ALPHA = 1.4

class NettingSet:
    def __init__(self,
                 collateral: float,
                 positions: dict[str, IRPosition] = {},
                 ):
        self._collateral = collateral
        self._positions = positions

    def _add_position(self,
                      position_name: str,
                      position: IRPosition):
        self._positions[position_name] = position

    def _calculate_total_market_value(self):
        total_value = 0
        for position in self._positions.values():
            total_value = total_value + position._market_value

        return total_value

    def _calculate_replacement_cost(self):
        #Much more complicated for margined trades
        return max(self._calculate_total_market_value() - self._collateral, 0)
'''
    def _calculate_EAD(self):
        return ALPHA * (self._calculate_replacement_cost() + self._calculate_PFE())

    def _calculate_multiplier(self):
'''



