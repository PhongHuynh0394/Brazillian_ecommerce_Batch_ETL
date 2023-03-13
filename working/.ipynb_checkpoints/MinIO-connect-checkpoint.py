from minio import Minio
from minio.error import S3Error


def main():
    client = Minio(
        endpoint="minio:9000",
        access_key="phonghuynh",
        secret_key="phonghuynh",
        secure=False
    )

    #Check if the bucket exist
    bucket = "warehouse-script"
    if client.bucket_exists(bucket):
        print(f"bucket {bucket} exits")
    else:
        print(f"bucket {bucket} does not exist")
        print(f"Create bucket {bucket}")
        client.make_bucket(bucket)

    #list all buckets -> list
    buckets = client.list_buckets()
    print(buckets) #warehouse-manual

    #get all object in warehouse-manual
    objects = client.list_objects(str(buckets[0]))
    obj_list = [obj.object_name for obj in objects]
    for obj in obj_list:
        client.fget_object(str(buckets[0]), obj, "./data/" + obj)
        
    #remove object in warehouse-script
    #client.remove_object(str(buckets[1]), obj_list[0])

    #Check warehouse-script
    print(client.list_objects(str(buckets[1])))
    # put to warehouse-script
    for obj in obj_list:
        client.fput_object(str(buckets[1]), obj, "./data/" + obj)



if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)