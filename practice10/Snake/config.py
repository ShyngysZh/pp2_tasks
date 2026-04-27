import json

def load_settings():
    try:
        with open("settings.json", "r") as f:
            return json.load(f)
    except:
        return {
            "snake_color": [0, 100, 0],
            "frame_color": [0, 255, 204],
            "grid_color": [200, 255, 255],
            "sound": True
        }


settings = load_settings()

SIZE_BLOCK = 20
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1

FRAME_COLOR = tuple(settings["frame_color"])
WHITE = (255, 255, 255)
BLUE = tuple(settings["grid_color"])

SNAKE_COLOR = tuple(settings["snake_color"])
FOOD_COLOR = (255, 0, 0)
BONUS_COLOR = (255, 0, 255)

HEADER_COLOR = (0, 204, 150)
FRAME_COLOR = (0, 255, 204)