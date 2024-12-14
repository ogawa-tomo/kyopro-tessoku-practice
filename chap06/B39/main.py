N, D = map(int, input().split())


class Job:
    def __init__(self, start, reward):
        self.start = start
        self.reward = reward

    def __lt__(self, other):
        return self.reward > other.reward

    def __repr__(self):
        return f"[start: {self.start}, reward: {self.reward}]"


jobs: list[Job] = []
for _ in range(N):
    start, reward = map(int, input().split())
    start -= 1
    job = Job(start, reward)
    jobs.append(job)
jobs.sort()
print(jobs)

# for job in jobs:
