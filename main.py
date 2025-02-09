import random

#rookie way
def approach_one():
    numbers: list[float] = [ 0.1, 0.2, 0.3, 0.4, 0.5, 0.6,0.7, 0.8, 0.9, 1]
    indexes : dict[int,list[float]] = {
            1:[],
            2:[],
            3:[],
            4:[],
            5:[],
            6:[]
            }
    #generator 
    def generator() -> float:
        random_number = random.choice(numbers)
        return random_number

    for _ in range(0,1000):
       working_number = generator()
       if working_number <= 1/6:
           indexes[1].append(working_number)
           continue
       if working_number <= 2/6:
           indexes[2].append(working_number)
           continue
       if working_number <= 3/6:
           indexes[3].append(working_number)
           continue
       if working_number <= 4/6:
           indexes[4].append(working_number)
           continue
       if working_number <= 5/6:
           indexes[5].append(working_number)
           continue
       if working_number <= 6/6:
           indexes[6].append(working_number)
           continue
    
    total: int = sum(len(v) for v in indexes.values())
    data = [[index, len(indexes[index]), f"{round((len(indexes[index]) / 1000) * 100, 1)}%"] for index in indexes]
    data.append(["Total", total, ""])
    
    print(f"{'FACE':^10} | {'FREQUENCY':^10} | {'PERCENTAGE':^12}")
    print("-" * 36)

    for index, values in indexes.items():
        count = len(values)
        percentage = round((count / 1000) * 100, 1)
        print(f"{index:^10} | {count:^10} | {percentage:^12}%")

    print("-" * 36)
    print(f"{'Total':^10} | {total:^10} |")

#the pro way 
def approach_two():
    def generator(start: int, stop: int) -> float:
        number = random.uniform(start, stop)
        return number

    faces:dict[int,list[float]] = {
            1:[],
            2:[],
            3:[],
            4:[],
            5:[],
            6:[]
            }

    for _ in range(0,1000):
        working_number = generator(0,1)
        if working_number <= 1/6:
           faces[1].append(working_number)
           continue
        if working_number <= 2/6:
           faces[2].append(working_number)
           continue
        if working_number <= 3/6:
           faces[3].append(working_number)
           continue
        if working_number <= 4/6:
           faces[4].append(working_number)
           continue
        if working_number <= 5/6:
           faces[5].append(working_number)
           continue
        if working_number <= 6/6:
           faces[6].append(working_number)
           continue

    total: int = sum(len(v) for v in faces.values())
    data = [[face, len(faces[face]), f"{round((len(faces[face]) / 1000) * 100, 1)}%"] for face in faces]
    data.append(["Total", total, ""])
    
    print(f"{'FACE':^10} | {'FREQUENCY':^10} | {'PERCENTAGE':^12}")
    print("-" * 36)

    for face, values in faces.items():
        count = len(values)
        percentage = round((count / 1000) * 100, 1)
        print(f"{face:^10} | {count:^10} | {percentage:^12}%")

    print("-" * 36)
    print(f"{'Total':^10} | {total:^10} |")

if __name__ == "__main__":
    print("Welcome to the dice rolling simulator")
    print("approach one or two?")
    print("1. Rookie way")
    approach_one()
    print( )
    print("2. Pro way")
    approach_two()
