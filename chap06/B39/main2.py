import heapq

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
    # heapq.heappush(jobs, job)

jobs.sort(key=lambda job: job.start)
# print(jobs)

job_queue: list[Job] = []
job_index = 0
reward = 0
for day in range(D):
    # その日にできる仕事をキューにためる
    while True:
        if job_index >= N:
            break
        job = jobs[job_index]
        if job.start <= day:
            heapq.heappush(job_queue, job)
        else:
            break
        job_index += 1

    if len(job_queue) > 0:
        job = heapq.heappop(job_queue)
        # print(job)
        reward += job.reward

print(reward)
