import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(12, 6))

# Network layers
layers = ['Input\n(x)', 'Hidden\nLayer 1', 'Hidden\nLayer 2', 'Output\n(ŷ)', 'Loss\nL(ŷ, y)']
x_positions = [1, 3, 5, 7, 9]

# Draw nodes
for i, (layer, x) in enumerate(zip(layers, x_positions)):
    ax.add_patch(patches.Rectangle((x-0.5, 0.5), 1, 1, 
                                   facecolor='lightblue', edgecolor='black'))
    ax.text(x, 1, layer, ha='center', va='center', fontsize=10)

# Forward pass arrows (blue)
for i in range(len(x_positions)-1):
    ax.annotate('', xy=(x_positions[i+1]-0.5, 1), xytext=(x_positions[i]+0.5, 1),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2))
    if i < len(x_positions)-2:
        ax.text((x_positions[i] + x_positions[i+1])/2, 1.2, 'Forward', 
                ha='center', color='blue', fontsize=9)

# Backward pass arrows (red)
for i in range(len(x_positions)-1, 0, -1):
    ax.annotate('', xy=(x_positions[i-1]+0.5, 1), xytext=(x_positions[i]-0.5, 1),
                arrowprops=dict(arrowstyle='->', color='red', lw=2, linestyle='--'))
    if i > 1:
        ax.text((x_positions[i] + x_positions[i-1])/2, 0.8, 'Backward\n(∇)', 
                ha='center', color='red', fontsize=9)

ax.text(5, 2, 'Backpropagation Flow', ha='center', fontsize=14, fontweight='bold')
ax.text(5, -0.5, 'Blue: Forward Pass (Prediction)\nRed: Backward Pass (Gradient Flow)', 
        ha='center', fontsize=10)

ax.set_xlim(0, 10)
ax.set_ylim(-1, 3)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.show()