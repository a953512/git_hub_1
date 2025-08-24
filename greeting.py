def greet(name):
    return f"Hello, {name}!"

def main():
    names = ["Aman", "Rahul", "Pradeep"]
    for name in names:
        message = greet(name)
        print(message)

if __name__ == "__main__":
    main()
