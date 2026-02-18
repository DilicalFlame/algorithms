from ._registry import register

@register
def mean(data):
    return sum(data) / len(data)
