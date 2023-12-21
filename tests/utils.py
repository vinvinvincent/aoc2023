from testplan.testing.multitest.result import Result

TIMEOUT_SEC = 5


def check_eq_or_log(result: Result, actual, expected, description=None):
    '''check actual == expected or log only if actual is None'''
    if expected is not None:
        result.eq(actual, expected, description)
    else:
        result.log(actual, description)
