import asyncio

import asyncpg


async def async_main():
    await asyncio.sleep(3)
    conn = await asyncpg.connect(user='postgres', password='',
                                 database='test_database', host='database')
    values = await conn.fetch('''SELECT * FROM character_names''')
    for value in values:
        print(f"{value['field1']} - {value['field2']}")

    await conn.close()


if __name__ == "__main__":
    asyncio.run(async_main())




