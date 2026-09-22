def agent(name, task):
    print(f"{name} is working on: {task}")
    return f"{name} completed the task"


def main():
    agents = [
        ("Research Agent", "Collect information"),
        ("Analysis Agent", "Analyze the information"),
        ("Decision Agent", "Make a final decision")
    ]

    for name, task in agents:
        result = agent(name, task)
        print(result)


if __name__ == "__main__":
    main()
