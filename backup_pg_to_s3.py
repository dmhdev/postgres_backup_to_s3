import os, gzip, boto3, uuid
from sh import pg_dump


class PostgresBackup:

  def __init__(self, s3_bucket_name, db_backup_file_path, pg_user, pg_pass, pg_db_name):
    self.s3_bucket_name = s3_bucket_name
    self.db_backup_file_path = db_backup_file_path
    self.pg_user = pg_user
    self.pg_pass = pg_pass
    self.pg_db_name = pg_db_name
  

  def create_db_backup(self):

  	os.putenv("PGPASSWORD",self.pg_pass)

  	# Backup Postgres DB to gzipped file
  	with gzip.open(self.db_backup_file_path, "wb") as f:
  		pg_dump("-h", "localhost", "-U", self.pg_user, self.pg_db_name, _out=f)

  def push_backup_to_s3(self):

  	# Connect to S3
  	s3 = boto3.client("s3")

  	# Push DB to S3
  	s3_file_name = "db-%s.gz" % (str(uuid.uuid4()))
  	s3.upload_file(self.db_backup_file_path, self.s3_bucket_name, s3_file_name)

  def delete_db_backup(self):
    os.remove(self.db_backup_file_path)


if __name__ == "__main__":
  
  postgres_backup = PostgresBackup('my-bucket', '/path/to_db_file.gz', 'ubuntu', 'password', 'example_db')

	postgres_backup.create_db_backup()
	postgres_backup.push_backup_to_s3()
  postgres_backup.delete_db_backup()
	
