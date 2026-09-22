class ResearchAgent:
    def run(self, topic):
        return f"Research Agent analyzed: {topic}"


class AnalysisAgent:
    def run(self, research):
        return f"Analysis Agent processed: {research}"


class DecisionAgent:
    def run(self, analysis):
        return f"Decision Agent created a decision from: {analysis}"
