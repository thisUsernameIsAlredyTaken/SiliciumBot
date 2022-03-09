from .bot import BotModule
from .calculator import CalculatorModule
from .deprecated import DeprecatedModule
from .info import InfoModule
from .jokes import JokesModule
from .shiki import ShikiModule
from .music import MusicModule
from .anek import AnekModule
from .balaboba import BalabobaModule
from .readycheck import ReadyCheckModule

cogs = [
    JokesModule,
    CalculatorModule,
    BotModule,
    ShikiModule,
    InfoModule,
    DeprecatedModule,
    MusicModule,
    AnekModule,
    BalabobaModule,
    ReadyCheckModule
]