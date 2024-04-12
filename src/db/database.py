import asyncio

import asyncpg


async def addUser(id, name):
    connection = None
    try:
        connection = await asyncpg.connect(user="postgres",
                                     password="12345",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="surgpubot")
        query = f'''INSERT INTO users(id, name) VALUES($1, $2)
                  ON CONFLICT (id) DO UPDATE SET name = $3;'''
        await connection.execute(query, id, name, name)
    except (Exception) as error:
        print("Error while adding user to PostgreSQL", error)
    finally:
        if connection:
            await connection.close()


async def updateMessage(user_id, message_id):
    conn = None
    try:
        conn = await asyncpg.connect(user="postgres",
                                          password="12345",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="surgpubot")

        # Insert a record into the created table.
        await conn.execute('''
            UPDATE users SET message=$1 WHERE id=$2
        ''', message_id, user_id)
    except Exception as ex:
        print('Error while updating message ',ex)
    finally:
        await conn.close()


async def lastMessage(user_id):
    conn = None
    result = None
    try:
        conn = await asyncpg.connect(user="postgres",
                                     password="12345",
                                     host="127.0.0.1",
                                     port="5432",
                                     database="surgpubot")
        result = await conn.fetch(f'SELECT message FROM users WHERE id=$1', user_id)
    except Exception as ex:
        print('Error while fetching id of last message',ex)
    finally:
        await conn.close()
        if len(result)>=1:
            return dict(result[0])['message']
        else:
            return 0


