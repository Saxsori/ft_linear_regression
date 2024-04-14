
def normalize_xy(x, y):
	x = (x - x.min()) / (x.max() - x.min())
	y = (y - y.min()) / (y.max() - y.min())
	return x, y


def denormalize_xy(x, y, original_x, original_y):
    x = x * (max(original_x) - min(original_x)) + min(original_x)
    y = y * (max(original_y) - min(original_y)) + min(original_y)
    return x, y


def normalize_value(x:float, original_x:list) -> float:
    x = (x - min(original_x)) / (max(original_x) - min(original_x))
    return x


def denormalize_value(x, original_x):
    x = x * (max(original_x) - min(original_x)) + min(original_x)
    return x