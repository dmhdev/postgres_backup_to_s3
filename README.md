# postgres_to_s3
Script that backs up PostgreSQL Database and uploads it to an Amazon S3 Bucket

Example usage:

    if __name__ == "__main__":

      pg_backup = PGBackupDB('my-s3-bucket', './db_file_backup.gz', 'ubuntu', 'password', 'example_db')

      pg_backup.create_db_backup()
      pg_backup.push_backup_to_s3()
      pg_backup.delete_db_backup()
