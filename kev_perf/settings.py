from kev.loading import KevHandler


s3_bucket = 'atlaslabsllc'
redis_host = 'redis1.atlaslabs.org'
dynamo_table = 'kev-perf'
active_db = 'dynamodb'

kev_handler = KevHandler({
    's3': {
        'backend': 'kev.backends.s3.db.S3DB',
        'connection': {
            'bucket': s3_bucket,
        }
    },
    #'redis': {
    #    'backend': 'kev.backends.redis.db.RedisDB',
    #    'connection': {
    #        'host': redis_host,
    #        'port': 6379,
    #    }
    #},
    'dynamodb': {
        'backend': 'kev.backends.dynamodb.db.DynamoDB',
        'connection': {
            'table': dynamo_table,
        }
    }
})
