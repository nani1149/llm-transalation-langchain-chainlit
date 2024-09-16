from db import pool
import sqlalchemy

# Connect to the connection pool
with pool.connect() as db_conn:
    # Create users table
    db_conn.execute(
        sqlalchemy.text(
            """
            CREATE TABLE IF NOT EXISTS users (
                id UUID PRIMARY KEY,
                identifier TEXT NOT NULL UNIQUE,
                metadata JSONB NOT NULL,
                createdAt TEXT
            );
            """
        )
    )

    # Create threads table
    db_conn.execute(
        sqlalchemy.text(
            """
            CREATE TABLE IF NOT EXISTS threads (
                id UUID PRIMARY KEY,
                createdAt TEXT,
                name TEXT,
                userId UUID,
                userIdentifier TEXT,
                tags TEXT[],
                metadata JSONB,
                FOREIGN KEY (userId) REFERENCES users(id) ON DELETE CASCADE
            );
            """
        )
    )

    # Create steps table
   # Create steps table
    db_conn.execute(
    sqlalchemy.text(
        """
        CREATE TABLE IF NOT EXISTS steps (
            id UUID PRIMARY KEY,
            name TEXT NOT NULL,
            type TEXT NOT NULL,
            threadId UUID NOT NULL,
            parentId UUID,
            disableFeedback BOOLEAN NOT NULL,
            streaming BOOLEAN NOT NULL,
            waitForAnswer BOOLEAN,
            isError BOOLEAN,
            metadata JSONB,
            tags TEXT[],
            input TEXT,
            output TEXT,
            createdAt TEXT,
            start TEXT,
            "end" TEXT,  -- Quote the "end" column to avoid conflicts with reserved keyword
            generation JSONB,
            showInput TEXT,
            language TEXT,
            indent INT
        );
        """
    )
    )


    # Create elements table
    db_conn.execute(
        sqlalchemy.text(
            """
            CREATE TABLE IF NOT EXISTS elements (
                id UUID PRIMARY KEY,
                threadId UUID,
                type TEXT,
                url TEXT,
                chainlitKey TEXT,
                name TEXT NOT NULL,
                display TEXT,
                objectKey TEXT,
                size TEXT,
                page INT,
                language TEXT,
                forId UUID,
                mime TEXT
            );
            """
        )
    )

    # Create feedbacks table
    db_conn.execute(
        sqlalchemy.text(
            """
            CREATE TABLE IF NOT EXISTS feedbacks (
                id UUID PRIMARY KEY,
                forId UUID NOT NULL,
                threadId UUID NOT NULL,
                value INT NOT NULL,
                comment TEXT
            );
            """
        )
    )

    # Commit transaction (SQLAlchemy v2.X.X is commit as you go)
    db_conn.commit()
