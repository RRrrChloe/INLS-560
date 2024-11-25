import pandas as pd
def main():
    roster = ["Claude", "Brown", "Cadeau"]
    for i in roster:
        print()
        
    data = pd.DataFrame({"Last name: " roster})
    print(data)
      #data.rename(columns={"0": "Last Name"})
    
main()