"""create company table

Revision ID: 51368d446dc1
Revises: 7720ea895713
Create Date: 2023-04-18 14:14:42.265152

"""
from alembic import op
import sqlalchemy as sa

from src.company.schemas import CompanyMode
# revision identifiers, used by Alembic.
revision = '51368d446dc1'
down_revision = '7720ea895713'
branch_labels = None
depends_on = None


def upgrade() -> None:
    company_table = op.create_table(
        "company",
        sa.Column("id", sa.UUID, nullable=False, primary_key=True),
        sa.Column("name", sa.String, unique=True, nullable=False, index=True),
        sa.Column("description", sa.String),
        sa.Column('mode', sa.Enum(CompanyMode), nullable=False, default=CompanyMode.DRAFT),
        sa.Column('rating', sa.SmallInteger, default=0),
    )
    op.add_column("user", sa.Column("company_id", sa.UUID, nullable=True))
    op.create_foreign_key('fk_user_company', 'user', 'company', ['company_id'], ['id'])

def downgrade() -> None:
    op.drop_table('company')
    op.drop_column('user', "company_id")
    op.execute("DROP TYPE companymode;")
