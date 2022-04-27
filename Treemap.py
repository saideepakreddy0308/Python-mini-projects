#Displays hierarchical data in such a way that each branch of tree receives a rectangle which is filled
# with smaller rectangles as sub-branches.
import plotly.graph_objects  as go
fig = go.Figure(go.Treemap(
    labels = ["A","B","C","D","E","F","G","H","I"],
    parents = ["","A","A","C","C","A", "A","G","A"]
))

fig.show()

