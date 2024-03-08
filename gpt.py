from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import sqlite3

def connect_to_database(database_url):
    connection = sqlite3.connect(database_url)
    return connection

def execute_sql_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

DATABASE_URL = 'example.db'

chatbot = ChatBot('MyBot')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

def get_bot_response(user_input):
    return chatbot.get_response(user_input)

def main():
    # Conectar ao banco de dados
    db_connection = connect_to_database(DATABASE_URL)

    # Interagir com o usuário
    while True:
        user_input = input("Você: ")

        if user_input.lower() == 'sair':
            break

        bot_response = get_bot_response(user_input)

        sql_query = bot_response.text
        query_result = execute_sql_query(db_connection, sql_query)

        print("Bot:", bot_response)
        print("Resultado da Consulta:", query_result)

    db_connection.close()

if __name__ == "__main__":
    main()
