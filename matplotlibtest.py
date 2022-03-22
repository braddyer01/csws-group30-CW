import matplotlib.pyplot as plt
plt.style.use('ggplot')

x = ['Man Utd', 'West Ham Utd', 'Chealsea', 'Manchester City', 'Liverpool']
energy = [48, 49, 57, 68, 75]

x_pos = [i for i, _ in enumerate(x)]

plt.bar(x_pos, energy, color='green')
plt.xlabel("Team")
plt.ylabel("Goals scored")
plt.title("Goals scored by top teams")

plt.xticks(x_pos, x)

plt.show()