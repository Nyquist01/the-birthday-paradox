
import random
import matplotlib.pyplot as plt


class TheBirthdayParadox():
    def __init__(self):
        self.cumulative_probability_of_pair = {}

    def run_simulation(self, simulations: int, number_of_people: int):
        """
        Generate a list of random birthdays and iterate over the list until a duplicate pair is found.
        Repeat for n simulations
        """
        pairs_by_group_size = {key: 0 for key in range(1, number_of_people + 1)}
        for _ in range(simulations):
            birthdays = [random.randint(1, 365) for _ in range(number_of_people)]
            seen_birthdays = set()
            for index, birthday in enumerate(birthdays):
                if birthday in seen_birthdays:
                    pairs_by_group_size[index + 1] += 1
                    break
                else:
                    seen_birthdays.add(birthday)

        # cumulative probability calculation
        cumulative_prob = 0
        for key in pairs_by_group_size:
            cumulative_prob += pairs_by_group_size[key]
            self.cumulative_probability_of_pair[key] = (cumulative_prob / simulations) * 100

        self.generate_graph()

    def generate_graph(self):
        x = list(self.cumulative_probability_of_pair.keys())
        y = list(self.cumulative_probability_of_pair.values())
        plt.plot(x, y, marker='o', linestyle='-', color='b')

        # find x axis intersection where probability = 50%
        for index, value in enumerate(y):
            if value >= 50:
                x_intersection_index = index
                plt.axhline(y = 50, color = 'black', linestyle = '--')
                plt.axvline(x = x[x_intersection_index], color = 'black', linestyle = '--')
                break

        plt.title(f"The Birthday Paradox")
        plt.xlabel("Number of people")
        plt.ylabel("Probably of duplicate birthdays in group")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    problem = TheBirthdayParadox()
    problem.run_simulation(simulations=10000, number_of_people=100)
