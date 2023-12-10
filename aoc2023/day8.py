class Part1:
    NODE_KEY='AAA'
    MATCH_LAMBDA=lambda v: v == 'ZZZ'

    @classmethod
    def total_steps(cls, instructions, nodes, node_key=NODE_KEY, match_lambda=MATCH_LAMBDA):
        ''' 
        get total steps from walking instructions and nodes 
        using node_key as initial starting node
        and end when node name matches with match_lambda
        '''
        total_steps=0
    
        while True:
            for i in range(len(instructions)):
                total_steps += 1
                instruction = instructions[i]
                current_node = nodes[node_key]

                if instruction == 'L':
                    node_key = current_node[0]
                else:
                    node_key = current_node[1]

                if match_lambda(node_key):
                    return total_steps

class Part2:
    MATCH_LAMBDA=lambda v: v.endswith('Z')

    @classmethod
    def get_node_keys(cls, nodes):
        return [x for x in nodes.keys() if x.endswith('A')]

    @classmethod
    def total_steps(cls, instructions, nodes, node_keys, match_lambda=MATCH_LAMBDA):
        min_steps_per_node_key = [Part1.total_steps(instructions, nodes, node_key, match_lambda) for node_key in node_keys] 

        import math
        return math.lcm(*min_steps_per_node_key)
