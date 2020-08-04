from chatbot.workflow import update_model, ask_bot

if __name__ == '__main__':
    # database link
    filepath = './input/chatbot_database.txt'
    
    # train model
    update_model(filepath)

    # ask the bot
    ask_bot('what is a chat bot')