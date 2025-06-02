"""primeira

Revision ID: 42f190acc411
Revises: 
Create Date: 2025-05-28 11:15:01.339186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42f190acc411'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'pessoa',
        sa.Column ('id', sa.Integer(), primary_key=True),
        sa.Column ('name', sa.String(length=50), nullable=False),
        sa.Column ('email', sa.String(length=50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table(
        'pessoa'
    )
