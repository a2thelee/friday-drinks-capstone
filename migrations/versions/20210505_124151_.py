"""empty message

Revision ID: b93cac385963
Revises: d5b972b9bb93
Create Date: 2021-05-05 12:41:51.892564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b93cac385963'
down_revision = 'd5b972b9bb93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('drinks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('isAlcoholic', sa.Boolean(), nullable=True),
    sa.Column('photo_url', sa.String(length=1000), nullable=True),
    sa.Column('instructions', sa.String(length=1500), nullable=False),
    sa.Column('authorId', sa.Integer(), nullable=True),
    sa.Column('favorites', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('ingredients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=75), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('drink_ingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('drinkId', sa.Integer(), nullable=False),
    sa.Column('ingredientId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['drinkId'], ['drinks.id'], ),
    sa.ForeignKeyConstraint(['ingredientId'], ['ingredients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_drinks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('drinkId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['drinkId'], ['drinks.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite_drinks')
    op.drop_table('drink_ingredient')
    op.drop_table('users')
    op.drop_table('ingredients')
    op.drop_table('drinks')
    # ### end Alembic commands ###
