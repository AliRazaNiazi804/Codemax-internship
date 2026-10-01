def simple_chatbot():
    print("chatbot: Hi! i am a simple rule_based Ai. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == 'exit':
            print("Chatbot:")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I assist you learn python?")
        elif "ai" in user_input:
            print("Chatbot: AI stands for Artificial Intelligence. It's fascinating!")
        elif "python" in user_input:
            print("Chatbot: Python is a the best langugar for beginners. It's versatile and widely used in AI and web development.")
        else:
            print("Chatbot: I'm still learning. Can you please rephrase or ask something else?")

# Run the chatbot
simple_chatbot()