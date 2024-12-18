"""empty message

Revision ID: 4074e362103e
Revises: 
Create Date: 2024-11-06 12:25:46.120542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4074e362103e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produto',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('categoria', sa.String(length=100), nullable=False),
    sa.Column('fornecedor', sa.String(length=100), nullable=False),
    sa.Column('descricao', sa.String(length=500), nullable=False),
    sa.Column('data_de_fabricacao', sa.DateTime(), nullable=False),
    sa.Column('data_de_validade', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produto')
    # ### end Alembic commands ###
