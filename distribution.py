from decimal import Decimal, ROUND_HALF_EVEN


class Project:
    def __init__(self, index, investment, profit):
        self.index = index
        self.investment = investment
        self.profit = profit


class Distribution:
    def __init__(self):
        self.values = {}
        self.profit = decimalize(0.0)

    def distribute(self, project, balance):
        self.values[project.index] = 1 if balance >= project.investment else balance / project.investment
        self.profit += project.profit * self.values[project.index]

    def __str__(self):
        return '{}\n{}'.format('  '.join(
            map(lambda item: '{}: {}'.format(item[0], item[1]), self.values.items())
        ), format(self.profit, '.4f'))


def distribute(investments, profits, funds):
    count = len(investments)
    projects = [Project(i, investments[i], profits[i]) for i in range(count)]
    projects.sort(key=lambda project: project.profit / project.investment, reverse=True)
    balance = funds
    distribution = Distribution()
    i = 0
    while balance > 0 and i < count:
        distribution.distribute(projects[i], balance)
        balance -= projects[i].investment
        i += 1
    return distribution


def decimalize(num, tolerance='0.001', rounding=ROUND_HALF_EVEN):
    return Decimal(num).quantize(Decimal(tolerance), rounding=rounding)


print(distribute([decimalize(1), decimalize(2), decimalize(2), decimalize(0.8)],
                 [decimalize(1.5), decimalize(3.5), decimalize(3.2), decimalize(1.2)],
                 decimalize(7.5)))
