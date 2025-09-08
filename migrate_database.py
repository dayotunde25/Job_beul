#!/usr/bin/env python3
"""
Database migration script to add new fields to the User model
Run this script to update your existing database with the new profile fields
"""

import sqlite3
import os
from datetime import datetime

def migrate_database():
    """Add new columns to the User table"""
    db_path = 'instance/jobs.db'

    if not os.path.exists(db_path):
        print("Database file not found. Please start the Flask app first to create the database.")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # List of new columns to add
    new_columns = [
        ('city', 'VARCHAR(100)'),
        ('country', 'VARCHAR(100)'),
        ('linkedin_url', 'VARCHAR(200)'),
        ('portfolio_url', 'VARCHAR(200)'),
        ('current_position', 'VARCHAR(100)'),
        ('years_of_experience', 'INTEGER'),
        ('certifications', 'TEXT'),
        ('languages', 'TEXT'),
        ('preferred_job_types', 'TEXT'),
        ('preferred_locations', 'TEXT'),
        ('salary_expectation_min', 'INTEGER'),
        ('salary_expectation_max', 'INTEGER'),
        ('remote_work_preference', 'VARCHAR(20)'),
        ('profile_completeness', 'INTEGER DEFAULT 0'),
        ('updated_at', 'DATETIME')
    ]
    
    print("Starting database migration...")
    
    # Check which columns already exist
    cursor.execute("PRAGMA table_info(user)")
    existing_columns = [column[1] for column in cursor.fetchall()]
    
    # Add new columns if they don't exist
    for column_name, column_type in new_columns:
        if column_name not in existing_columns:
            try:
                alter_sql = f"ALTER TABLE user ADD COLUMN {column_name} {column_type}"
                cursor.execute(alter_sql)
                print(f"✓ Added column: {column_name}")
            except sqlite3.Error as e:
                print(f"✗ Error adding column {column_name}: {e}")
        else:
            print(f"- Column {column_name} already exists")
    
    # Update existing users with default values
    try:
        cursor.execute("""
            UPDATE user 
            SET updated_at = ?, profile_completeness = 0 
            WHERE updated_at IS NULL
        """, (datetime.utcnow(),))
        print("✓ Updated existing users with default values")
    except sqlite3.Error as e:
        print(f"✗ Error updating existing users: {e}")
    
    conn.commit()
    conn.close()
    print("Database migration completed successfully!")

def verify_migration():
    """Verify that the migration was successful"""
    db_path = 'jobs.db'
    
    if not os.path.exists(db_path):
        print("Database file not found.")
        return False
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check table structure
    cursor.execute("PRAGMA table_info(user)")
    columns = cursor.fetchall()
    
    print("\nCurrent User table structure:")
    print("-" * 50)
    for column in columns:
        print(f"{column[1]:<25} {column[2]:<15} {'NOT NULL' if column[3] else 'NULL'}")
    
    # Check if we have any users
    cursor.execute("SELECT COUNT(*) FROM user")
    user_count = cursor.fetchone()[0]
    print(f"\nTotal users in database: {user_count}")
    
    # Check jobs table
    cursor.execute("SELECT COUNT(*) FROM job")
    job_count = cursor.fetchone()[0]
    print(f"Total jobs in database: {job_count}")
    
    conn.close()
    return True

if __name__ == "__main__":
    print("JobBoard Database Migration Tool")
    print("=" * 40)
    
    try:
        migrate_database()
        print("\n" + "=" * 40)
        verify_migration()
        
        print("\n" + "=" * 40)
        print("Migration completed successfully!")
        print("\nNext steps:")
        print("1. Start your Flask application")
        print("2. Test the new profile features")
        print("3. Check job recommendations")
        print("4. Verify admin-only scraper access")
        
    except Exception as e:
        print(f"Migration failed: {e}")
        print("Please check your database and try again.")
