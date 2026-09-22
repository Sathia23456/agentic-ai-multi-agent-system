from agents import ResearchAgent, AnalysisAgent, DecisionAgent


def main():
    topic = input("Enter a topic: ")

    research_agent = ResearchAgent()
    analysis_agent = AnalysisAgent()
    decision_agent = DecisionAgent()

    research = research_agent.run(topic)
    analysis = analysis_agent.run(research)
    decision = decision_agent.run(analysis)

    print("\n--- Agentic AI Result ---")
    print(research)
    print(analysis)
    print(decision)


if __name__ == "__main__":
    main()
