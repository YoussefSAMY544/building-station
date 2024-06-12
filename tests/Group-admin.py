import matplotlib.pyplot as plt
import networkx as nx

# Diagram 1: System Architecture Overview
G1 = nx.DiGraph()
G1.add_edges_from([
    ("Users", "Group Management System", {'label': 'Super Admin'}),
    ("Users", "Group Management System", {'label': 'Regular User'}),
    ("Group Management System", "Create Group"),
    ("Group Management System", "Edit Group"),
    ("Group Management System", "Delete Group"),
    ("Group Management System", "View Group"),
    ("View Group", "Users"),
    ("Create Group", "Users"),
    ("Edit Group", "Users"),
    ("Delete Group", "Users")
])

pos1 = nx.spring_layout(G1)
labels1 = nx.get_edge_attributes(G1, 'label')

plt.figure(figsize=(10, 8))
nx.draw(G1, pos1, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)
nx.draw_networkx_edge_labels(G1, pos1, edge_labels=labels1, font_color='red')
plt.title("System Architecture Overview")
plt.savefig("/mnt/data/System_Architecture_Overview.png")
plt.clf()

# Diagram 2: User Permissions Flow
G2 = nx.DiGraph()
G2.add_edges_from([
    ("Start", "Are you a Super Admin?"),
    ("Are you a Super Admin?", "Create Group", {'label': 'Yes'}),
    ("Are you a Super Admin?", "Edit Group", {'label': 'Yes'}),
    ("Are you a Super Admin?", "Delete Group", {'label': 'Yes'}),
    ("Are you a Super Admin?", "View Group", {'label': 'Yes'}),
    ("Are you a Super Admin?", "View Group Only", {'label': 'No'}),
    ("Create Group", "End"),
    ("Edit Group", "End"),
    ("Delete Group", "End"),
    ("View Group", "End"),
    ("View Group Only", "End")


])

pos2 = nx.spring_layout(G2)
labels2 = nx.get_edge_attributes(G2, 'label')

plt.figure(figsize=(10, 8))
nx.draw(G2, pos2, with_labels=True, node_size=3000, node_color="lightgreen", font_size=10, font_weight="bold", arrows=True)
nx.draw_networkx_edge_labels(G2, pos2, edge_labels=labels2, font_color='blue')
plt.title("User Permissions Flow")
plt.savefig("/mnt/data/User_Permissions_Flow.png")
plt.clf()

# Diagram 3: Group Management Process
G3 = nx.DiGraph()
G3.add_edges_from([
    ("Start", "Super Admin: Access Groups Tab"),
    ("Super Admin: Access Groups Tab", "Create/Edit/Delete Group"),
    ("Create/Edit/Delete Group", "Fill in Group Details"),
    ("Fill in Group Details", "Add Users"),
    ("Add Users", "Assign Permissions"),
    ("Assign Permissions", "Save Group"),
    ("Save Group", "Group Created/Edited/Deleted")
])

pos3 = nx.spring_layout(G3)

plt.figure(figsize=(10, 8))
nx.draw(G3, pos3, with_labels=True, node_size=3000, node_color="lightcoral", font_size=10, font_weight="bold", arrows=True)
plt.title("Group Management Process")
plt.savefig("/mnt/data/Group_Management_Process.png")
plt.clf()

# Diagram 4: Use Case Diagram
G4 = nx.DiGraph()
G4.add_edges_from([
    ("Super Admin", "Create Group"),
    ("Super Admin", "Edit Group"),
    ("Super Admin", "Delete Group"),
    ("Super Admin", "View Group"),
    ("Regular User", "View Group")
])

pos4 = nx.spring_layout(G4)

plt.figure(figsize=(10, 8))
nx.draw(G4, pos4, with_labels=True, node_size=3000, node_color="lightyellow", font_size=10, font_weight="bold", arrows=False)
plt.title("Use Case Diagram")
plt.savefig("/mnt/data/Use_Case_Diagram.png")
plt.clf()

# Diagram 5: Sequence Diagram (simplified as flow)
G5 = nx.DiGraph()
G5.add_edges_from([
    ("Super Admin", "Group Management System", {'label': 'Create/Edit/Delete Group'}),
    ("Group Management System", "Super Admin", {'label': 'Confirm Action'}),
    ("Regular User", "Group Management System", {'label': 'View Group'}),
    ("Group Management System", "Regular User", {'label': 'Display Group Details'})
])

pos5 = nx.spring_layout(G5)
labels5 = nx.get_edge_attributes(G5, 'label')

plt.figure(figsize=(10, 8))
nx.draw(G5, pos5, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)
nx.draw_networkx_edge_labels(G5, pos5, edge_labels=labels5, font_color='purple')
plt.title("Sequence Diagram")
plt.savefig("/mnt/data/Sequence_Diagram.png")
plt.clf()

# Diagram 6: Advantages Diagram
G6 = nx.DiGraph()
G6.add_edges_from([
    ("Advantages", "Security"),
    ("Advantages", "Centralized Control"),
    ("Advantages", "Role Clarity"),
    ("Advantages", "Efficiency"),
    ("Advantages", "Accountability")
])

pos6 = nx.spring_layout(G6)

plt.figure(figsize=(10, 8))
nx.draw(G6, pos6, with_labels=True, node_size=3000, node_color="lightpink", font_size=10, font_weight="bold", arrows=False)
plt.title("Advantages Diagram")
plt.savefig("/mnt/data/Advantages_Diagram.png")
plt.clf()

# Paths to the saved images
image_paths = [
    "/mnt/data/System_Architecture_Overview.png",
    "/mnt/data/User_Permissions_Flow.png",
    "/mnt/data/Group_Management_Process.png",
    "/mnt/data/Use_Case_Diagram.png",
    "/mnt/data/Sequence_Diagram.png",
    "/mnt/data/Advantages_Diagram.png"
]

image_paths
