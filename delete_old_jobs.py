# Script to delete the oldest 400 jobs from the database
from __init__ import create_app, db
from app.models import Job

def delete_oldest_jobs():
    app = create_app()
    with app.app_context():
        # Get the oldest 400 jobs ordered by creation date
        oldest_jobs = Job.query.order_by(Job.created_at).limit(400).all()

        if not oldest_jobs:
            print("No jobs found in the database.")
            return

        count = len(oldest_jobs)
        print(f"Found {count} oldest jobs to delete:")

        # Print details of jobs to be deleted
        for i, job in enumerate(oldest_jobs[:5], 1):  # Show first 5
            print(f"  {i}. {job.title} - {job.company} - Created: {job.created_at}")

        if count > 5:
            print(f"  ... and {count - 5} more jobs")

        # Confirm deletion
        confirm = input(f"\nAre you sure you want to delete these {count} jobs? (yes/no): ").lower().strip()

        if confirm == 'yes':
            # Delete the jobs
            for job in oldest_jobs:
                db.session.delete(job)

            db.session.commit()
            print(f"Successfully deleted {count} oldest jobs from the database.")
        else:
            print("Deletion cancelled.")

if __name__ == "__main__":
    delete_oldest_jobs()
