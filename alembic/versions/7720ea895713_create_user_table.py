"""create user table

Revision ID: 7720ea895713
Revises: 
Create Date: 2023-04-18 13:58:48.318420

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime
from src.authent.services import get_password_hash
from src.settings import ADMIN_PASSWORD
# revision identifiers, used by Alembic.
revision = '7720ea895713'
down_revision = None
branch_labels = None
depends_on = None
import uuid

def upgrade() -> None:
    user_table = op.create_table(
        "user",
        sa.Column("id", sa.UUID, nullable=False, primary_key=True),
        sa.Column("email", sa.String, unique=True, nullable=True, index=True),
        sa.Column("username", sa.String, unique=True, index=True),
        sa.Column("first_name", sa.String),
        sa.Column("last_name", sa.String),
        sa.Column("hashed_password", sa.String),
        sa.Column("is_active", sa.Boolean, default=True),
        sa.Column("is_admin", sa.Boolean, default=False),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime)
    )

    #seed admin account
    op.bulk_insert(user_table, [
        {
            "id": uuid.uuid4(),
            "email": "admin@sample.com",
            "username": "admin",
            "hashed_password": get_password_hash(ADMIN_PASSWORD),
            "first_name": "Admin",
            "last_name": "Admin",
            "is_active": True,
            "is_admin": True,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
        }
    ])



def downgrade() -> None:
    op.drop_table("user")
