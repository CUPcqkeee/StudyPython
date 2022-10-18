# Говно код снизу


game_field = [["_", "_", "_", ],
              ["_", "_", "_", ],
              ["_", "_", "_", ]
              ]


def render_field():
    step = 0
    for i in game_field:
        print(i)
        step += 1
        if step >= 3:
            print()