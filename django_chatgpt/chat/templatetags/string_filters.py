from django import template

register = template.Library()


@register.filter(name='substring')
def substring(value, arg):
    """
    Returns a substring of 'value' from start to end indices provided in 'arg'.
    'arg' should be in the format "start:end".
    If 'end' is omitted, returns the substring from 'start' to the end of the string.
    """
    try:
        start, end = map(int, arg.split(':'))
        return value[start:end]
    except ValueError:  # Handles cases where 'arg' is not in the expected format
        return value
