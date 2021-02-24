from dataclasses import dataclass
from itertools import combinations
from typing import List, Tuple, Optional, Set

import networkx as nx
from networkx import neighbors


@dataclass
class Node:
    id: int
    name: str
    type: str
    status: str

    def __hash__(self):
        return self.id


@dataclass
class Edge:
    id: int
    name: str
    n1: str
    n2: str
    length: Optional[int]
    length_vel_calc: Optional[int]
    status: Optional[str]

    def __hash__(self):
        return self.id

@dataclass
class SimulationResult:
    nodes_to_close: List[Node]
    edges: List[Edge]


def is_open_locking_device(node: Node):
    return node.type == 'locking_device' and node.status == 'OPEN'


class EmergencySimulationAlgorithm2(object):
    """
    Принцип работы заключается в поиске ближайшей запорной арматуры для
    изолирования участка от источника водоснабжения.

    Моделирование аварийных ситуаций предназначено для анализа изменений
    вследствие отключения задвижек или участков сети. В результате задачи
    определяются объекты, попавшие под отключение. При этом производится
    расчет объемов воды, которые возможно придется сливать из трубопроводов
    водопроводной сети. Результаты расчета отображаются на карте в виде
    тематической раскраски отключенных участков и потребителей и выводятся
    в отчет.

    """
    def __init__(
            self,
            nodes: List[Tuple[str, Node]],
            edges: List[Tuple[str, str, Edge]]
    ):
        self.nodes = nodes
        self.edges = edges

        self.G = nx.Graph()
        self.G.add_nodes_from(self.nodes)
        self.G.add_edges_from(self.edges)

        self.nearest_locking_devices: Set[Node] = set()
        self.pipes: List[Edge] = []

        self.sources = self.source_nodes()

        self.processed_nodes: Set[str] = set()

    def locking_device_to_close(self) -> Set[Node]:
        locking_devices_names = set(map(lambda d: d.name, self.nearest_locking_devices))
        source_nodes_name = set(map(lambda n: n.name, self.sources))

        to_close_names: Set[str] = set()

        for exclude_names in combinations(locking_devices_names, len(locking_devices_names)-1):
            locking_device_name = list(locking_devices_names.difference(set(exclude_names)))[0]

            graph_view = nx.subgraph_view(self.G, nx.classes.filters.hide_nodes(exclude_names))
            components = nx.connected_components(graph_view)
            for component in components:
                if locking_device_name in component:
                    if len(component & source_nodes_name) > 0:
                        to_close_names.update({locking_device_name})
                        # Выходим из цикла поиска задвижки в подсетях, т. к. в этом подграфе
                        # задвижка есть и есть источинк, а значит задвижку нужно закрыть.
                        break
                    # Выходим из цикла поиска задвижки в подсетях, т. к. в этом подграфе
                    # задвижка есть, а источника нет.
                    break

        return set(filter(lambda n: n.name in to_close_names, self.nearest_locking_devices))

    def source_nodes(self):
        return list(map(lambda d: Node(**d), [y for x, y in self.G.nodes(data=True) if y['type'] == 'source_constant']))

    def simulate(self, edges: List[Edge]):

        # Find nearest locking devices.
        for edge in edges:
            self.process_node(edge.n1)
            self.process_node(edge.n2)

    def process_node(self, node_name: str):
        self.processed_nodes.add(node_name)
        node: Node = Node(**self.G.nodes[node_name])
        if is_open_locking_device(node):
            self.nearest_locking_devices.add(node)
            return

        neighbor_nodes_names = neighbors(self.G, node_name)
        for name in neighbor_nodes_names:
            if name in self.processed_nodes:
                continue
            edge = Edge(**self.G.edges[(node_name, name)])
            self.pipes.append(edge)
            self.process_node(name)
