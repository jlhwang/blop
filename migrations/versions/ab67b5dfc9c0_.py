"""empty message

Revision ID: ab67b5dfc9c0
Revises: f4f00d456287
Create Date: 2016-06-09 16:23:14.832909

"""

# revision identifiers, used by Alembic.
revision = 'ab67b5dfc9c0'
down_revision = 'f4f00d456287'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('general_locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=15), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('specific_locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('general_location_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['general_location_id'], ['general_locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mapping',
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('incident_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['incident_id'], ['incidents.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['types.id'], )
    )
    op.add_column('incidents', sa.Column('date', sa.Date(), nullable=True))
    op.add_column('incidents', sa.Column('general_location_id', sa.Integer(), nullable=True))
    op.add_column('incidents', sa.Column('specific_location_id', sa.Integer(), nullable=True))
    op.add_column('incidents', sa.Column('time', sa.Time(), nullable=True))
    op.create_foreign_key(None, 'incidents', 'general_locations', ['general_location_id'], ['id'])
    op.create_foreign_key(None, 'incidents', 'specific_locations', ['specific_location_id'], ['id'])
    op.drop_column('incidents', 'eventtype')
    op.drop_column('incidents', 'location')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('incidents', sa.Column('location', sa.VARCHAR(length=25), autoincrement=False, nullable=True))
    op.add_column('incidents', sa.Column('eventtype', sa.VARCHAR(length=25), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'incidents', type_='foreignkey')
    op.drop_constraint(None, 'incidents', type_='foreignkey')
    op.drop_column('incidents', 'time')
    op.drop_column('incidents', 'specific_location_id')
    op.drop_column('incidents', 'general_location_id')
    op.drop_column('incidents', 'date')
    op.drop_table('mapping')
    op.drop_table('specific_locations')
    op.drop_table('types')
    op.drop_table('general_locations')
    ### end Alembic commands ###
