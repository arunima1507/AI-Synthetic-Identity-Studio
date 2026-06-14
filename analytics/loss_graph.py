import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("training/losses.csv")

plt.figure(figsize=(10, 5))

plt.plot(
    df["epoch"],
    df["loss_d"],
    label="Discriminator Loss"
)

plt.plot(
    df["epoch"],
    df["loss_g"],
    label="Generator Loss"
)

plt.xlabel("Epoch")
plt.ylabel("Loss")

plt.title("GAN Training Loss")

plt.legend()
plt.grid()

plt.savefig(
    "analytics/loss_graph.png"
)

plt.show()