# # from splaytree import SplayTree
# # import random

# # def generate_custom_list(n, m, c, x):
# #     count_x = int(m * c / 100)
# #     result = [x] * count_x
# #     result += [random.randint(1, n) for _ in range(m - count_x)]
# #     random.shuffle(result)
# #     return result


# # # Initialize the Splay Tree and insert elements
# # tree = SplayTree()
# # n = 20
# # for i in range(n):
# #     tree.insert(i)

# # c = 100
# # x = 10
# # m = 100000

# # # Generate list
# # arr = generate_custom_list(n, m, c, x)

# # # Reset search counter before testing
# # tree.search_counter = 0
# # for i in arr:
# #     if i == x:
# #         tree.search(x)

# # print(f"Search counter for x per query:{tree.search_counter/((c/100.0)*m)}")
      
# from splaytree import SplayTree
# import random
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np

# def generate_custom_list(n, m, c, x):
#     count_x = int(m * c / 100)
#     result = [x] * count_x
#     result += [random.randint(1, n) for _ in range(m - count_x)]
#     random.shuffle(result)
#     return result

# def run_simulation(n, x, c, m):
#     # Initialize the Splay Tree and insert elements
#     tree = SplayTree()
#     for i in range(n):
#         tree.insert(i)
    
#     # Generate the list
#     arr = generate_custom_list(n, m, c, x)

#     # Reset search counter before testing
#     tree.search_counter = 0
#     for i in arr:
#         if i == x:
#             tree.search(x)
    
#     # Return the search counter per query
#     return tree.search_counter / ((c / 100.0) * m)

# # Parameters
# n = 100
# x = 20
# c_values = range(1, 101)  # c from 1 to 100
# m_values = [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

# # Prepare data for plotting
# c_plot, m_plot, search_counter_plot = [], [], []

# # Run the simulations for all values of c and m
# for c in c_values:
#     for m in m_values:
#         search_counter_per_query = run_simulation(n, x, c, m)
#         c_plot.append(c)
#         m_plot.append(m)
#         search_counter_plot.append(search_counter_per_query)

# # Create 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Scatter plot in 3D
# ax.scatter(c_plot, m_plot, search_counter_plot, c='b', marker='o')
# ax.set_xlabel('Percentage of x (c)')
# ax.set_ylabel('List Size (m)')
# ax.set_zlabel('Search Counter per Query')

# plt.title("3D plot of Search Counter per Query vs. c and m")
# plt.show()

from splaytree import SplayTree
import plotly.graph_objects as go
import random
from tqdm import tqdm

# Function to generate the custom list
def generate_custom_list(n, m, c, x):
    count_x = int(m * c / 100)
    result = [x] * count_x
    result += [random.randint(1, n) for _ in range(m - count_x)]
    random.shuffle(result)
    return result

# Initialize parameters
n = 100
x = 20
m_values = [1000, 5000, 10000, 50000, 100000, 500000, 5000000]  # m from 1000 to 5000000
c_values = list(range(1, 101))  # c from 1 to 100

search_counter_results = []

# Loop through values of m and c
for m in tqdm(m_values):
    search_counter_per_c = []
    for c in c_values:
        # Initialize the Splay Tree and insert elements
        tree = SplayTree()
        for i in range(n):
            tree.insert(i)

        # Generate list
        arr = generate_custom_list(n, m, c, x)

        # Reset search counter before testing
        tree.search_counter = 0
        for i in arr:
            if i == x:
                tree.search(x)

        # Store the search counter result for the current c
        search_counter_per_c.append(tree.search_counter / (m * c / 100.0))

    search_counter_results.append(search_counter_per_c)

# Prepare data for plotting
c_plot = []
m_plot = []
search_counter_plot = []

for i, m in enumerate(m_values):
    for j, c in enumerate(c_values):
        c_plot.append(c)
        m_plot.append(i)  # Use the index of m_values for equispacing
        search_counter_plot.append(search_counter_results[i][j])

# Create 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=c_plot,
    y=m_plot,
    z=search_counter_plot,
    mode='markers',
    marker=dict(size=5)  # Adjust marker size if needed
)])

# Update layout with axis labels and custom tick values for y-axis
fig.update_layout(scene=dict(
    xaxis_title='Percentage of x (c)',
    yaxis_title='List Size (m)',
    zaxis_title='Search Counter per Query',
    yaxis=dict(
        tickvals=list(range(len(m_values))),  # Set tick positions
        ticktext=m_values  # Set tick labels
    )
))

# Show the plot
fig.show()
