"""added models from task (fixed relationships and fks)

Revision ID: 4afd12f91abe
Revises: ffc2b78e29ef
Create Date: 2025-04-03 09:49:37.297213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4afd12f91abe'
down_revision: Union[str, None] = 'ffc2b78e29ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
