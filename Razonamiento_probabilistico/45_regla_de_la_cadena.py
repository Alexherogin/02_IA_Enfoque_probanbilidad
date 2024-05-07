


class BayesianNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name, parents, distribution):
        self.nodes[name] = {'parents': parents, 'distribution': distribution}

    def calculate_probability(self, node, configuration):
        if not self.nodes[node]['parents']:
            return self.nodes[node]['distribution'][()]
        parents = tuple(configuration[p] for p in self.nodes[node]['parents'])
        return self.nodes[node]['distribution'][parents]


class ChainRule:
    def __init__(self, bayesian_network):
        self.bayesian_network = bayesian_network

    def calculate_conditional_probability(self, evidence, variable):
        probability = 1.0
        for node in evidence:
            probability *= self.bayesian_network.calculate_probability(node, evidence)
        probability *= self.bayesian_network.calculate_probability(variable, evidence)
        return probability


# Example Usage
bayesian_network = BayesianNetwork()
bayesian_network.add_node('X', [], {(): 0.3})
bayesian_network.add_node('Y', ['X'], {(True,): 0.8, (False,): 0.2})

chain_rule = ChainRule(bayesian_network)
probability = chain_rule.calculate_conditional_probability({'X': True}, 'Y')
print("Probability of Y given X=True:", probability)
