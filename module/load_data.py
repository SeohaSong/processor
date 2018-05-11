
from aws_handler import S3


s3 = S3("seohasong", "./key/public-key.csv")
data = s3.get_key("public/imdb/master")
open("./data/imdb_master_df", "wb").write(data)
