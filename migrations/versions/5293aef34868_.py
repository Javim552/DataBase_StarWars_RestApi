"""empty message

Revision ID: 5293aef34868
Revises: 496ade514967
Create Date: 2022-11-22 11:36:51.190060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5293aef34868'
down_revision = '496ade514967'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('namePerson', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('namePlanet', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idPlanet', sa.Integer(), nullable=True),
    sa.Column('idCharacter', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idCharacter'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['idPlanet'], ['planets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('userDatos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userName', sa.String(length=250), nullable=False),
    sa.Column('lastUserName', sa.String(length=250), nullable=False),
    sa.Column('idfavoritos', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idfavoritos'], ['favoritos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userDatos')
    op.drop_table('favoritos')
    op.drop_table('planets')
    op.drop_table('characters')
    # ### end Alembic commands ###