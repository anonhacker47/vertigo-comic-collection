"""Issue

Revision ID: f12c29dfb65d
Revises: 
Create Date: 2022-11-09 13:36:19.934146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f12c29dfb65d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('first_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['users.id'], )
    )
    op.create_table('series',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=280), nullable=False),
    sa.Column('publisher', sa.String(length=280), nullable=True),
    sa.Column('genre', sa.String(length=280), nullable=True),
    sa.Column('main_char', sa.String(length=280), nullable=True),
    sa.Column('writer', sa.String(length=280), nullable=True),
    sa.Column('artist', sa.String(length=280), nullable=True),
    sa.Column('editor', sa.String(length=280), nullable=True),
    sa.Column('summary', sa.String(length=570), nullable=True),
    sa.Column('series_format', sa.String(length=100), nullable=True),
    sa.Column('books_count', sa.Integer(), nullable=True),
    sa.Column('read_whole', sa.Integer(), nullable=True),
    sa.Column('have_whole', sa.Integer(), nullable=True),
    sa.Column('dominant_color', sa.String(length=280), nullable=True),
    sa.Column('slug', sa.String(length=280), nullable=True),
    sa.Column('thumbnail', sa.String(length=280), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_series_timestamp'), 'series', ['timestamp'], unique=False)
    op.create_index(op.f('ix_series_user_id'), 'series', ['user_id'], unique=False)
    op.create_table('tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('access_token', sa.String(length=64), nullable=False),
    sa.Column('access_expiration', sa.DateTime(), nullable=False),
    sa.Column('refresh_token', sa.String(length=64), nullable=False),
    sa.Column('refresh_expiration', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tokens_access_token'), 'tokens', ['access_token'], unique=False)
    op.create_index(op.f('ix_tokens_refresh_token'), 'tokens', ['refresh_token'], unique=False)
    op.create_index(op.f('ix_tokens_user_id'), 'tokens', ['user_id'], unique=False)
    op.create_table('issue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=280), nullable=False),
    sa.Column('slug', sa.String(length=280), nullable=True),
    sa.Column('read_whole', sa.Integer(), nullable=True),
    sa.Column('have_whole', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('series_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['series_id'], ['series.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_issue_series_id'), 'issue', ['series_id'], unique=False)
    op.create_index(op.f('ix_issue_timestamp'), 'issue', ['timestamp'], unique=False)
    op.create_index(op.f('ix_issue_user_id'), 'issue', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_issue_user_id'), table_name='issue')
    op.drop_index(op.f('ix_issue_timestamp'), table_name='issue')
    op.drop_index(op.f('ix_issue_series_id'), table_name='issue')
    op.drop_table('issue')
    op.drop_index(op.f('ix_tokens_user_id'), table_name='tokens')
    op.drop_index(op.f('ix_tokens_refresh_token'), table_name='tokens')
    op.drop_index(op.f('ix_tokens_access_token'), table_name='tokens')
    op.drop_table('tokens')
    op.drop_index(op.f('ix_series_user_id'), table_name='series')
    op.drop_index(op.f('ix_series_timestamp'), table_name='series')
    op.drop_table('series')
    op.drop_table('followers')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
