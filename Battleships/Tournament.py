from itertools import combinations
import numpy as np
import matplotlib.pyplot as plt


def mapValue(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class Tournament:
    round = 0

    def __init__(self, contestants, rounds=10):
        self.contestants = contestants
        self.rounds = rounds

        self.data = {}

    def begin(self):
        matches = list(combinations(self.contestants, 2))

        for i, match in enumerate(matches):
            # print("{sep}[ match {n} ]{sep}".format(sep="-" * 10, n=i + 1))

            contestant1, contestant2 = match
            self.data.setdefault(contestant1, [])
            self.data.setdefault(contestant2, [])

            for roundID in range(self.rounds):
                # print(f"-- round {roundID+1} --")
                while not contestant1.hasWon(against=contestant2) and not contestant2.hasWon(against=contestant1):
                    contestant1.attack(contestant2)
                    contestant2.attack(contestant1)

                contestant1.score.wonTimes += (1 if contestant1.hasWon(against=contestant2) else 0)
                contestant2.score.wonTimes += (1 if contestant2.hasWon(against=contestant1) else 0)

                contestant1.score.gamesPlayed += 1
                contestant2.score.gamesPlayed += 1

                self.data[contestant1].append({'against': contestant2, 'score': contestant1.score})
                self.data[contestant2].append({'against': contestant1, 'score': contestant2.score})

                contestant1.reset()
                contestant2.reset()

            # print("{sep}[ match has ended ]{sep}".format(sep="-" * 10))

    def print_score(self):
        for contestant in self.data:
            hits = sum(score['score'].__dict__["hit"] for score in self.data[contestant])
            missed = sum(score['score'].__dict__["missed"] for score in self.data[contestant])
            shipsSank = sum(score['score'].__dict__["shipsSank"] for score in self.data[contestant])
            wonTimes = sum(score['score'].__dict__["wonTimes"] for score in self.data[contestant])
            playedTimes = sum(score['score'].__dict__["gamesPlayed"] for score in self.data[contestant])

            print("Player", contestant.strategy.__class__.__name__ + ":")
            print(" " * 4, "Hit:", hits)
            print(" " * 4, "Missed:", missed)
            print(" " * 4, "ShipsSank:", shipsSank)
            print(" " * 4, "WonTimes:", wonTimes)
            print()
            print(" " * 4, "Hitrate:", round(hits / (hits + missed) * 100, 2), "%")
            print(" " * 4, "Winrate:", round(wonTimes / playedTimes * 100, 2), "%")
            print()

    @staticmethod
    def graph(data):
        entries = [contestant.strategy.name for contestant in data.keys()]
        wonTimes = {}
        for contestant1 in data:
            for score_zaznam in data[contestant1]:
                contestant2 = score_zaznam['against']

                category_name = "{cont1} vs. {cont2}".format(cont1=contestant1.strategy.name,
                                                             cont2=contestant2.strategy.name)
                if category_name not in wonTimes:
                    wonTimes[category_name] = score_zaznam['score']
                else:
                    wonTimes[category_name] += score_zaznam['score']

        index = np.arange(len(entries))
        maxMarkersize = wonTimes[max(wonTimes, key=lambda category_name: wonTimes[category_name].wonTimes)].wonTimes

        for category_name in wonTimes:
            contestant1, contestant2 = category_name.split(" vs. ")
            x = entries.index(contestant1)
            y = entries.index(contestant2)

            markersize = mapValue(wonTimes[category_name].wonTimes, 0, maxMarkersize, 0, 20)
            plt.plot(x, y, 'ro', markersize=markersize)

        plt.xticks(index, entries, rotation='vertical')
        plt.yticks(index, entries)

        plt.show()

        """
        fig, ax = plt.subplots()

        rects1 = ax.bar(index, misses, bar_width,
                        alpha=opacity, color='b',
                        label='Misses')

        rects2 = ax.bar(index + bar_width, hits, bar_width,
                        alpha=opacity, color='r',
                        label='Hits')

        ax.set_xlabel('Contestant')
        ax.set_ylabel('Score')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(entries)
        ax.legend()

        for i, rect in enumerate(rects1):
            height = rect.get_height()
            top_text = str(round(100 / (hits[i] + misses[i]) * hits[i], 2)) + " %"
            plt.text(rect.get_x() + rect.get_width() / 2.0, height, top_text, ha='center', va='bottom')

        fig.tight_layout()
        plt.show()
        """
