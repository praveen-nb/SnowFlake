# SnowFlake
Snowflake Security and Compliance: Ensuring Data Protection and Regulatory Compliance
import snowflake.connector

# Establishing connection to Snowflake
conn = snowflake.connector.connect(
    user='your_username',
    password='your_password',
    account='your_account',
    warehouse='your_warehouse',
    database='your_database',
    schema='your_schema'
)

# Creating a role for data access
def create_role(role_name):
    try:
        conn.cursor().execute(f'CREATE ROLE {role_name}')
        print(f'Role "{role_name}" created successfully.')
    except snowflake.connector.errors.ProgrammingError:
        print(f'Role "{role_name}" already exists.')

# Granting privileges to the role
def grant_privileges(role_name, privilege, object_name):
    try:
        conn.cursor().execute(f'GRANT {privilege} ON {object_name} TO ROLE {role_name}')
        print(f'Privilege "{privilege}" granted on "{object_name}" to role "{role_name}" successfully.')
    except snowflake.connector.errors.ProgrammingError:
        print(f'Failed to grant privilege "{privilege}" on "{object_name}" to role "{role_name}".')

# Enabling data encryption
def enable_encryption():
    try:
        conn.cursor().execute('USE SCHEMA your_schema')
        conn.cursor().execute('ALTER SCHEMA your_schema SET ENCRYPTION = ON')
        print('Data encryption enabled successfully.')
    except snowflake.connector.errors.ProgrammingError:
        print('Failed to enable data encryption.')

# Implementing auditing
def enable_auditing():
    try:
        conn.cursor().execute('USE SCHEMA your_schema')
        conn.cursor().execute('ALTER SCHEMA your_schema SET TRANSIENT = FALSE')
        conn.cursor().execute('ALTER DATABASE your_database SET AUDITING = TRUE')
        print('Auditing enabled successfully.')
    except snowflake.connector.errors.ProgrammingError:
        print('Failed to enable auditing.')

# Calling the functions to execute the security measures
create_role('data_access_role')
grant_privileges('data_access_role', 'SELECT', 'your_table')
enable_encryption()
enable_auditing()

# Closing the connection
conn.close()
