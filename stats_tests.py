from charles.charles import Population, Individual
from data.sudoku_puzzles import easy, medium, hard, expert
from charles.selection import fps, tournament, rank
from charles.mutation import (
    swap_mutation,
    multiple_swap_mutation,
    random_mutation,
    intelligent_random_mutation,
    inversion_mutation,
    partial_inversion_mutation,
)
from charles.crossover import single_point_co, two_point_co, uniform_co
from charles.fitness_functions import evaluate, evaluate_robust
from charles.stats_functions import testing_plot, create_and_plot
import numpy as np

# Monkey Patching
Individual.evaluate = evaluate
# Individual.evaluate = evaluate_robust

# Runs for the best GA
runs = 30

for i in range(runs):
    print("Run:", i)

    pop_test = Population(
        grid_initial=easy,
        size=1000,
        optim="min",
        sol_size=len(easy),
        valid_set=list(np.arange(1, 10)),
        file_name="best_run",
    )

    pop_test.evolve(
        gens=75,
        select=tournament,
        crossover=two_point_co,
        mutate=swap_mutation,
        co_p=0.7,
        mu_p=0.9,
        elitism=True,
    )

# Testing plots
testing_plot(
    names=[
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_fps_swap_uniform.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_rank_swap_uniform.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_tournament_swap_uniform.csv",
    ],
    legends=[
        "FPS",
        "Rank selection",
        "Tournament selection",
    ],
    subheading="Easy puzzle - Uniform crossover and swap mutation",
    plot_name="Chart1",
)

testing_plot(
    names=[
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_fps_swap_uniform.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_rank_swap_uniform.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_tournament_swap_uniform.csv",
    ],
    legends=[
        "FPS",
        "Rank selection",
        "Tournament selection",
    ],
    subheading="Expert puzzle - Uniform crossover and swap mutation",
    plot_name="Chart2",
)

testing_plot(
    names=[
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_fps_swap_single.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_rank_swap_single.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_tournament_swap_single.csv",
    ],
    legends=[
        "FPS",
        "Rank selection",
        "Tournament selection",
    ],
    subheading="Easy puzzle - Single-point crossover and swap mutation",
    plot_name="Chart3",
)

testing_plot(
    names=[
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_fps_swap_single.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_rank_swap_single.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_tournament_swap_single.csv",
    ],
    legends=[
        "FPS",
        "Rank selection",
        "Tournament selection",
    ],
    subheading="Expert puzzle - Single-point crossover and swap mutation",
    plot_name="Chart4",
)

testing_plot(
    names=[
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_fps_swap_two.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_rank_swap_two.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_tournament_swap_two.csv",
    ],
    legends=[
        "FPS",
        "Rank selection",
        "Tournament selection",
    ],
    subheading="Easy puzzle - Two-point crossover and swap mutation",
    plot_name="Chart5",
)

testing_plot(
    names=[
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_fps_swap_two.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_rank_swap_two.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_tournament_swap_two.csv",
    ],
    legends=[
        "FPS",
        "Rank selection",
        "Tournament selection",
    ],
    subheading="Expert puzzle - Two-point crossover and swap mutation",
    plot_name="Chart6",
)

testing_plot(
    names=[
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_tournament_multiple_swap_two_point.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_tournament_random_two_point.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_tournament_intelligent_random_two_point.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_tournament_inversion_mutation_two_point.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_tournament_partial_inversion_two_point.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\easy_tournament_swap_mutation_two_point.csv",
    ],
    legends=[
        "Multiple swap mutation",
        "Random mutation",
        "Intelligent random mutation",
        "Inversion mutation",
        "Partial inversion mutation",
        "Swap mutation",
    ],
    subheading="Easy puzzle - Tournament selection and two-point crossover",
    plot_name="Chart7",
)

testing_plot(
    names=[
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_tournament_multiple_swap_two_point.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_tournament_random_two_point.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_tournament_intelligent_random_two_point.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_tournament_inversion_mutation_two_point.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_tournament_partial_inversion_two_point.csv",
        "C:\\Users\\helen\\Downloads\\Testes_csv\\Testes_csv\\expert_tournament_swap_mutation_two_point.csv",
    ],
    legends=[
        "Multiple swap mutation",
        "Random mutation",
        "Intelligent random mutation",
        "Inversion mutation",
        "Partial inversion mutation",
        "Swap mutation",
    ],
    subheading="Expert puzzle - Tournament selection and two-point crossover",
    plot_name="Chart8",
)

# Final plot
create_and_plot("best_run.csv", "best_run")
