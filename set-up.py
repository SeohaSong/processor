
# The order is important.
from module import load_module
from module.aws_handler import S3


if __name__ == "__main__":
    
    print("[set-up.py] Loading IMDB data from AWS S3...")
    s3 = S3("seohasong", "./key/public-key.csv")
    data = s3.get_key("public/imdb/master")
    open("./data/imdb_master_df", "wb").write(data)
