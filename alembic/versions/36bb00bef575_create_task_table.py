"""create task table

Revision ID: 36bb00bef575
Revises: 51368d446dc1
Create Date: 2023-04-19 15:52:53.885647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36bb00bef575'
down_revision = '51368d446dc1'
branch_labels = None
depends_on = None

from src.task.schemas import TaskStatus
def upgrade() -> None:
    task_table = op.create_table(
        "task",
        sa.Column("id", sa.UUID, nullable=False, primary_key=True),
        sa.Column("summary", sa.String, nullable=False),
        sa.Column("description", sa.String),
        sa.Column('status', sa.Enum(TaskStatus), nullable=False, default=TaskStatus.TODO),
        sa.Column('priority', sa.SmallInteger, default=0),
        sa.Column("user_id", sa.UUID, nullable=True)
    )
    op.create_foreign_key('fk_task_user', 'task', 'user', ['user_id'], ['id'])


def downgrade() -> None:
    op.drop_table('task')
    op.execute("DROP TYPE taskstatus;")
