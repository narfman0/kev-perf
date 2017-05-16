from kev.loading import KevHandler

from kev_perf import settings


kev_handler = KevHandler({
    's3': {
        'backend': 'kev.backends.s3.db.S3DB',
        'connection': {
            'bucket': settings.s3_bucket,
        }
    },
    'redis': {
        'backend': 'kev.backends.redis.db.RedisDB',
        'connection': {
            'host': settings.redis_host,
            'port': 6379,
        }
    },
    'dynamodb': {
        'backend': 'kev.backends.dynamodb.db.DynamoDB',
        'connection': {
            'table': settings.dynomo_table,
        }
    }
})
