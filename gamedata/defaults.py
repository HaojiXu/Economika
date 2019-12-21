default_start_template = {
        "game_data": {
            "global": {
                "currencies": [
                    {
                        "name": "Silver",
                        "is_primitive": True,
                        "_id": "Ag0"
                    },
                    {
                        "name": "Gold",
                        "is_primitive": True,
                        "_id": "Au1"
                    }
                ],
            },
            "player": {
                "currencies": [
                    {
                        "_id": "Ag0",
                        "is_legal": True,
                    },
                    {
                        "_id": "Au1",
                        "is_legal": True,
                    }
                ],
                "treasuries": [
                    {
                        "name": "Palace Treasury",
                        "is_palace": True,
                    }
                ]

            }
        },
        "config": {
            "tick_interval_ms": 500 # 0.5s/Tick
        }
    }