def job_sequencing(jobs, deadlines, profits):
    n = len(jobs)
    
    job_list = [(profits[i], deadlines[i], jobs[i]) for i in range(n)]
    job_list.sort(reverse=True)
    
    max_deadline = max(deadlines)
    slots = [-1] * (max_deadline + 1)
    scheduled_jobs = []
    total_profit = 0
    
    for profit, deadline, job in job_list:
        for slot in range(deadline, 0, -1):
            if slots[slot] == -1:
                slots[slot] = job
                scheduled_jobs.append(job)
                total_profit += profit
                break
    
    return scheduled_jobs, total_profit

jobs = ['J1', 'J2', 'J3', 'J4', 'J5']
deadlines = [2, 1, 3, 2, 1]
profits = [100, 19, 27, 25, 15]

scheduled, profit = job_sequencing(jobs, deadlines, profits)
print("Scheduled jobs:", scheduled)
print("Total profit:", profit)