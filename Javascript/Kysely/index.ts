require('dotenv').config()
import { Kysely, MysqlDialect } from 'kysely'
import { createPool } from "mysql2";

const db = new Kysely<any>({
    // Use MysqlDialect for MySQL and SqliteDialect for SQLite.
    dialect: new MysqlDialect({
        pool: createPool({
            host: process.env.host,
            user: process.env.user,
            password: process.env.password,
            database: process.env.database,
        }),
    })
})

async function getData() {
    console.time()
    let data = await db.selectFrom('2021_AusCensus')
        .selectAll()
        .where('Location', '=', 'Queensland')
        .execute()
    console.timeEnd()
    console.log(data[0].Male)
    // Timing of this query on my own self hosted shitty hardware was 79ms for the 2021 Australian Census. 
    // Can be fixed with better hardware and caching. If the data never changes, cache at network, redis and anywhere that's free.
}

getData()
