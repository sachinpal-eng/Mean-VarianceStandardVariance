import numpy as np

class StatisticsCalculator:
    def __init__(self, data):
        self.data = np.array(data)

    def mean(self):
        return np.mean(self.data)

    def variance(self):
        return np.var(self.data)

    def standard_deviation(self):
        return np.std(self.data)

    def summary(self):
        return {
            "Mean": self.mean(),
            "Variance": self.variance(),
            "Standard Deviation": self.standard_deviation()
        }

# ---------------- MAIN PROGRAM ---------------- #

if __name__ == "__main__":
    print("📊 Mean-Variance-Standard Deviation Calculator")
    print("Enter numbers separated by spaces:")
    
    try:
        # Take user input
        numbers = list(map(float, input().split()))
        
        # Create calculator object
        calc = StatisticsCalculator(numbers)
        
        # Get results
        results = calc.summary()
        
        print("\nResults:")
        for key, value in results.items():
            print(f"{key}: {value:.4f}")
    
    except ValueError:
        print("❌ Please enter valid numeric values.")
