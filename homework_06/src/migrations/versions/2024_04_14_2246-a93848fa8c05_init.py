"""init

Revision ID: a93848fa8c05
Revises: 
Create Date: 2024-04-14 22:46:28.074418

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a93848fa8c05"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )


def downgrade():
    op.drop_table("user")
