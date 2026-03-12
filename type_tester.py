# This script helps us understand how Python 'thinks'
def main():
    print("--- 🧠 The Type-Checking Lab ---")
    
    # Let's get a number from you
    user_input = input("Enter a number to double: ")
    
    # ❌ THE WRONG WAY (Uncomment the line below to see it fail later!)
    # result = user_input * 2 
    
    # ✅ THE RIGHT WAY
    # We 'cast' (convert) the text into an integer
    true_number = int(user_input)
    final_result = true_number * 2
    
    print(f"You entered: {user_input}")
    print(f"When we double it correctly, we get: {final_result}")

if __name__ == "__main__":
    main()
