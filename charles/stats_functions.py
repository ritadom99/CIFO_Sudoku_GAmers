from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd


def testing_plot(names, legends, plot_name, subheading):
    for i in range(len(names)):
        if i == 0:
            df1 = pd.read_csv(
                names[0],
                names=[
                    "Generation",
                    "Best_r",
                    "Best fitness",
                    "Worst_r",
                    "Worst fitness",
                    "Avg fitness",
                ],
            )
            df1["Type"] = legends[0]

        elif i == 1:
            df2 = pd.read_csv(
                names[1],
                names=[
                    "Generation",
                    "Best_r",
                    "Best fitness",
                    "Worst_r",
                    "Worst fitness",
                    "Avg fitness",
                ],
            )
            df2["Type"] = legends[1]
            new = pd.concat([df1, df2])

        elif i == 2:
            df3 = pd.read_csv(
                names[2],
                names=[
                    "Generation",
                    "Best_r",
                    "Best fitness",
                    "Worst_r",
                    "Worst fitness",
                    "Avg fitness",
                ],
            )
            df3["Type"] = legends[2]
            new = pd.concat([new, df3])

        elif i == 3:
            df4 = pd.read_csv(
                names[3],
                names=[
                    "Generation",
                    "Best_r",
                    "Best fitness",
                    "Worst_r",
                    "Worst fitness",
                    "Avg fitness",
                ],
            )
            df4["Type"] = legends[3]
            new = pd.concat([new, df4])

        elif i == 4:
            df5 = pd.read_csv(
                names[4],
                names=[
                    "Generation",
                    "Best_r",
                    "Best fitness",
                    "Worst_r",
                    "Worst fitness",
                    "Avg fitness",
                ],
            )
            df5["Type"] = legends[4]
            new = pd.concat([new, df5])

        elif i == 5:
            df6 = pd.read_csv(
                names[5],
                names=[
                    "Generation",
                    "Best_r",
                    "Best fitness",
                    "Worst_r",
                    "Worst fitness",
                    "Avg fitness",
                ],
            )
            df6["Type"] = legends[5]
            new = pd.concat([new, df6])

    plt.figure(figsize=(13, 8))
    sns.lineplot(data=new, x="Generation", y="Best fitness", hue="Type", ci=95)
    plt.title(subheading, fontsize=23)
    plt.legend(fontsize=13, labelspacing=1.2, borderpad=0.8)
    plt.ylabel("Average Best Fitness", fontsize=15)
    plt.xlabel("Generation", fontsize=15)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)

    # Save plot
    plt.savefig(plot_name + ".png", dpi=300)

    plt.show()


def create_and_plot(csv_name, plot_name):
    # Import and treat data
    df = pd.read_csv(
        csv_name,
        names=[
            "Generation",
            "Best_r",
            "Best fitness",
            "Worst_r",
            "Worst fitness",
            "Avg fitness",
        ],
    )
    df.set_index("Generation", inplace=True)
    df.drop(columns=["Best_r", "Worst_r"], inplace=True)

    # Create plot
    plt.figure(figsize=(13, 8))
    sns.lineplot(data=df, palette=["darkgreen", "red", "royalblue"], dashes=False)
    plt.ylim([0, max(df["Worst fitness"] + 5)])
    plt.title("Evolution of the GA", fontsize=23)
    plt.legend(fontsize=13, labelspacing=1.2, borderpad=0.8)
    plt.ylabel("Fitness", fontsize=15)
    plt.xlabel("Generation", fontsize=15)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)

    # Save plot
    plt.savefig(plot_name + ".png", dpi=300)

    plt.show()
