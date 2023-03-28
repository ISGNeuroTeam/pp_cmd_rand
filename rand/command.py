import numpy as np
import pandas as pd
from otlang.sdk.syntax import Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax


class RandCommand(BaseCommand):
    syntax = Syntax(
        [
            Positional("column", required=True, otl_type=OTLType.TEXT),
            Positional("count", required=False, otl_type=OTLType.INTEGER),
        ],
    )
    idempotent = False

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.log_progress('Start range command')
        column = self.get_arg("column").value
        count = self.get_arg("count").value or 10

        if df.empty:
            df[column] = np.random.randint(1000, size=(count,))
        else:
            df[column] = np.random.randint(1000, size=df.shape[0])
        return df
