import streamlit as st

st.title("🧠 Beginner Python Project Menu")

menu_options = [
    "1. Hello World",
    "2. Name Printing",
    "3. Basic Calculator using if-else",
    "4. Calculator by Mod Menu",
    "5. Palindrome Number Checker",
    "6. Armstrong Number Checker",
    "7. Strong Number Checker",
    "8. Square of a Number",
    "9. Volume of Cylinder by Function Calling",
    "10. Decimal to Binary Converter",
    "11. Binary to Decimal Converter",
    "12. Prime Number Checker",
    "13. Even/Odd Checker",
    "14. Factorial of a Number",
    "15. Factors of a Number",
    "16. Grade Generator"
]

choice = st.selectbox("Choose a program to run:", menu_options)

st.write("---")

if choice == "1. Hello World":
    st.subheader("Hello World")
    st.code("print('Hello World')")
    st.success("Hello World")

elif choice == "2. Name Printing":
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Entered name is: {name}")

elif choice == "3. Basic Calculator using if-else":
    num1 = st.number_input("Enter first number")
    operator = st.selectbox("Operator", ["+", "-", "*", "/"])
    num2 = st.number_input("Enter second number")

    if st.button("Calculate"):
        if operator == "+":
            st.success(f"Result: {num1 + num2}")
        elif operator == "-":
            st.success(f"Result: {num1 - num2}")
        elif operator == "*":
            st.success(f"Result: {num1 * num2}")
        elif operator == "/":
            if num2 != 0:
                st.success(f"Result: {num1 / num2}")
            else:
                st.error("Cannot divide by zero!")

elif choice == "4. Calculator by Mod Menu":
    a = st.number_input("Enter first number")
    b = st.number_input("Enter second number")
    op = st.selectbox("Choose operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

    if st.button("Calculate Result"):
        if op == "Addition":
            st.success(f"Result: {a + b}")
        elif op == "Subtraction":
            st.success(f"Result: {a - b}")
        elif op == "Multiplication":
            st.success(f"Result: {a * b}")
        elif op == "Division":
            if b != 0:
                st.success(f"Result: {a / b}")
            else:
                st.error("Cannot divide by zero!")

elif choice == "5. Palindrome Number Checker":
    num = st.number_input("Enter a number:", step=1.0, format="%.0f")
    if st.button("Check"):
        original = int(num)
        reversed_num = int(str(original)[::-1])
        if original == reversed_num:
            st.success(f"{original} is a palindrome number.")
        else:
            st.warning(f"{original} is not a palindrome number.")

elif choice == "6. Armstrong Number Checker":
    num = st.number_input("Enter a number:", step=1.0, format="%.0f")
    if st.button("Check Armstrong"):
        n = int(num)
        order = len(str(n))
        total = sum(int(d) ** order for d in str(n))
        if total == n:
            st.success(f"{n} is an Armstrong number.")
        else:
            st.warning(f"{n} is not an Armstrong number.")

elif choice == "7. Strong Number Checker":
    def factorial(n):
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f

    num = st.number_input("Enter a number:", step=1.0, format="%.0f")
    if st.button("Check Strong Number"):
        temp = int(num)
        total = sum(factorial(int(d)) for d in str(temp))
        if total == temp:
            st.success(f"{temp} is a Strong number.")
        else:
            st.warning(f"{temp} is not a Strong number.")

elif choice == "8. Square of a Number":
    num = st.number_input("Enter a number:")
    if st.button("Find Square"):
        st.success(f"Square of {num} is {num**2}")

elif choice == "9. Volume of Cylinder by Function Calling":
    def volume(radius, height):
        return 3.1416 * radius * radius * height

    r = st.number_input("Enter radius:")
    h = st.number_input("Enter height:")
    if st.button("Calculate Volume"):
        vol = volume(r, h)
        st.success(f"Volume of the cylinder is: {vol}")

elif choice == "10. Decimal to Binary Converter":
    num = st.number_input("Enter a decimal number:", step=1.0, format="%.0f")
    if st.button("Convert to Binary"):
        st.success(f"Binary: {bin(int(num))[2:]}")

elif choice == "11. Binary to Decimal Converter":
    binary = st.text_input("Enter a binary number:")
    if st.button("Convert to Decimal"):
        try:
            decimal = int(binary, 2)
            st.success(f"Decimal: {decimal}")
        except:
            st.error("Invalid binary number")

elif choice == "12. Prime Number Checker":
    num = st.number_input("Enter a number:", step=1.0, format="%.0f")
    if st.button("Check Prime"):
        n = int(num)
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    st.warning(f"{n} is not a prime number.")
                    break
            else:
                st.success(f"{n} is a prime number.")
        else:
            st.warning(f"{n} is not a prime number.")

elif choice == "13. Even/Odd Checker":
    num = st.number_input("Enter a number:", step=1.0, format="%.0f")
    if st.button("Check Even/Odd"):
        if int(num) % 2 == 0:
            st.success(f"{int(num)} is even.")
        else:
            st.success(f"{int(num)} is odd.")

elif choice == "14. Factorial of a Number":
    num = st.number_input("Enter a number:", step=1.0, format="%.0f")
    if st.button("Find Factorial"):
        fact = 1
        for i in range(1, int(num) + 1):
            fact *= i
        st.success(f"Factorial of {int(num)} is {fact}")

elif choice == "15. Factors of a Number":
    num = st.number_input("Enter a number:", step=1.0, format="%.0f")
    if st.button("Find Factors"):
        n = int(num)
        factors = [str(i) for i in range(1, n + 1) if n % i == 0]
        st.success("Factors: " + ", ".join(factors))

elif choice == "16. Grade Generator":
    marks = st.slider("Enter your marks (0-100):", 0, 100)
    if st.button("Generate Grade"):
        if marks >= 90:
            st.success("Grade: A")
        elif marks >= 80:
            st.success("Grade: B")
        elif marks >= 70:
            st.success("Grade: C")
        elif marks >= 60:
            st.success("Grade: D")
        else:
            st.error("Grade: F")
