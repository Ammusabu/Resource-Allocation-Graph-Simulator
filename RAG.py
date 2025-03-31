
import networkx as nx
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import ipywidgets as widgets

class ResourceAllocationSimulator:
    def __init__(self):
        self.reset_simulator()

    def reset_simulator(self):
        self.graph = nx.DiGraph()
        self.process_count = 0
        self.resource_count = 0
        self.allocations = []
        self.requests = []

    def add_process(self):
        self.process_count += 1
        pid = f"P{self.process_count}"
        self.graph.add_node(pid, type='process', color='#66b3ff', shape='s')
        return pid

    def add_resource(self):
        self.resource_count += 1
        rid = f"R{self.resource_count}"
        self.graph.add_node(rid, type='resource', color='#99ff99', shape='d')
        return rid

    def auto_connect(self):
        messages = []
        # Auto-allocate last resource to last process
        if self.resource_count >= 1 and self.process_count >= 1:
            rid = f"R{self.resource_count}"
            pid = f"P{self.process_count}"
            self.graph.add_edge(rid, pid, color='black', style='solid')
            self.allocations.append((rid, pid))
            messages.append(f"Allocated {rid} → {pid}")

        # Create request from previous process to new resource
        if self.resource_count >= 1 and self.process_count >= 2:
            rid = f"R{self.resource_count}"
            pid = f"P{self.process_count-1}"
            self.graph.add_edge(pid, rid, color='red', style='dashed')
            self.requests.append((pid, rid))
            messages.append(f"Requested {pid} → {rid}")

        return messages

    def detect_deadlock(self):
        try:
            cycle = nx.find_cycle(self.graph, orientation='original')
            return True, cycle
        except nx.NetworkXNoCycle:
            return False, None

    def draw_graph(self):
        plt.figure(figsize=(10, 6))

        # Create layout
        pos = {}
        process_nodes = [f"P{i+1}" for i in range(self.process_count)]
        resource_nodes = [f"R{i+1}" for i in range(self.resource_count)]

        # Position processes on left, resources on right
        for i, node in enumerate(process_nodes):
            pos[node] = (0, -i)

        for i, node in enumerate(resource_nodes):
            pos[node] = (2, -i)

        # Draw nodes
        node_colors = []
        for node in self.graph.nodes():
            node_colors.append(self.graph.nodes[node]['color'])

        nx.draw_networkx_nodes(
            self.graph, pos,
            node_color=node_colors,
            node_size=2500,
            edgecolors='black'
        )

        # Draw labels
        labels = {node: node for node in self.graph.nodes()}
        nx.draw_networkx_labels(self.graph, pos, labels=labels, font_size=12)

        # Draw edges
        solid_edges = [(u, v) for u, v, d in self.graph.edges(data=True) if d.get('style') == 'solid']
        dashed_edges = [(u, v) for u, v, d in self.graph.edges(data=True) if d.get('style') == 'dashed']

        nx.draw_networkx_edges(
            self.graph, pos,
            edgelist=solid_edges,
            edge_color='black',
            arrows=True,
            arrowstyle='-|>',
            arrowsize=20,
            width=2
        )

        nx.draw_networkx_edges(
            self.graph, pos,
            edgelist=dashed_edges,
            edge_color='red',
            style='dashed',
            arrows=True,
            arrowstyle='-|>',
            arrowsize=20,
            width=2
        )

        # Add legend
        plt.plot([], [], color='black', linestyle='-', label='Allocation')
        plt.plot([], [], color='red', linestyle='--', label='Request')
        plt.legend(loc='upper right')

        plt.title("Resource Allocation Graph")
        plt.axis('off')
        plt.tight_layout()
        plt.show()

        # Check for deadlock
        deadlock, cycle = self.detect_deadlock()
        if deadlock:
            cycle_path = " → ".join([str(node[0]) for node in cycle] + [str(cycle[0][0])])
            print(f"⚠️ DEADLOCK DETECTED! Cycle: {cycle_path}")
        else:
            print("✅ System is deadlock-free")

def create_simulator_ui():
    simulator = ResourceAllocationSimulator()

    # Create buttons
    add_process_btn = widgets.Button(
        description="Add Process",
        button_style='primary',
        icon='plus'
    )

    add_resource_btn = widgets.Button(
        description="Add Resource",
        button_style='success',
        icon='plus'
    )

    clear_btn = widgets.Button(
        description="Clear All",
        button_style='danger',
        icon='trash'
    )

    output = widgets.Output()

    # Button click handlers
    def on_add_process(btn):
        with output:
            clear_output()
            pid = simulator.add_process()
            print(f"Added process: {pid}")
            messages = simulator.auto_connect()
            for msg in messages:
                print(msg)
            simulator.draw_graph()

    def on_add_resource(btn):
        with output:
            clear_output()
            rid = simulator.add_resource()
            print(f"Added resource: {rid}")
            messages = simulator.auto_connect()
            for msg in messages:
                print(msg)
            simulator.draw_graph()

    def on_clear(btn):
        with output:
            clear_output()
            simulator.reset_simulator()
            print("Simulator reset - all processes and resources cleared")
            simulator.draw_graph()

    # Assign handlers
    add_process_btn.on_click(on_add_process)
    add_resource_btn.on_click(on_add_resource)
    clear_btn.on_click(on_clear)

    # Display UI
    display(widgets.HBox([add_process_btn, add_resource_btn, clear_btn]))
    display(output)

    # Initial empty graph
    with output:
        simulator.draw_graph()

# Run the simulator
print("Resource Allocation Graph Simulator")
print("Click buttons to add processes/resources and see automatic allocations!")
create_simulator_ui()
