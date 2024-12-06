import random
# 定义老师排课问题的参数

# 定义遗传算法的参数
population_size = 100  # 种群大小
generations = 10  # 迭代次数
mutation_rate = 0.01  # 变异概率

# 初始化种群
def initialize_population(population_size, teachers):
    population = []
    for _ in range(population_size):
        schedule = {teacher["name"]: (random.choice(teacher["days"]), random.choice(["1-2节", "3-4节", "5-6节", "7-8节", "9-10节"])) for teacher in teachers}
        population.append(schedule)
    return population

# 计算适应度
def fitness(schedule):
    fitness_score = 0
    for teacher, (day, period) in schedule.items():
        if teacher in ["汪卫星", "张丽英"]:
            fitness_score += 1  # 优先考虑电脑性能高的老师
        elif teacher == "肖小红":
            fitness_score += 1  # 优先考虑连续4节的老师
    return fitness_score

# 选择操作
def select(population):
    population.sort(key=fitness, reverse=True)
    return population[:int(population_size * 0.2)]  # 选择前20%的解

# 交叉操作
def crossover(parent1, parent2, teachers):
    child1 = parent1.copy()
    child2 = parent2.copy()
    for teacher in teachers:
        if random.random() < 0.5:
            child1[teacher["name"]], child2[teacher["name"]] = child2[teacher["name"]], child1[teacher["name"]]
    return child1, child2

# 变异操作
def mutate(schedule, teachers):
    for teacher in teachers:
        if random.random() < mutation_rate:
            schedule[teacher["name"]] = (random.choice(teacher["days"]), random.choice(["1-2节", "3-4节", "5-6节", "7-8节", "9-10节"]))
    return schedule

# 遗传算法主函数
def genetic_algorithm(teachers):
    population = initialize_population(population_size, teachers)
    for _ in range(generations):
        selected_population = select(population)
        children = []
        for _ in range(population_size // 2):
            parent1, parent2 = random.sample(selected_population, 2)
            child1, child2 = crossover(parent1, parent2, teachers)
            children.extend([mutate(child1, teachers), mutate(child2, teachers)])
        population = children
    best_schedule = population[0]
    return [[teacher, day, period] for teacher, (day, period) in best_schedule.items()]

