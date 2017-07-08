# GameParams.data unpack
Set of tools and classes that will help you in your work with GameParams.data of WorldOfWarships game.

## Command-line usage
usage: game_params.py [-h] --json [--by-id] [--type-filter TYPE_FILTER] FILE

positional arguments:
  FILE                  path to GameParams.data

optional arguments:
  -h, --help            show this help message and exit
  --json                show data as json
  --by-id               show data by id
  --type-filter TYPE_FILTER
                        show only values of given type (see item.typeinfo.type
                        in json)

## Module usage
```
from GameParams import GameParams
gp = GameParams()
gp.load(<file_path>)

print gp.data
print gp.dataById
```

For questions: shalal545@gmail.com and skype:shalal147258.
