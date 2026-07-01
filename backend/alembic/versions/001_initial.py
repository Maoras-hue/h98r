"""Initial migration

Revision ID: 001
Revises: 
Create Date: 2024-01-01 00:00:00.000000


"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('full_name', sa.String(), nullable=True),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('is_premium', sa.Boolean(), nullable=False, server_default='false'),
        sa.Column('profile_picture', sa.String(), nullable=True),
        sa.Column('bio', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('last_login', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)

    # Create contents table
    op.create_table(
        'contents',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('content_type', sa.Enum('BLOG_POST', 'SOCIAL_MEDIA', 'EMAIL', 'NEWSLETTER', 'AD_COPY', 'PRODUCT_DESCRIPTION', name='contenttype'), nullable=False, server_default='BLOG_POST'),
        sa.Column('tone', sa.Enum('PROFESSIONAL', 'CASUAL', 'FUNNY', 'FORMAL', 'FRIENDLY', name='contenttone'), nullable=False, server_default='PROFESSIONAL'),
        sa.Column('language', sa.String(), nullable=False, server_default='en'),
        sa.Column('keywords', sa.String(), nullable=True),
        sa.Column('meta_description', sa.String(), nullable=True),
        sa.Column('slug', sa.String(), nullable=True),
        sa.Column('seo_score', sa.Float(), nullable=False, server_default='0.0'),
        sa.Column('model_used', sa.String(), nullable=False, server_default='gpt-4'),
        sa.Column('tokens_used', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contents_slug'), 'contents', ['slug'], unique=False)

    # Create content_templates table
    op.create_table(
        'content_templates',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('content_type', sa.Enum('BLOG_POST', 'SOCIAL_MEDIA', 'EMAIL', 'NEWSLETTER', 'AD_COPY', 'PRODUCT_DESCRIPTION', name='contenttype'), nullable=False),
        sa.Column('template', sa.Text(), nullable=False),
        sa.Column('variables', sa.String(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default='true'),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # Create user_credits table
    op.create_table(
        'user_credits',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('total_credits', sa.Float(), nullable=False, server_default='10.0'),
        sa.Column('used_credits', sa.Float(), nullable=False, server_default='0.0'),
        sa.Column('available_credits', sa.Float(), nullable=False, server_default='10.0'),
        sa.Column('last_reset', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('next_reset', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id')
    )

    # Create credit_transactions table
    op.create_table(
        'credit_transactions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('transaction_type', sa.Enum('PURCHASE', 'USE', 'REFUND', 'BONUS', 'MONTHLY_RESET', name='transactiontype'), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('reason', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('credit_transactions')
    op.drop_table('user_credits')
    op.drop_table('content_templates')
    op.drop_table('contents')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
