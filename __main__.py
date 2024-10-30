from saccr.netting_set import NettingSet
from saccr.position import Currency, OptionType, IRPosition
import pandas as pd


if __name__ == "__main__":

    trade_data = pd.read_csv("Input_1_IR.csv")
    netting_set = NettingSet(collateral=0)