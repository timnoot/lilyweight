# lilyweight

[![discord](https://img.shields.io/discord/670733991082459146?logo=discord&style=for-the-badge)](https://discord.gg/kXfBmF4)
[![license](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![pypi](https://img.shields.io/pypi/v/lilyweight?style=for-the-badge)](https://pypi.org/project/lilyweight/)

Hypixel SkyBlock Weight Calculator

## Information

This is a reimplementation of https://github.com/Antonio32A/lilyweight in Python.
Which is a reimplementation of https://github.com/LappySheep/hypixel-skyblock-weight

Written without any external libraries other than `aiohttp` which is used to fetch data from the Hypixel API.

This requires a Hypixel API key. You may obtain one by logging onto `hypixel.net` with your Minecraft client and typing
/api new.

## Credits
- [LappySheep](https://github.com/LappySheep/) - Original author of the calculator
- [Desco](https://github.com/Desco1) - Ported the calculator to JavaScript.
- [Antonio32A](https://github.com/Antonio32A) - Ported the calculator to JavaScript.
- [timnoot](https://github.com/timnoot) - Ported the calculator to Python.

## Usage

```py
import asyncio

from lilyweight import LilyWeight

# replace HYPIXEL_API_KEY with your Hypixel API key
lily = LilyWeight("HYPIXEL_API_KEY")


async def main():
    # using a UUID
    print(await lily.get_weight("e710ff36fe334c0e8401bda9d24fa121"))

    # using a username
    print(await lily.get_weight_from_name("timnoot"))

    # functions for if you wish to see a certain profile instead of the most recently used profile
    print(await lily.get_weight_from_name("MooshiMochi", "Orange"))
    print(await lily.get_weight("0ce87d5afa5f4619ae78872d9c5e07fe", "Mango"))

    # get raw weight from raw data, read the JSDoc for more information
    # this does not return the uuid and username fields but it does not make any requests
    print(LilyWeight.get_weight_raw(
        {  # Skill levels in a dict
            'enchanting': 60,
            'taming': 60,
            'alchemy': 60,
            'mining': 60,
            'farming': 60,
            'foraging': 52,
            'combat': 60,
            'fishing': 60
        },
        {  # Skill experience in a dict
            'enchanting': 842351020.815073,
            'taming': 2884548541.3704095,
            'alchemy': 125648244.46351068,
            'mining': 510669860.4613964,
            'farming': 200263881.0307403,
            'foraging': 68274086.12834656,
            'combat': 3590591634.1474257,
            'fishing': 227814154.47671163
        },
        {  # Dungeon completions in a dict
            '0': 22.0, '1': 138.0, '2': 967.0, '3': 100.0, '4': 172.0, '5': 323.0, '6': 578.0, '7': 1201.0
        },
        {  # Master dungeon completions in a dict
            '1': 907.0, '2': 40.0, '3': 1100.0, '4': 873.0, '5': 2729.0, '6': 1508.0, '7': 974.0
        },
        1316600722.1128976,  # Total experience in the catacombs
        **{  # Slayer experience as kwargs
            'zombie': 34954055, 'spider': 64968075, 'wolf': 1526995, 'enderman': 3575580, 'blaze': 259305
        }

    ))


asyncio.run(main())
```

Example output of one of the functions, in JSON:
```json
{
    "total": 14439.880600696824,
    "skill": {
        "base": 10346.795817290036,
        "overflow": 173.30267908613297
    },
    "catacombs": {
        "completion": {
            "base": 1226.2725420124711,
            "master": 532.7492424907152
        },
        "experience": 1057.0997512507508
    },
    "slayer": 1103.6605685667157
}
```

## API
If you aren't using Python or JavaScript and you need an API, take a look at [lilyweight-worker](https://lilydocs.antonio32a.com/).
