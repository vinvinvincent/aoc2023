from enum import Enum
from typing import List
from data.day19 import Workflow, Parts


class ResultLabel(Enum):
    ACCEPT = 'A'
    REJECT = 'R'


def evaulate_next_workflow(
    parts: Parts,
    workflows: dict[Workflow],
    workflow_name: str = 'in',
):
    expr = workflows.get(workflow_name).expressions_eval_str
    return eval(expr, parts.xmas)


def check_parts_accepted(
    parts: Parts,
    workflows: dict[Workflow],
    workflow_name: str = 'in',
    verbose=False,
):
    while workflow_name not in [
        ResultLabel.ACCEPT.value,
        ResultLabel.REJECT.value,
    ]:
        expr = workflows.get(workflow_name).expressions_eval_str
        if verbose:
            print(workflow_name, '\t\t', expr)
        workflow_name = eval(expr, parts.xmas)

    return workflow_name == ResultLabel.ACCEPT.value


def get_sum_of_all_expected_parts(
    parts_list: List[Parts],
    workflows: dict[Workflow],
    workflow_name: str = 'in',
    verbose=False,
):
    sum = 0
    for parts in parts_list:
        if check_parts_accepted(parts, workflows, workflow_name, verbose):
            sum += parts.xmas['x'] + parts.xmas['m'] + parts.xmas['a'] + parts.xmas['s']
    return sum
